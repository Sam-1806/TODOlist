# TODO List App
This is a web-based To-Do List application developed using Django. The app allows users to create, read, update, and delete tasks in a to-do list. It provides a RESTful API for managing tasks and includes a Django admin interface for easy management.

Features:-
-Create a new task with a title, description, due date, and optional tags.
-Read individual tasks and view all tasks.
-Update task details such as title, description, due date, tags, and status.
-Delete tasks.
-Timestamp is automatically set when creating a task and cannot be edited.
-Tasks have a status that can be set to OPEN, WORKING, DONE, or OVERDUE.
-Validation checks are in place to enforce mandatory fields and logical constraints.

Prerequisites:-
-Python 3.8 or higher
-Django 3.1 or higher
-Django Rest Framework 3.1 or higher

Installation:-
-Clone the repository-> git clone <>
-Create a virtual environment:
     python3 -m venv env
-Activate the virtual environment:
     For Windows- env\Scripts\activate
     For macOS/Linux- source env/bin/activate
-Install the dependencies:
     pip install -r requirements.txt

Usage:-
Run the Django development server:
     python manage.py runserver
     
     
Access the web application at http://localhost:8000/.

Access the Django admin interface at http://localhost:8000/admin/.
