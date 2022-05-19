import matplotlib
import numpy as np
import matplotlib.pyplot as plt


import get_data

print("HI")

# print(get_data.GetData().get_data())
data = get_data.GetData().get_data()
for d in data: 
    if d.Age >0: 
        d.Name
list = ["yes" if d.Age > 0 else "no"+d.Name for d in data]
#print(list)

print("data:")
print(data)
input()



# make graph using matplotlib
# plt.plot([d.PassengerId for d in data])
plt.plot([d.Sex for d in data if d.Survived])
fig, ax = plt.subplots()
def sor_func(data: get_data.TitanicType):
    return data.Age

data.sort(key=sor_func)
mData = [d.Age for d in data if d.Sex == "male"]
mData2 = [d.Embarked for d in data if d.Sex == "male"]
fData = [d.Age for d in data if d.Sex == "female"]
fData2 = [d.Embarked for d in data if d.Sex == "female"]
ax.bar(x= mData2 , height=mData, label='Men')
ax.bar(x=fData2, height=fData, label='Female')
plt.legend()
plt.show()

print(data.__len__())

