LINES_PER_PAGE = 40

with open('zarathustra.txt', 'r') as file:
    lines = file.readlines()

page_num = 1
while lines:
    page = '\n'.join(lines[:LINES_PER_PAGE])
    del lines[:LINES_PER_PAGE]
    with open(f'{page_num}.txt', 'w') as file:
        file.write(page)
    page_num += 1