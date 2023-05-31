from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create a connection to the SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a users table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (username TEXT PRIMARY KEY, password TEXT)''')

# Insert the initial users into the table
cursor.execute("INSERT OR IGNORE INTO users VALUES ('user1', 'password1')")
cursor.execute("INSERT OR IGNORE INTO users VALUES ('user2', 'password2')")
cursor.execute("INSERT OR IGNORE INTO users VALUES ('user3', 'password3')")

# Commit the changes and close the connection
conn.commit()
conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        result = cursor.fetchone()

        conn.close()

        if result and result[0] == password:
            return render_template('result.html', result='success')
        else:
            return render_template('result.html', result='failure')

    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        result = cursor.fetchone()

        if result:
            conn.close()
            return render_template('result.html', result='exists')

        cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return render_template('result.html', result='success')

    return render_template('signup.html')

if __name__ == '__main__':
    app.run()