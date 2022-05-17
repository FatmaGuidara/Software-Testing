import sqlite3
import os

def create_db(database_filename):
    # Connect to SQLite
    connexion = sqlite3.connect(database_filename)
    
    # Create a Connection
    curseur = connexion.cursor()
    
    # Drop todos table if already exists
    curseur.execute("DROP TABLE IF EXISTS todos")
    
    # Create todos table
    sql = '''
        CREATE TABLE "todos" (
            "id"        INTEGER PRIMARY KEY AUTOINCREMENT,
            "name"      TEXT,
            "status"    INTEGER
        )
    '''
    curseur.execute(sql)
    
    # Commit changes
    connexion.commit()
    
if __name__ == '__main__':
    database_file_name = os.environ.get('DATABASE_FILENAME', 'todos.db')
    create_db(database_file_name) 