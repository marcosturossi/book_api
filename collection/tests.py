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
        self.category1 = Category.objects.create(name='Financeiro')
        self.category2 = Category.objects.create(name='Programação')
        book_data = {'name': 'Python do 0 ao Avançado', 'collection': Collection.objects.get(user__username='marcos'),
                     'author': 'Fernando', 'category': Category.objects.get(name='Financeiro'),
                     'created': timezone.now(), 'slug': slugify('Python do 0 ao Avançado')}
        self.book = Book.objects.create(**book_data)
        self.client = APIClient()

    def teste_collection_get_method(self):
        """ Verifica se a da view (collections-detail) """
        response = self.client.get(reverse('collections:collection_detail', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, 200)
        # TODO implementar a verificação dos dados na view

    def teste_book_get_method(self):
        response = self.client.get(reverse('collections:book_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('collections:book_detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, 200)
        # TODO implementar a verificação dos dados na view

    def teste_book_post_method(self):
        book_data = {'name': 'Do 0 a 1 milhão', 'collection': Collection.objects.get(user__username='marcos').id,
                     'author': 'Gustavo', 'category': Category.objects.get(name='Financeiro').id,
                     'slug': slugify('Do 0 a 1 milhão')}
        response = self.client.post(reverse('collections:book_list'), book_data, format='json')
        self.assertEqual(response.status_code, 201)
        # TODO implementar a verificação dos dados na view

    def teste_category_get_method(self):
        response = self.client.get(reverse('collections:category_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('collections:category_detail', kwargs={'pk': self.category1.id}))
        self.assertEqual(response.status_code, 200)
        # TODO implementar a verificação dos dados na view

    def teste_category_post_method(self):
        category_data = {'name': 'AutoAjuda', 'slug': slugify('AutoAjuda')}
        response = self.client.post(reverse('collections:category_list'), category_data, format='json')
        self.assertEqual(response.status_code, 201)
        # TODO implementar a verificação dos dados na view

    def testa_book_put_delete_method(self):
        book = Book.objects.last()
        self.assertEqual(book.name, 'Python do 0 ao Avançado')
        book_data = {'name': 'Do 0 a 1 milhão', 'collection': Collection.objects.get(user__username='marcos').id,
                     'author': 'Gustavo', 'category': Category.objects.get(name='Financeiro').id,
                     'slug': slugify('Do 0 a 1 milhão')}

        # PUT METHOD
        response = self.client.put(reverse('collections:book_detail', kwargs={'pk': book.id}), book_data,
                                   format='json')
        self.assertEqual(response.status_code, 200)
        book = Book.objects.last()  # Atualiza o dado
        self.assertEqual(book.name, 'Do 0 a 1 milhão')

        # DELETE METHOD
        response = self.client.delete(reverse('collections:book_detail', kwargs={'pk': book.id}))
        self.assertEqual(response.status_code, 204)
        books = Book.objects.all()
        self.assertEqual(len(books), 0)


