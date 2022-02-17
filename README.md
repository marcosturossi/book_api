# book_api
## API para Acervo de Livros
Esse projeto usa as tecnologias Django e DjangoREST Framework para a criação de um sistema de gestão simples de livros.

Dependências
```
python==3.5+
Django==4.0.2
django-filter==21.1
djangorestframework==3.13.1
```

1 Instalar Depêndencias (Verificar se está na pasta correta)
```
pip install requirements.txt
```

2 Sincronize a Base de Dados
```
python manage.py makemigrations
python manage.py migrate
```

3 Criar Usuário Adm
```
python manage.py createsuperuser
```

4 Teste a instalação no ambiente de teste
```
python manage.py runserver
```

5 No navegador coloque o caminho http://127.0.0.1:8000
```
Deve abrir uma página HTML do DjangoREST
```
6 Documentação 
```
A documentação da API está disponível em:  http://127.0.0.1:8000/documentation
```
Informações importantes: 
```
Este projeto usa como sistema de autenticação via TOKEN, sendo assim só deve ser utilizado em produção com uma conexão HTTPS.
Se for colocado em produção lembrar de preencher a secret_key do django com um hash seguro.
```
