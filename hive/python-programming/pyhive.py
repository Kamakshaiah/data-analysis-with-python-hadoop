from pyhive import hive
import pandas as pd

#Create Hive connection 
conn = hive.Connection(host="localhost", port=10000)

# Read Hive table and Create pandas dataframe
df = pd.read_sql("show databases;", conn)
print(df)

