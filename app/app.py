from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
import time

app = Flask(__name__)

# db_config = {
#     'user': 'root',
#     'password': '123456789',
#     'host': 'localhost',
#     'database': 'todo_db'
# }

# def get_db_connection():
#     connection = mysql.connector.connect(**db_config)
#     return connection

def get_db_connection():
    db_config = {
        'user': 'root',
        'password': '123456789',
        'host': 'todo-db',
        'database': 'todo_db'
    }
    connection = None
    for _ in range(10):
        try:
            connection = mysql.connector.connect(**db_config)
            if connection.is_connected():
                print("Successfully connected to the database")
                break
        except Error as e:
            print(f"Error: {e}")
            time.sleep(5)
    if not connection or not connection.is_connected():
        raise Exception("Failed to connect to the database")
    return connection


@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM todo')
    todos = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    description = request.form.get('description')
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO todo (title, description, completed) VALUES (%s, %s, %s)', (title, description, False))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('index'))

@app.route('/update/<int:todo_id>')
def update_todo(todo_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT completed FROM todo WHERE id = %s', (todo_id,))
    result = cursor.fetchone()
    if result:
        completed = not result['completed']
        cursor.execute('UPDATE todo SET completed = %s WHERE id = %s', (completed, todo_id))
        connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM todo WHERE id = %s', (todo_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
