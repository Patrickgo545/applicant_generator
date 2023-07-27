import os
import openai
import query_components
import pyodbc

# CHAT GPT
openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages= [
    {
      "role": "system",
      "content": str(query_components.complete_query)
    },
  ],
  temperature=0,
  max_tokens=1024
)

# SQL DATABASE
server = 'LAPTOP-T37NP786' # (SQL) SELECT @@ServerName
database = 'api_test'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    # Establish the connection
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Example: Execute a query
    cursor.execute('SELECT TOP 5 * FROM dbo.api_test_table')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the connection
    connection.close()

except pyodbc.Error as ex:
    print('Error:', ex)
    print('Error code:', ex.args[0])
    print('Error message:', ex.args[1])



'''query_qty = 5

while query_qty > 0:
    print('.')
    query_qty -= 1'''