import pandas as pd
import pyodbc
from sqlalchemy import create_engine

# Параметры подключения
server = 'EANTONOVA-MBL'
database = 'AdventureWorksDW2017'

# Строка подключения
connection_string = f'mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

# Подключение к базе данных
engine = create_engine(connection_string)

# order_items load
order_items = pd.read_csv('/Homework lesson 23/order_items.csv')
order_items.to_sql('Order_items', con=engine, if_exists='append', index=False)

# orders load
orders = pd.read_csv('/Homework lesson 23/orders.csv')
orders.to_sql('Orders', con=engine, if_exists='append', index=False)

# categories load
categories = pd.read_csv('/Homework lesson 23/categories.csv')
categories.to_sql('Categories', con=engine, if_exists='append', index=False)

# products load
products = pd.read_csv('/Homework lesson 23/products.csv')
products.to_sql('Products', con=engine, if_exists='append', index=False)