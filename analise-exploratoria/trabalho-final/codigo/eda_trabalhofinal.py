#!/usr/bin/env python
# coding: utf-8

# ## **Trabalho final: Análise Exploratória de Dados**
# 
# Grupo: Bianca Muniz, Meyrele Torres e Ricardo Grimbaun

# ## **Análise exploratória univariada**
# Variável escolhida: `idade`

# In[ ]:


# Importando as bibliotecas
import pandas as pd #para abrir e manipular as bases
import statistics #para o cálculo da moda
get_ipython().system('pip install altair #instalando a biblioteca altair')
import altair as alt #para as visualizações gráficas


# In[2]:


alt.data_transformers.disable_max_rows()


# In[3]:


# Carregando a base de dados
dados = pd.read_csv(r'https://raw.githubusercontent.com/biamuniz/trabalhofinal_eda_mjda/main/dados/microdados.csv', sep=';')

# Visualizando a base de dados
dados


# In[4]:


# estatísticas descritivas da base
print(dados.describe())


# Note que a base a base tem dados tem aproximadamente 270 mil observações, mas este valor não é compatível com o número de registros de `altura`, de `peso` e de `idade`. Logo, isso mostra a presença de missing data.
# 
# Olhando a base, podemos ver que há nomes que se repetem na coluna nome_atleta, pois um mesmo atleta pode participar de diferentes modalidades de um mesmo esporte.
# 
# Para prosseguirmos com a análise, limpamos a base com a finalidade de ter um registro por atleta em cada edição dos jogos, excluindo dessa maneira as colunas medalha e evento. Em seguida, removemos os valores duplicados. A base ficou com 189765 registros únicos.

# In[5]:


dados_analise = dados.drop('evento', 1) # criando o dataframe 'analise_idade', que é uma cópia do 'df', sem a coluna 'evento'
dados_analise = dados_analise.drop('medalha', 1) # excluindo a coluna 'medalha' e sobrescrevendo o dataframe 'analise_idade'
dados_analise = dados_analise.drop_duplicates() # removendo valores duplicados


# In[6]:


dados_analise


# In[7]:


dados_analise.select_dtypes(include=['number']) #incluindo um NaN nos dados ausentes


# In[8]:


# Análise descritiva da variável idade
dados_analise['idade'].describe()


# In[9]:


#calculando a moda
statistics.mode(dados_analise['idade'])


# In[10]:


# Gráfico: Frequência de idade
chart1 = alt.Chart(dados_analise).mark_bar(color='firebrick').encode(
  x='idade',
  y='count(idade)',
)
chart1


# **Variável escolhida: `esporte = atletismo`**

# In[11]:


#Limpeza da base: queremos registros únicos de cada participante por edição e esporte
dados_esporte = dados.drop('evento', 1) # criando o dataframe 'dados_esporte', que é uma cópia de 'dados', sem a coluna 'evento'
dados_esporte = dados_esporte.drop('medalha', 1) # excluindo a coluna 'medalha' e sobrescrevendo o dataframe 'dados_esporte'
dados_esporte = dados_esporte.drop_duplicates() # removendo valores duplicados


# In[12]:


atletismo = dados_esporte.loc[dados_esporte['esporte'] == 'Athletics']
atletismo


# In[13]:


# Estatísticas sobre os participantes que competem no atletismo
atletismo.describe()


# In[14]:


# contagem de atletas por esporte
chart2 = alt.Chart(dados_esporte).mark_bar(color='green').encode(
  x='esporte',
  y='count(id_atleta)',
)
chart2


# ## **Análise exploratória bivariada**

# **Variáveis escolhidas: `idade` e `sexo`**

# In[15]:


# Estatísticas de idade para o sexo feminino
feminino = dados_analise["idade"].loc[dados_analise['sexo'] == 'F']
feminino.describe()


# In[16]:


# Qual a idade mais frequente entre competidores do sexo feminino nos jogos olímpicos?
statistics.mode(dados_analise['idade'].loc[dados_analise['sexo'] == 'F'])


# In[17]:


# Estatísticas para o sexo masculino
masculino = dados_analise["idade"].loc[dados_analise['sexo'] == 'M']
masculino.describe()


# In[18]:


# Qual a idade mais frequente entre competidores do sexo masculino nos jogos olímpicos?
statistics.mode(dados_analise['idade'].loc[dados_analise['sexo'] == 'M'])


# In[20]:


# criando a tabela "estatistica_idade_sexo", a partir de uma tabela dinâmica, comparando os resultados para os dois sexos
unused_columns = dados_analise.columns.difference(set(['sexo']).union(set([])).union(set({'idade'})))
tmp_df = dados_analise.drop(unused_columns, axis=1)
tab_dinamica_b = tmp_df.pivot_table(
    index=['sexo'],
    values=['idade'],
  aggfunc={'idade': ['mean', 'median', 'min', 'max', 'count']}) #media, mediana, valor mínimo e máximo para cada sexo
estatistica_idade_sexo = tab_dinamica_b.reset_index()
estatistica_idade_sexo # visualizando o resultado


# In[21]:


chart3 = alt.Chart(dados_analise).mark_bar().encode(
    x=alt.X('sexo', axis=alt.Axis(title='sexo')),
    y=alt.Y('mean(idade)',
        axis=alt.Axis(title='idade')
    ),
    color=alt.Color('sexo:N')
)
chart3


# In[22]:


unused_columns = dados_analise.columns.difference(set(['ano']).union(set(['sexo'])).union(set({'id_atleta'})))
tabela = dados_analise.drop(unused_columns, axis=1)
pivot_table = tabela.pivot_table(
    index=['ano'],
    columns=['sexo'],
    values=['id_atleta'],
    aggfunc={'id_atleta': ['count']}
)
participacao = pivot_table.reset_index()
participacao


# In[23]:


# Gráfico: Participação nas Olimpíadas de acordo com o sexo
chart4 = alt.Chart(dados_analise).mark_bar().encode(
    x='ano',
    y='count(id_atleta)',
    color=alt.Color('sexo:N', scale=alt.Scale(range=["orange","green"]))
)
chart4 ### espaços em branco no gráfico = dados ausentes


# In[24]:


# normalizando os dados
chart4.mark_bar().encode(
    x='ano',
    y=alt.Y('count(id_atleta)', stack='normalize'),
    opacity=alt.value(0.7)
)


# **Variáveis escolhidas: `idade`, `peso`, `altura` e `medalha = ouro`**

# In[25]:


medalha_ouro = dados.loc[dados['medalha']=='Gold']


# In[26]:


medalha_ouro = medalha_ouro.drop('evento', 1)
medalha_ouro = medalha_ouro.drop_duplicates() # removendo valores duplicados


# In[27]:


medalha_ouro


# In[28]:


medalha_ouro.describe() # estatísticas descritivas sobre os medalhistas de ouro


# In[29]:


statistics.mode(medalha_ouro['idade'])


# In[30]:


statistics.mode(medalha_ouro['peso'])


# In[31]:


statistics.mode(medalha_ouro['altura'])

