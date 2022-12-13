#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df= pd.read_csv(r"C:\Users\Admin\Downloads\Biodiversity_by_County_-_Distribution_of_Animals__Plants_and_Natural_Communities.csv")


# In[3]:


df


# In[4]:


bio=df.loc[:,["County","Category","Taxonomic Group","Distribution Status"]]
bio


# In[5]:


bio.shape


# In[6]:


bio.isnull().sum()


# In[7]:


bio.describe()


# In[8]:


bio.County.unique()


# In[9]:


bio.drop(bio.loc[bio['County']=='Bronx'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Atlantic Ocean and Long Island Sound'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Counties Unknown'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Lake Erie Open Waters'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Lake Ontario Open Waters'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='New York'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Queens'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Richmond'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Kings'].index, inplace=True)


# In[10]:


bio.describe()


# In[11]:


bio.shape


# In[12]:


bio.rename(columns = {'Taxonomic Group':'Taxonomic_Group', 'Distribution Status': 'Distribution_Status'}, inplace = True)


# In[13]:


bio.Taxonomic_Group.unique()


# In[14]:


bio.Distribution_Status.unique()


# In[15]:


bio.info()


# ## Using Farmland class Dataset
# 

# In[16]:


df2= pd.read_csv(r"C:\Users\Admin\Downloads\farmclass.csv")


# In[17]:


df2


# In[18]:


df2.rename(columns = {'Area\nSymbol':'Area_symbol', 'Area Name':'County','Map Unit\nSymbol':'Map_unit_symbol','Map Unit Name': 'Map_unit_name','Farmland Class':'Farmland_Class','Map Unit\nAcres': 'unit_Acres'}, inplace = True)


# In[19]:


df2


# In[20]:


df2.describe()


# In[21]:


df2.County.unique()


# In[22]:


df2.Farmland_Class.unique()


# In[23]:


df2['County'].value_counts()


# In[24]:


df2.dtypes


# In[25]:


df2.set_index('County', inplace=True)


# In[26]:


# changing index cols with rename()
df2.rename(index = {"Albany County, New York":"Albany", "Allegany County Area, New York":"Allegany",
       "Broome County, New York":"Broome", "Cattaraugus County, New York":"Cattaraugus",
       "Cayuga County, New York":"Cayuga", "Chautauqua County, New York":"Chautauqua",
       "Chemung County, New York":"Chemung", "Chenango County, New York":"Chenango",
       "Clinton County, New York":"Clinton", "Columbia County, New York":"Columbia",
       "Cortland County, New York":"Cortland", "Delaware County, New York":"Delaware",
       "Dutchess County, New York":"Dutchess", "Erie County, New York":"Erie",
       "Essex County, New York":"Essex",
       "Franklin County, New York, Northern Part":"Franklin",
       "Fulton County, New York":"Fulton", "Genesee County, New York":"Genesee",
       "Greene County, New York":"Greene", "Hamilton County, New York":"Hamilton",
       "Herkimer County, New York, Southern Part":"Herkmier",
       "Jefferson County, New York":"Jefferson",
       "Lewis County, New York, Middle Part":"Lewis",
       "Livingston County, New York":"Livingston", "Madison County, New York":"Madison",
        "Monroe County, New York":"Monroe",
       "Montgomery County, New York":"Montgomery", "Nassau County, New York":"Nassau",
       "Niagara County Area, New York":"Niagara", "Oneida County, New York":"Oneida",
       "Onondaga County, New York":"Onondaga", "Ontario County, New York":"Ontario",
       "Orange County, New York":"Orange", "Orleans County, New York":"Orleans",
       "Oswego County, New York":"Oswego", "Otsego County, New York":"Ostego",
       "Putnam County, New York":"Putnam", "Rensselaer County, New York":"Rensselaer",
       "Rockland County, New York":"Rockland", "Saratoga County, New York":"Saratoga",
       "Schenectady County, New York":"Schenectady", "Schoharie County, New York":"Schoharie",
       "Schuyler County, New York":"Schuyler", "Seneca County, New York":"Seneca",
       
       "St. Lawrence County, New York":"St. Lawrence", "Steuben County, New York":"Steuben",
       "Suffolk County, New York":"suffolk", "Sullivan County, New York":"Sullivan",
       "Tioga County, New York":"Tioga", "Tompkins County, New York":"Tompkins",
       "Ulster County, New York":"Ulster", "Warren County, New York":"Warren",
       "Washington County, New York":"Washington", "Wayne County, New York":"Wayne",
       "Westchester County, New York":"Westchester", "Wyoming County, New York":"Wyoming",
       "Yates County, New York":"Yates"},
                                 inplace = True)
# display
df2


# In[27]:


df2.reset_index('County',inplace=True)


# In[28]:


df2.drop(df2.loc[df2['County']=='Akwesasne Territory: St. Regis Mohawk Reservation'].index, inplace=True)
df2.drop(df2.loc[df2['County']=='Area Name'].index, inplace=True)
df2.drop(df2.loc[df2['County']=='Seneca Nation of Indians, New York'].index, inplace=True)


# In[29]:


df2.describe()


# # Merging Datasets using pd.merge method
# 

# In[30]:


final=pd.merge(bio,df2,how='inner',on='County')

final


# In[31]:


final.describe()


# In[32]:


final


# In[33]:


group=final.loc[:,["County","unit_Acres"]]
group


# In[34]:


group.dtypes


# In[35]:


group.set_index('County', inplace=True)


# In[36]:


group


# In[37]:


group.astype(float).sum()


# In[38]:


group.groupby('unit_Acres').max()


# In[39]:


df_final=final.groupby(['County', 'unit_Acres'])['Farmland_Class'].agg('sum')


# In[40]:


df_final.head(50)


# In[ ]:




