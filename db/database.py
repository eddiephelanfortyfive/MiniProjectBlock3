import sqlite3

# Connect to the database
con = sqlite3.connect("ClubHub.db")
cur = con.cursor()

# Create the users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username VARCHAR(30) UNIQUE,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    password VARCHAR(30),
    email VARCHAR(255) UNIQUE,
    is_student BOOLEAN,  
    is_coordinator BOOLEAN,
    is_admin BOOLEAN
)
""")

# Insert a sample user
#sample_user = ('john_doe', 'John', 'Doe', 'password123', 'john@example.com', 1, 0, 0)
#cur.execute("""
#INSERT INTO users (username, first_name, last_name, password, email, is_student, is_coordinator, is_admin)
#VALUES ('markSmith', 'mark', 'Smith', 'padwoord', 'email@gmail.com', 1, 0, 1)
#""")


# Commit the transaction
con.commit()

# Fetch and print all users from the table
cur.execute("SELECT * FROM users")
users = cur.fetchall()
for user in users:
    print(user)

# Close the connection
con.close()
