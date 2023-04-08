from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.test.client import Client
from library_app.models import Genre
from json import dumps


class GenreViewSetTests(TestCase):
    url = '/rest/Genre/'
    
    def setUp(self):
        self.client = Client()
        self.creds_superuser = {'username': 'super', 'password': 'super'}
        self.creds_user = {'username': 'default', 'password': 'default'}
        self.superuser = User.objects.create_user(is_superuser=True, **self.creds_superuser)
        self.user = User.objects.create_user(**self.creds_user)

    def test_get(self):
        # logging in with superuser creds
        self.client.login(**self.creds_user)
        # GET
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # logging out
        self.client.logout()

    def test_manage_superuser(self):
        # logging in with superuser creds
        self.client.login(**self.creds_superuser)
        # POST
        name = 'abcdef'
        resp_post = self.client.post(self.url, data={'name': name})
        self.assertEqual(resp_post.status_code, status.HTTP_201_CREATED)
        # PUT
        created_id = Genre.objects.get(name=name).id
        description = name[::-1]
        resp_put = self.client.put(
            f'{self.url}?id={created_id}', 
            data=dumps({'description': description})
        )
        self.assertEqual(resp_put.status_code, status.HTTP_200_OK)
        self.assertEqual(Genre.objects.get(id=created_id).description, description)
        # DELETE EXISTING
        resp_delete = self.client.delete(f'{self.url}?id={created_id}')
        self.assertEqual(resp_delete.status_code, status.HTTP_204_NO_CONTENT)
        # DELETE NONEXISTENT
        repeating_delete = self.client.delete(f'{self.url}?id={created_id}')
        self.assertEqual(repeating_delete.status_code, status.HTTP_404_NOT_FOUND)

        # logging out
        self.client.logout()

    def test_manage_user(self):
        # logging in with superuser creds
        self.client.login(**self.creds_user)
        # POST
        name = 'abcdef'
        resp_post = self.client.post(self.url, data={'name': name})
        self.assertEqual(resp_post.status_code, status.HTTP_403_FORBIDDEN)
        # PUT
        created = Genre.objects.create(name=name)
        resp_put = self.client.put(
            f'{self.url}?id={created.id}', 
            data=dumps({'description': name[::-1]})
        )
        self.assertEqual(resp_put.status_code, status.HTTP_403_FORBIDDEN)
        # DELETE EXISTING
        resp_delete = self.client.delete(f'{self.url}?id={created.id}')
        self.assertEqual(resp_delete.status_code, status.HTTP_403_FORBIDDEN)
        # clean up
        created.delete()
        # logging out
        self.client.logout()