"""
Notes:
workflow of sql querying with python/sqlalchemy:
- import packages and functions
- create db engine
- connect to the engine
- query the database
- save query results to a pandas DataFrame
- close the connection
"""

# Import necessary modules
from sqlalchemy import create_engine
import pandas as pd


# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute('SELECT * FROM ALBUM')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()


# Print head of DataFrame df
print(df.head())

# Save the table names to a list: table_names
#table_names = engine.table_names()

# Print the table names to the shell
#print(table_names)

