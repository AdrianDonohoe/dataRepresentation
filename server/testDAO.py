from statesDAO import StatesDAO

x = StatesDAO()

y = x .getAll()

print(y)

x.closeConnection()

x = StatesDAO()
values = (1,2,3.6,55.5,'AL')
x.update(values)



x.closeConnection()
