'''
 перебор элементов словаря
'''
d={'c':14,'a':12,'g':18}
for key in d:
    print(key,end=' ')
    ''' выведет все ключи словаря '''
for key in d.keys():
    print(key,end=' ' )
    ''' выведет все ключи словаря '''
for value in d.values():
    print(value,end=' ')
    '''выведет все элементы словаря'''
for key,value in d.items():
    print(key,value,end='; ')
    ''' выведет ключи и принадлежащие им элементы '''