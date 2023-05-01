import pyodbc

# Define the connection string
server = 'cc-8995ffe3-66b777c5b6-S4gqx'
database = 'DeepCoffeeDB'
username = 'djhousman@stcloudstate.edu'
password = 'Theick@247'
driver= '{ODBC Driver 18 for SQL Server}'
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Create a connection object
cnxn = pyodbc.connect(conn_str)

# Create a cursor object
cursor = cnxn.cursor()

# Execute a query
cursor.execute('SELECT * FROM your_table_name')

# Fetch the results
rows = cursor.fetchall()

# Process the results
for row in rows:
    print(row)
