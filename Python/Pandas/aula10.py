import pandas as pd
import numpy as np

#+---------------+
#| USANDO SERIES |
#+---------------+

s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])

print(s)
print("---")

s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
              index = ['A','Z','C','Y','W'])

print(s)
print("---")

d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
cities = pd.Series(d)
print(cities)
print("---")

print(cities[cities<=1000])
print("---")

less_than_1000 = cities <= 1000

print(less_than_1000)
print("\n")
print(cities[less_than_1000])
print("---")

newcities = cities		# eh uma referencia, nao eh uma copia!!!!.
# Ex:
print(newcities)
print("")
print(cities)
print("")

newcities[0] = 1500

print(newcities)
print("")
print(cities)
print("---")

#+-------------------+
#| USANDO DATAFRAMES |
#+-------------------+

# from_csv = pd.read_csv()
# print(from_csv)




#--- .loc[] .iloc[] .ix[]:


