import pyodbc
import insert_test

# Replace the following variables with your SQL Server connection details
server = 'LAPTOP-T37NP786' # (SQL) SELECT @@ServerName
database = 'api_test'

# Create the connection string
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

# INSERT
try:
    # Establish the connection
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # SQL command to insert data
    sql_command = insert_test.sql_command

    # Execute the SQL command
    cursor.execute(sql_command)
    connection.commit()

    # Close the connection
    connection.close()

    print("Data inserted successfully!")

except pyodbc.Error as ex:
    print('Error:', ex)
    print('Error code:', ex.args[0])
    print('Error message:', ex.args[1])

# Query
try:
    # Establish the connection
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Example: Execute a query
    cursor.execute('SELECT * FROM dbo.api_test_table')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the connection
    connection.close()

except pyodbc.Error as ex:
    print('Error:', ex)
    print('Error code:', ex.args[0])
    print('Error message:', ex.args[1])

