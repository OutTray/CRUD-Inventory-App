# Inventory Tracking Web Application

Created by Eric Shum for the Summer 2022 Shopify Backend Developer Intern Challenge

## Languages and Frameworks Used:

- Python 3.10 or above
- MySQL 8.0 or above
- Django 4.0 or above
- HTML

## Installation Instructions

1. Install pip
2. Set up a virtual environment (optional but recommended)
3. Enter the command:

```
python -m pip install Django
```

4. Create a MySQL database named �shopify_2022_inventory� or go to CRUD/settings.py, scroll down to DATABASES, and change the NAME field to the desired database name. Alter the HOST and PORT fields if desired.
5. In the CRUD folder (the same folder as CRUD/settings.py, create a file named "config.py" with the username and password of the SQL server:

```
sql_username = �USERNAME�
sql_password = �PASSWORD�
```
6. To run the project, naviage to the directory containing the file manage.py and run the following command:
```
python manage.py runserver
```
7. Copy the development server address (typically http://127.0.0.1:8000/) and add the path /inventory/show to access the inventory. The link should be:
```
http://127.0.0.1:8000/inventory/show
```