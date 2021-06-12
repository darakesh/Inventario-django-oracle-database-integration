#Inventario
####one stop to store all your products

[![Python Version](https://img.shields.io/badge/python-3.8-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2-brightgreen.svg)](https://djangoproject.com)


This is a django project to illustrate the implementation of an Oracle database and create a CRUD application. In this django app, user can create a new product, view all products, Edit or delete an existing product.

## screenshots
### Homepage
![Inventario homepage Screenshot](https://github.com/livingdead3551/Inventario-django-oracle-database-integration/blob/master/Screenshots/hompage.jpg)
![Inventario homepage with pagnation Screenshot](https://github.com/livingdead3551/Inventario-django-oracle-database-integration/blob/master/Screenshots/hompage%20with%20pagnation.jpg)
### Add Product
![Inventario Add Product Screenshot](https://github.com/livingdead3551/Inventario-django-oracle-database-integration/blob/master/Screenshots/hompage.jpg)
### Edit Product
![Inventario Edit Product Screenshot](https://github.com/livingdead3551/Inventario-django-oracle-database-integration/blob/master/Screenshots/hompage.jpg)
### Delete Product
![Inventario Delete Product Screenshot](https://github.com/livingdead3551/Inventario-django-oracle-database-integration/blob/master/Screenshots/hompage.jpg)


## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/livingdead3551/Inventario-django-oracle-database-integration.git
```

Install Oracle Database using the instructions given in [Django 3.2 oracle integration guide](https://github.com/livingdead3551/Inventario-django-oracle-database-integration/blob/master/django%203.2%20oracle%20integration%20guide.pdf).

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](https://github.com/livingdead3551/Inventario-django-oracle-database-integration/blob/master/LICENSE).