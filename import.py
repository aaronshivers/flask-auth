import pandas
import sqlite3

csv = 'books.csv'
cnx = sqlite3.connect('project/db.sqlite')
df = pandas.read_csv(csv)
df.to_sql('books', cnx)
# print(df)