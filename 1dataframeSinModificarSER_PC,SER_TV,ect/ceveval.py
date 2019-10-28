#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


csv_original = 'ceneval.csv'
ceneval = pd.read_csv(csv_original, encoding='latin-1', low_memory=False)


# In[3]:


ceneval


# In[4]:


pd.value_counts(ceneval['DICTAMEN'])


# In[5]:


100 * ceneval['DICTAMEN'].value_counts() / len(ceneval['DICTAMEN'])


# In[6]:


plot = ceneval['DICTAMEN'].value_counts().plot(kind='bar', title='Testimonio')


# In[7]:


plot = ceneval['DICTAMEN'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),
                                            title='Testimonio')


# In[8]:


pd.value_counts(ceneval['TIPO_EXA'])


# In[9]:


plot = ceneval['TIPO_EXA'].value_counts().plot(kind='bar', title='Testimonio')


# In[10]:


# Tabla 
pd.crosstab(index=ceneval['TIPO_EXA'], columns=ceneval['DICTAMEN'], margins=True)


# In[11]:


# tabla de contingencia en porcentajes relativos segun sobreviviente
pd.crosstab(index=ceneval['TIPO_EXA'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[12]:


plot = pd.crosstab(index=ceneval['TIPO_EXA'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,
                                              axis=1).plot(kind='bar')


# In[13]:


# Tabla 
pd.crosstab(index=ceneval['PLT_PROC'], columns=ceneval['DICTAMEN'], margins=True)


# In[14]:


# tabla de contingencia en porcentajes relativos segun sobreviviente
pd.crosstab(index=ceneval['PLT_PROC'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[15]:


# Tabla 
pd.crosstab(index=ceneval['PRO_LIC'], columns=ceneval['DICTAMEN'], margins=True)


# In[16]:


pd.crosstab(index=ceneval['TIPO_EXA'], columns=ceneval['PRO_LIC'], margins=True)


# In[17]:


pd.crosstab(index=ceneval['TIEM_TRAB'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[18]:


pd.crosstab(index=ceneval['SER_PC'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[19]:


pd.crosstab(index=ceneval['SER_INTE'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[20]:


pd.crosstab(index=ceneval['SER_AUTO'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[21]:


pd.crosstab(index=ceneval['CPV_CASA'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[22]:


pd.crosstab(index=ceneval['NIV_EDU'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[23]:


pd.crosstab(index=ceneval['BECA_DAC'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[24]:


pd.crosstab(index=ceneval['BECA_NEC'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[25]:


pd.crosstab(index=ceneval['SIT_LAB'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[26]:


ceneval.dtypes


# In[27]:


ceneval['FECHA_APLI']=pd.to_datetime(ceneval['FECHA_APLI'])#se esta sobrescribiendo y cambiando el tipo de dato


# In[28]:


exams_before = {}
exams_before_values = []
for i, row in ceneval.sort_values(['FECHA_APLI'],ascending=True).iterrows(): 
    matricula = row["MATRICULA"]
    exams_before[matricula] = 1  + exams_before.get(matricula, 0)
    exams_before_values.append(exams_before[matricula] - 1)
    
ceneval["VECES_EXAM"] = exams_before_values


# In[29]:


ceneval["VECES_EXAM"].unique()


# In[30]:


len(ceneval.query("VECES_EXAM > 1"))


# In[31]:


ceneval.query("VECES_EXAM > 1")["FOLIO"]


# In[32]:


pd.crosstab(index=ceneval['VECES_EXAM'], columns=ceneval['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[33]:


categorias = [0, 1]


# In[34]:


df=ceneval


# In[35]:


df.DICTAMEN = df.DICTAMEN.replace({'AòN NO SATISFACTORIO': 0})
df.DICTAMEN = df.DICTAMEN.replace({'SOBRESALIENTE': 1})
df.DICTAMEN = df.DICTAMEN.replace({'SATISFACTORIO': 1})


# In[36]:


df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE ARTE, ARQUITECTURA Y DISEO.': 0})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE CIENCIAS BIOLîGICAS Y AGROPECUARIAS': 1})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE CIENCIAS DE LA SALUD': 2})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE CIENCIAS ECONîMICO-ADMINISTRATIVAS': 3})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE CIENCIAS EXACTAS E INGENIERêAS': 4})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE CIENCIAS SOCIALES Y HUMANIDADES': 5})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE LA CINEGA': 6})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE LA COSTA': 7})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE LA COSTA SUR': 8})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE LOS ALTOS': 9})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE LOS LAGOS': 10})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE LOS VALLES': 11})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DE TONALç': 12})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DEL NORTE': 13})
df.PLT_PROC = df.PLT_PROC.replace({'CENTRO UNIVERSITARIO DEL SUR': 14})
df.PLT_PROC = df.PLT_PROC.replace({'SISTEMA DE UNIVERSIDAD VIRTUAL': 15})


# In[37]:


df.ANO_NAC = 2019-df.ANO_NAC


# In[38]:


for i in range(10):
    v=9+(i*0.1)
    df.PRO_LIC = df.PRO_LIC.replace({v: 9})
for i in range(10):
    v=8+(i*0.1)
    df.PRO_LIC = df.PRO_LIC.replace({v: 8})
for i in range(10):
    v=7+(i*0.1)
    df.PRO_LIC = df.PRO_LIC.replace({v: 7})
for i in range(10):
    v=6+(i*0.1)
    df.PRO_LIC = df.PRO_LIC.replace({v: 6})


# In[39]:


df.SEXO = df.SEXO.replace({1: 0})


# In[40]:


df.SEXO = df.SEXO.replace({2: 1})


# In[41]:


df.LENG_MA = df.LENG_MA.replace({2: 0})
df.LENG_PA = df.LENG_PA.replace({2: 0})


# In[42]:


df.RAZ_RAPT = df.RAZ_RAPT.replace({2: 0})
df.RAZ_RACT = df.RAZ_RACT.replace({2: 0})
df.RAZ_OPT = df.RAZ_OPT.replace({2: 0})
df.RAZ_PCUM = df.RAZ_PCUM.replace({2: 0})
df.RAZ_CMNF = df.RAZ_CMNF.replace({2: 0})
df.REG_PROC = df.REG_PROC.replace({2: 0})


# In[43]:


df.SER_TELE = df.SER_TELE.replace({2: 0})
df.SER_LAV = df.SER_LAV.replace({2: 0})
df.SER_REF = df.SER_REF.replace({2: 0})
df.SER_HOR = df.SER_HOR.replace({2: 0})
df.SER_INTE = df.SER_INTE.replace({2: 0})
df.SER_TVP = df.SER_TVP.replace({2: 0})
df.SER_TABL = df.SER_TABL.replace({2: 0})


# In[44]:


df.dropna()


# In[45]:


pd.crosstab(index=df['PRO_LIC'], columns=df['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[46]:


df = df.drop(df[df['PRO_LIC']==0.0].index)


# In[47]:


pd.crosstab(index=df['PRO_LIC'], columns=df['DICTAMEN']).apply(lambda r: r/r.sum() *100,axis=1)


# In[48]:


df.drop(['APLI', 'NEMOTECNIA', 'DESC_MNEMO', 'IDENTIFICA', 'DESC_IDENT', 'CVE_SEDE',
         'NOM_SEDE', 'CIU_SEDE', 'EDO_SEDE', 'TIPO_SEDE', 'ID_INSTITU', 'ID_CAMPUS',
         'ID_FACULTA', 'PERFIL', 'Duplicados', 'DIA_NAC', 'MES_NAC', 'NOM_PROC', 
          'CIU_PROC', 'EDO_PROC', 'CVE_PROC', 'P1', 'A1', 'P2', 'A2', 'P3', 'A3', 
         'P4', 'A4', 'P5', 'A5', 'P6', 'A6'], axis = 1, inplace=True) 
print(df.head())


# In[49]:


df.FOPR_CLEX = df.FOPR_CLEX.replace({1: 0})
df.FOPR_AULA = df.FOPR_AULA.replace({1: 0})
df.FOPR_LATA = df.FOPR_LATA.replace({1: 0})
df.FOPR_BIBL = df.FOPR_BIBL.replace({1: 0})
df.FOPR_SACO = df.FOPR_SACO.replace({1: 0})
df.FOPR_CAFE = df.FOPR_CAFE.replace({1: 0})
df.FOPR_ESDE = df.FOPR_ESDE.replace({1: 0})
df.FOPR_SDTE = df.FOPR_SDTE.replace({1: 0})
df.FOPR_ACIN = df.FOPR_ACIN.replace({1: 0})
df.FOPR_ACEL = df.FOPR_ACEL.replace({1: 0})
df.FOPR_ABRE = df.FOPR_ABRE.replace({1: 0})
df.FOPR_BOTR = df.FOPR_BOTR.replace({1: 0})
df.FOPR_LIMP = df.FOPR_LIMP.replace({1: 0})


# In[50]:


df.FOPR_CLEX = df.FOPR_CLEX.replace({2: 1})
df.FOPR_CLEX = df.FOPR_CLEX.replace({3: 1})
df.FOPR_CLEX = df.FOPR_CLEX.replace({4: 1})


# In[51]:


df.FOPR_AULA = df.FOPR_AULA.replace({2: 1})
df.FOPR_AULA = df.FOPR_AULA.replace({3: 1})
df.FOPR_AULA = df.FOPR_AULA.replace({4: 1})


# In[52]:


df.FOPR_LATA = df.FOPR_LATA.replace({2: 1})
df.FOPR_LATA = df.FOPR_LATA.replace({3: 1})
df.FOPR_LATA = df.FOPR_LATA.replace({4: 1})


# In[53]:


df.FOPR_BIBL = df.FOPR_BIBL.replace({2: 1})
df.FOPR_BIBL = df.FOPR_BIBL.replace({3: 1})
df.FOPR_BIBL = df.FOPR_BIBL.replace({4: 1})


# In[54]:


df.FOPR_SACO = df.FOPR_SACO.replace({2: 1})
df.FOPR_SACO = df.FOPR_SACO.replace({3: 1})
df.FOPR_SACO = df.FOPR_SACO.replace({4: 1})


# In[55]:


df.FOPR_CAFE = df.FOPR_CAFE.replace({2: 1})
df.FOPR_CAFE = df.FOPR_CAFE.replace({3: 1})
df.FOPR_CAFE = df.FOPR_CAFE.replace({4: 1})


# In[56]:


df.FOPR_ESDE = df.FOPR_ESDE.replace({2: 1})
df.FOPR_ESDE = df.FOPR_ESDE.replace({3: 1})
df.FOPR_ESDE = df.FOPR_ESDE.replace({4: 1})


# In[57]:


df.FOPR_SDTE = df.FOPR_SDTE.replace({2: 1})
df.FOPR_SDTE = df.FOPR_SDTE.replace({3: 1})
df.FOPR_SDTE = df.FOPR_SDTE.replace({4: 1})


# In[58]:


df.FOPR_ACIN = df.FOPR_ACIN.replace({2: 1})
df.FOPR_ACIN = df.FOPR_ACIN.replace({3: 1})
df.FOPR_ACIN = df.FOPR_ACIN.replace({4: 1})


# In[59]:


df.FOPR_ACEL = df.FOPR_ACEL.replace({2: 1})
df.FOPR_ACEL = df.FOPR_ACEL.replace({3: 1})
df.FOPR_ACEL = df.FOPR_ACEL.replace({4: 1})


# In[60]:


df.FOPR_ABRE = df.FOPR_ABRE.replace({2: 1})
df.FOPR_ABRE = df.FOPR_ABRE.replace({3: 1})
df.FOPR_ABRE = df.FOPR_ABRE.replace({4: 1})


# In[61]:


df.FOPR_BOTR = df.FOPR_BOTR.replace({2: 1})
df.FOPR_BOTR = df.FOPR_BOTR.replace({3: 1})
df.FOPR_BOTR = df.FOPR_BOTR.replace({4: 1})


# In[62]:


df.FOPR_LIMP = df.FOPR_LIMP.replace({2: 1})
df.FOPR_LIMP = df.FOPR_LIMP.replace({3: 1})
df.FOPR_LIMP = df.FOPR_LIMP.replace({4: 1})


# In[65]:


df


# In[ ]:





# In[ ]:




