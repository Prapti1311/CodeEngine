import pyodbc

odbc_driver = "ODBC Driver 18 for SQL Server" 
server = "tcp:masher.database.windows.net"
database = "toy_data"
username = "poco"
password = "3Gnsakhjewpiewjckewnckewn"

# Construct the ODBC connection string
connection_string = f"DRIVER={odbc_driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Establish the ODBC connection
connection = pyodbc.connect(connection_string)

# Create a cursor
cursor = connection.cursor()

# Execute SQL queries or commands
cursor.execute("SELECT * FROM invoices")
result = cursor.fetchall()
print(result)

# Close the cursor and connection
cursor.close()
connection.close()
