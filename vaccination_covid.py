#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.chdir('C:\\Users\\steno\\OneDrive\\Desktop\\Blossom\\vaccination')


# In[2]:


import pandas as pd

df = pd.read_csv('2021-03-22-prise-rdv-national.csv')
df


# In[3]:


vaccination_1 = df[df['rang_vaccinal'] == 1]
vaccination_2 = df[df['rang_vaccinal'] == 2]


# In[4]:


import plotly.express as px

fig = px.bar(vaccination_1, x='date_debut_semaine', y="nb", labels = {'date_debut_semaine':'Date du début de la semaine', 'nb': 'Nombre de rendez-vous'}, title = 'Nombre de rendez-vous pris en France pour une première injection de vaccin')
fig.show()


# In[5]:


import plotly.express as px

fig = px.bar(vaccination_2, x='date_debut_semaine', y="nb", labels = {'date_debut_semaine':'Date du début de la semaine', 'nb': 'Nombre de rendez-vous'}, title = 'Nombre de rendez-vous pris en France pour une seconde injection de vaccin')
fig.show()


# In[6]:


df_region = pd.read_csv('2021-03-22-prise-rdv-par-reg.csv')
df_region_rdv_1 = df_region[df_region['rang_vaccinal'] == 1]
df_region_rdv_2 = df_region[df_region['rang_vaccinal'] == 2]


# In[7]:


fig = px.bar(df_region_rdv_1, x='date_debut_semaine', y='nb', color = 'region', labels = {'date_debut_semaine':'Date du début de la semaine', 'nb': 'Nombre de rendez-vous', 'region': 'Région'}, title = 'Nombre de rendez-vous pris pour une première injection de vaccin par Région')
fig.show()


# In[8]:


fig = px.bar(df_region_rdv_2, x='date_debut_semaine', y='nb', color = 'region', labels = {'date_debut_semaine':'Date du début de la semaine', 'nb': 'Nombre de rendez-vous', 'region': 'Région'}, title = 'Nombre de rendez-vous pris pour une seconde injection de vaccin par Région')
fig.show()


# In[18]:


df_livraisons = pd.read_csv('flux-total-reg.csv')
cleaner1 = df_livraisons.loc[(df_livraisons['date_fin_semaine'] < '2021-04-19') & (df_livraisons['date_fin_semaine'] > '2021-01-17')].reset_index()
total_livraisons = cleaner1.groupby(['date_fin_semaine','type_de_vaccin']).sum().reset_index()


# In[19]:


fig = px.bar(total_livraisons, x='date_fin_semaine', y='nb_doses', color = 'type_de_vaccin', labels = {'nb_doses':'Nombre de doses', 'date_fin_semaine': 'Date de la fin de semaine', 'type_de_vaccin': 'Fournisseur'},title = 'Livraisons réalisées et prévisionnelles des doses de vaccin Covid-19 en France métropolitaine et DROM')
fig.show()


# In[ ]:




