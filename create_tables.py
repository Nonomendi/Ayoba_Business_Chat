import sqlite3

# Define the path to your SQL file
sql_file_path = 'dumby_data.sql'

# Create a connection to the SQLite database
conn = sqlite3.connect('Ayoba.db')

# Create a cursor object
cursor = conn.cursor()

# Read the SQL file
with open(sql_file_path, 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL commands in the file
# Note: Split the script if it contains multiple statements
# SQLite executes statements separated by semicolons
for statement in sql_script.split(';'):
    statement = statement.strip()
    if statement:  # Avoid executing empty statements
        try:
            cur=cursor.execute(statement)
        except Exception as e:
            print(statement)
            print(e)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
