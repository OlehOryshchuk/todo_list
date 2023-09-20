# todo_list
Todo list task management web application designed to help you efficiently organize your daily tasks and stay on top of
your to-do-lists.

# Key features
- Task Creation.Easily create task and assign them deadlines to unsure nothing is overlooked
- Tagging System. Organize tasks using customizable tags to group and categorize your to-do items.
- Task Status. Monitor task completion status, helping you track progress
    
## Installation

A quick introduction of the minimal setup you need to get

```shell
git clone https://github.com/OlehOryshchuk/todo_list.git
cd todo_list
```

```shell
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

# DB structure diagram
 ![DB-structure diagram](/static/img/db_diagram.png)
 [DB-structure diagram](/static/img/db_diagram.png)
 
# Demo
Superuser for admin site (or create another one by yourself: `python manage.py createsuperuser`):
- Name: Admin
- Password: T00bri3t?4

# Pages
![Home page](/static/img/home_page.png)
![Tag list page](/static/img/tag_list_page.png)
![Task create page](/static/img/create_task.png)
![Tag create page](/static/img/create_tag.png)
