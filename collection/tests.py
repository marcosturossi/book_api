from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import User, Collection, Category, Book


class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='marcos')
        self.collection = Collection.objects.get(user=self.user)
        self.token = Token.objects.get(user=self.user)

    def test_create_collection_token(self):
        """Este teste tem como objetivo verificar se o sistema irá criar o Token e uma o Collection
        quando um usuário for criado"""
        self.assertEqual(self.user, self.collection.user)
        self.assertEqual(self.user, self.token.user)


class CollectionTeste(TestCase):
    def setUp(self):
        # TODO Refatorar para reduzir repetição de código
        self.user = User.objects.create(username='marcos')  # Deve criar o Collection Automaticamente
        self.token = Token.objects.get(user=self.user)
        self.category1 = Category.objects.create(name='Financeiro', collection=self.user.collection)
        self.category2 = Category.objects.create(name='Programação', collection=self.user.collection)
        book_data = {'name': 'Python do 0 ao Avançado', 'author': 'Fernando',
                     'category': Category.objects.get(name='Financeiro'), 'created': timezone.now(),
                     'slug': slugify('Python do 0 ao Avançado')}
        self.book = Book.objects.create(**book_data)
        self.client_not_authenticated = APIClient()
        self.client_authenticated = APIClient()
        self.client_authenticated.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def teste_collection_get_method(self):
        """ Verifica se com method GET na view CreateView do collections """

        # Cliente não Autenticado
        response = self.client_not_authenticated.get(reverse('collections:collection_detail',
                                                             kwargs={'pk': self.user.collection.id}))
        self.assertEqual(response.status_code, 401)

        # Cliente Autenticado
        response = self.client_authenticated.get(reverse('collections:collection_detail',
                                                         kwargs={'pk': self.user.collection.id}))
        self.assertEqual(response.status_code, 200)
        # TODO implementar a verificação dos dados na view

    def teste_book_get_method(self):
        """ Verifica a view com método GET na ListCreateAPI do book """
        # Cliente não Autenticado
        response = self.client_not_authenticated.get(reverse('collections:book_list'))
        self.assertEqual(response.status_code, 401)
        response = self.client_not_authenticated.get(reverse('collections:book_detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, 401)

        # Cliente Autenticado
        response = self.client_authenticated.get(reverse('collections:book_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client_authenticated.get(reverse('collections:book_detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, 200)
        # TODO implementar a verificação dos dados na view

    def teste_book_post_method(self):
        """ Verifica a view com método POST na ListCreateAPI do book """
        book_data = {'name': 'Do 0 a 1 milhão', 'collection': Collection.objects.get(user__username='marcos').id,
                     'author': 'Gustavo', 'category': Category.objects.get(name='Financeiro').id,
                     'slug': slugify('Do 0 a 1 milhão')}
        # Cliente não Autenticado
        response = self.client_not_authenticated.post(reverse('collections:book_list'), book_data, format='json')
        self.assertEqual(response.status_code, 401)

        # Cliente Autenticado
        response = self.client_authenticated.post(reverse('collections:book_list'), book_data, format='json')
        self.assertEqual(response.status_code, 201)
        # TODO implementar a verificação dos dados na view

    def teste_category_get_method(self):
        """ Verifica se a view com método GET na RetrieveUpdateDestroyAPIView da Category """
        # Cliente não Autenticado
        response = self.client_not_authenticated.get(reverse('collections:category_list'))
        self.assertEqual(response.status_code, 401)
        response = self.client_not_authenticated.get(
            reverse('collections:category_detail', kwargs={'pk': self.category1.id}))
        self.assertEqual(response.status_code, 401)

        # Cliente Autenticado
        response = self.client_authenticated.get(reverse('collections:category_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client_authenticated.get(
            reverse('collections:category_detail', kwargs={'pk': self.category1.id}))
        self.assertEqual(response.status_code, 200)
        # TODO implementar a verificação dos dados na view

    def teste_category_post_method(self):
        """ Verifica se a view com método POST na ListCreateAPI da Category """
        # Cliente não Autenticado
        category_data = {'name': 'AutoAjuda', 'collection': self.user.collection.id, 'slug': slugify('AutoAjuda')}
        response = self.client_not_authenticated.post(reverse('collections:category_list'), category_data,
                                                      format='json')
        self.assertEqual(response.status_code, 401)
        # Cliente Autenticado
        response = self.client_authenticated.post(reverse('collections:category_list'), category_data,
                                                  format='json')
        self.assertEqual(response.status_code, 201)
        # TODO implementar a verificação dos dados na view

    def testa_book_put_delete_method(self):
        """ Verifica se a view com método PUT/DELETE na RetrieveUpdateDestroyAPIView da Book """
        book = Book.objects.last()
        self.assertEqual(book.name, 'Python do 0 ao Avançado')
        book_data = {'name': 'Do 0 a 1 milhão', 'collection': Collection.objects.get(user__username='marcos').id,
                     'author': 'Gustavo', 'category': Category.objects.get(name='Financeiro').id,
                     'slug': slugify('Do 0 a 1 milhão')}

        # PUT METHOD
        # Cliente não autenticado
        response = self.client_not_authenticated.put(reverse('collections:book_detail', kwargs={'pk': book.id}),
                                                     book_data, format='json')
        self.assertEqual(response.status_code, 401)
        # Cliente autenticado
        response = self.client_authenticated.put(reverse('collections:book_detail', kwargs={'pk': book.id}), book_data,
                                                 format='json')
        self.assertEqual(response.status_code, 200)
        book = Book.objects.last()  # Atualiza o dado
        self.assertEqual(book.name, 'Do 0 a 1 milhão')

        # DELETE METHOD
        # Cliente não autenticado
        response = self.client_not_authenticated.delete(reverse('collections:book_detail', kwargs={'pk': book.id}))
        self.assertEqual(response.status_code, 401)
        books = Book.objects.all()
        self.assertEqual(len(books), 1)

        # Cliente autenticado
        response = self.client_authenticated.delete(reverse('collections:book_detail', kwargs={'pk': book.id}))
        self.assertEqual(response.status_code, 204)
        books = Book.objects.all()
        self.assertEqual(len(books), 0)
