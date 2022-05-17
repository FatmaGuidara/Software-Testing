## What is Integration testing

Integration testing also known as integration and testing (I&T) is a type of software testing in which the different units, modules or components of a software application are tested as a combined entity. 

## Project Description
It's a Flask API that handles the get, post, delete of a todo.

## How to run the Flask API
```cmd
$  py -3 -m venv .venv
$  .venv\Scripts\activate
```
```cmd
$  set DATABASE_FILENAME=todos.db
$  python utils/create_db.py
$  python app.py 
```
and the Flask server should be running

## The Tests Scenerio

1. Create a client to the server
2. Retrieve all todos in the database (it should be empty by then)
3. Add 3 todos
4. Retrieve all todos in the database
5. Delete the first todo added
6. Retry to delete the already deleted todo
7. Try to delete non-existant todo
8. Retrieve all todos in the database (2)

*Note:* The test create its own database in a temporary file.

## How to run the tests
```cmd
$  pytest -v
```
**Preview**
![pytest](https://user-images.githubusercontent.com/62222721/168854480-cffb50d2-ff44-41c2-ba86-357fe301c902.png)


```cmd
$  pytest -vvv --cov=app tests/
```
**Preview**
![cov](https://user-images.githubusercontent.com/62222721/168854578-db8bab53-8348-4144-b904-b2ab54d09663.png)
