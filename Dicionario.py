dicionario = {'chave': 'valor'}
print(type(dicionario))
dicionario_2 = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
print(type(dicionario_2))
dicionario_3 = dict(primeiro=1, segundo=2, terceiro=3)
print(type(dicionario_2))
dicionario_4 = dict(zip(['primeiro', 'segundo', 'terceiro'], [1, 2, 3]))
print(type(dicionario_2))

dicionario_2.update({'quarto': 4})
print(dicionario_2)
print(dicionario_2.__len__())

dicionario_2.__setitem__('quinto', 5)
print(dicionario_2)

dicionario_4.popitem()
print(dicionario_4)
dicionario_4.pop('primeiro')
print(dicionario_4)
