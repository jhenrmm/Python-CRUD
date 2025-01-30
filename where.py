import sqlite3
import uuid

# Step 1: Connect to the SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()


def create_user(name, email):
    user_id = str(uuid.uuid4())  # Convert UUID to string
    try:
        cursor.execute(
            'INSERT INTO users (id_, name, email) VALUES (?, ?, ?)', (user_id, name, email))
        conn.commit()
        print(f"User {name} added successfully with ID {user_id}!")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")


def get_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(user)


def select_user(user_id):
    cursor.execute('SELECT * FROM users WHERE id_ = ?', (user_id,))
    user = cursor.fetchone()  # Fetch one matching record

    if user:
        return user  # Return the tuple containing user details
    return "User not found."


# Example usage
user_data = select_user('2788aa42-bcbe-46c5-9703-b2d77dfd8524')
print(user_data)  # This will print the tuple (id_, name, email) if found
