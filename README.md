#A Template to create your own Flask Application with MVC architecture

## First step is to create a folder with the name of the application

## Then create the following files and folders :

~/Application_Name
    |-- run.py
    |-- config.py
    |__ /env             # Virtual Environment
    |__ /app             # Our Application Module
         |-- __init__.py
         |-- /module_one      #First module 
             |-- __init__.py
             |-- controllers.py
             |-- models.py                
         |__ /templates
             |__ /module_one
                 |-- hello.html
         |__ /static
         |__ ..
         |__ .
    |__ ..
    |__ .