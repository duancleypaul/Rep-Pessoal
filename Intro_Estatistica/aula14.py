import plotly.express as px
import pandas as pd

'''
url = "https://raw.githubusercontent.com/advinstai/python-datascience/master/csv/gpa.csv"
df1 = pd.read_table(url,sep=" ")  

fig = px.histogram(df1, x = 'verb_SAT')
print(type(fig))
fig.show()
'''
url = "https://raw.githubusercontent.com/advinstai/python-datascience/master/csv/diabetic_data.csv"
df2 = pd.read_table(url,sep=",",na_values="?")
df2 = df2[:1000]
print(df2)
#fig = px.bar(df2, x="race")
#fig.show()

###
'''
fig = px.histogram(colldata, x="Apps")
print(type(fig))
fig.show()
'''