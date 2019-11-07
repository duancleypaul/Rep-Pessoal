import pandas as pd
import numpy as np

df1 = pd.DataFrame({'employee': ['Bob','Jake','Lisa','Sue'],
                     'group':    ['Accounting','Engineering','Engineering','HR']})
df2 = pd.DataFrame({'employee': ['Lisa','Bob','Jake','Sue'],
                     'hire_date':    [2004,2008,2012,2014]})
print(df1)
print("")
print(df2)
print("")

df3 = pd.merge(df1,df2)

print(df3)
print("-"*35)

df4 = pd.DataFrame({'group':      ['Accounting','Engineering','HR'],
                    'supervisor': ['Carly','Guido','Steve']})

print(df4)
print("")
print(pd.merge(df3,df4))
print("-"*35)

df5 = pd.DataFrame({'group':  ['Accounting','Accounting','Engineering','Engineering','HR','HR'],
                    'skills': ['math','spreadsheets','coding','linux','spreadsheets','organization']})

print(df5)
print("")
print(pd.merge(df1,df5))
print("-"*35)