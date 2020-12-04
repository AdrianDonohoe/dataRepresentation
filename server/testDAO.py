from test_pool import statesDAO

values = (1434159,843473,62.1,36.5,'AL')
statesDAO.update(values)

y = statesDAO.findByAbv('AL')

print(y)

