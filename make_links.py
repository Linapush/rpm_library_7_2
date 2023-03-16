from psycopg2 import connect
from dotenv import load_dotenv
from os import getenv

load_dotenv()
credentials = {
    'host' : getenv('PG_HOST'),
    'port' : int(getenv('PG_PORT')),
    'user' : getenv('PG_USER'),
    'password' : getenv('PG_PASSWORD'),
    'dbname' : getenv('PG_DBNAME')
}

connection = connect(**credentials)
cursor = connection.cursor()

get_ids = 'select id from'
cursor.execute(f'{get_ids} library.book')
book_ids = [id[0] for id in cursor.fetchall()]

cursor.execute(f'{get_ids} library.author')
author_ids = [id[0] for id in cursor.fetchall()]

books_authors_ratio = len(book_ids) // len(author_ids)
request = "INSERT INTO library.book_author (book_id, author_id) VALUES ('{0}', '{1}')"

for book_ind in range(len(book_ids)//2):
    author_ind = book_ind // books_authors_ratio
    cursor.execute(request.format(book_ids[book_ind], author_ids[author_ind]))
    print('Current index: ', book_ind)

connection.commit()
cursor.close()
connection.close()
