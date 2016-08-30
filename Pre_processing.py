import pandas as pd
import matplotlib.pyplot as plt
import plotly.plotly as py
import math
data = pd.read_csv('train.csv',index_col=0)
data['AUCP']=data.AUCP.apply(int)
data['Category'] = data['Category'].astype('category')
data.Category=data.Category.cat.codes
data.Docdt=pd.to_datetime(data['Docdt'])
data['Purchase_Year'] =data['Docdt'].dt.year
data['Purchase_Month']=data['Docdt'].dt.month
data['Type']=data['Type'].fillna('No Lens')
data['Type'] = data['Type'].astype('category')
data.Type=data.Type.cat.codes
data['Store_Type'] = data['Store_Type'].astype('category')
data.Store_Type=data.Store_Type.cat.codes
data['City'] = data['City'].astype('category')
data.City=data.City.cat.codes
data['Store'] = data['Store'].astype('category')
data.Store=data.Store.cat.codes
data['Dummy']=data['Store_open_date']
data['Dummy']=data.Dummy.str.replace(r'\([^~,][^~,]*', '')
data['Dummy']=data.Dummy.str.replace('31st May \'13', '31-05-13')
data['Dummy']=data.Dummy.str.replace('28th Oct \'09', '28-Oct-09')
data['Dummy']=data.Dummy.str.replace('12th May 2010 ', '12-05-10')
data.Dummy=pd.to_datetime(data['Dummy'])
data['Store_Year'] =data['Dummy'].dt.year
data.Store_Year.isnull().sum()
counts = data.groupby('Store_Year').size();
data['Store_Year']=data['Store_Year'].fillna(2011)
data['Store_Year']=data['Store_Year'].astype('int')
counts = data.groupby('AGE_F').size(); counts