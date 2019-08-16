import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

df = pd.read_csv('FMEL_Dataset.csv')
engine = create_engine('mysql+mysqlconnector://root:PASSWORD@localhost:3306/Giraffe', echo=False)

df.to_sql(name='test2', con=engine, if_exists = 'append', index=False)

#This script translates CSV files into DF and then into a mysql databse

#Tailor line 6 to the database platform of your choice and the specific database

#have not tested for excel, just csv



