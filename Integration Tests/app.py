import os
import sqlite3
from flask import Flask, jsonify, request
import string
import random

def create_app(name):
    app = Flask(name)
    # Database Connexion 
    database_file_name = os.environ.get('DATABASE_FILENAME', 'database.db')
    db_connection = sqlite3.connect(database_file_name, check_same_thread=False)
    # To be discovered in the whole application
    app.config.from_mapping(
        DATABASE_CON = db_connection
    )
    
    # Routes
    @app.get('/todos')
    def get_all_todos():
        db_connection = app.config['DATABASE_CON']
        db_connection.row_factory = sqlite3.Row
        curseur = db_connection.cursor()
        curseur.execute(
            "SELECT * FROM todos"
        )
        data = curseur.fetchall()
        return(jsonify(
            [
                {
                    "id": element['id'],
                    "name": element['name'],
                    "status": element['status']    
                } for element in data
            ])
        )
    
    
    @app.post('/todos')
    def create_todo():
        """ 
            POST /todos JSON
            {
                "name": string
            }
        """
        request_body = request.get_json()
        name = request_body['name']
        # Persist in the database
        db_connection = app.config["DATABASE_CON"]
        curseur = db_connection.cursor()
        curseur.execute(
            "INSERT INTO todos(name,status) VALUES (?,?)",
            (name, 0)
        )
        db_connection.commit()
        # Get the todo id added by the last curseur 
        todo_id = curseur.lastrowid
        db_connection.row_factory = sqlite3.Row
        
        curseur = db_connection.cursor()
        curseur.execute(
            "SELECT * FROM todos WHERE id = ?",
            # Tuple with one element
            (todo_id,)
        )
        
        data = curseur.fetchone()
        return(dict(data),201)    

    @app.delete('/todos/<string:id>')
    def delete_user(id):
        db_connection = app.config["DATABASE_CON"]
        curseur = db_connection.cursor()
        curseur.execute('DELETE FROM todos where id = ?', (id,))
        if curseur.rowcount == 0:
            return {
                "message": "Todo not deleted successfully"
            }
        elif curseur.rowcount == 1:
            return {
                "message": "Todo deleted successfully"
            }    
    return app

# # Entry point
# if __name__ == "__main__":
#     app = create_app(__name__)
#     app.run()