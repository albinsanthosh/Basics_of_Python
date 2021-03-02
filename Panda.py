# importing pandas package
import pandas as pd

df = { "Name": {"a":1, "b":2}, "age": {'a':2,'b': 3}}
# making data frame from csv file
dl = { "Name": {"c", "d"}, "age": [12, 13]}

"""
di = pd.DataFrame(df)
dh = pd.DataFrame(dl)
# ds = dh.append(di)
ds = pd.concat([di, dh], ignore_index=True)
ds = pd.concat([ds, dh], ignore_index=True)

ds.to_excel('hello.xlsx')
df["Name"].update({"z":3})
df['hello']={"a":9}
df['hello'].update({"a":10})
print(df['hello']["a"])
"""
for org in df:
    df[org].pop('a')

print(df)