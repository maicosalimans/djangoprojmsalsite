import sqlite3

# Connect to the database file or create a new one if it does not exist
conn = sqlite3.connect("books.db")

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create a table named books with two columns: title and writer
cur.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, writer TEXT)")

# Define a function to insert a new book into the table
def add_book(title, writer):

# Use a parameterized query to avoid SQL injection
cur.execute("INSERT INTO books VALUES (?, ?)", (title, writer))

# Commit the changes to the database
conn.commit()

# Print a confirmation message
print(f"Added {title} by {writer} to the database")

# Test the function by adding some books
add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
add_book("The Lord of the Rings", "J.R.R. Tolkien")
add_book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")

# Close the connection to the database
conn.close()
