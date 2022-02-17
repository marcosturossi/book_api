# book_api
Esse projeto usa as tecnologias Django e DjangoREST Framework para a criação de um sistema de gestão simples de livros.

Dependências

Django==4.0.2
django-filter==21.1
djangorestframework==3.13.1

1 Instalar Depêndencias
Verificar se está na pasta correta.

Windows 
pip install requirements.txt
Linux
pip3 install requirements.txt

2 Sincronize a Base de Dados

python manage.py makemigrations
python manage.py migrate

3 Criar Usuário Adm

python manage.py createsuperuser

4 Teste a instalação no ambiente de teste

python manage.py runserver
