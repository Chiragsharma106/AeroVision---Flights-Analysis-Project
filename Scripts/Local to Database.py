# Use this script to load data from Local to SQL

# In[1]:


import pandas as pd
import os
from sqlalchemy import create_engine


# In[2]:


pg_user = 'postgres'
pg_password = 'SQUAL#QUE'
pg_host = 'localhost'
pg_port = '5432'
pg_db = 'FlightProject'


# In[3]:


PostgresCar = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')


# In[4]:


folder = r"C:\Users\chira\Documents\All Files\PortFolio Dashboards💸\#3 FlightDashboard"


# In[5]:


for files in os.listdir(folder):
    if files.endswith('csv'):
        names = files.strip().replace(' ', 's').lower().replace('.csv', '').replace('data', '').replace('table', '')
        df = pd.read_csv(os.path.join(folder, files))
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)
        print("-"*50)
        print(f'{names} table loading')
        df.to_sql(names, con = PostgresCar, if_exists = 'replace', index = False)
        print('Done')
print("-"*50)
print('All Done')

