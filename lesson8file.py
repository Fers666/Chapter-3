inf=open('file.txt','r') # ткрыть файл ттолько для чтения
s1=inf.readline()#рочитать одну строк у
s2=inf.readline()
inf.close #обязательно закрывать файл

''' конструкция для чтения файла - тоже самое что и сверху но удобнее ИСПОЛЬЗОВАТЬ ЕГО '''
with open('file.txt)') as inf :
    s1=inf.readline()
    s2=inf.readline()

''' полезные функции '''
s=inf.readline().strip() # strip убирает из строки " /t abc /n " ненужные символы , получается строка abc

''' полный пусть файла '''# что бы это работало нужно поключить модуль import os11
os.path.join('c','github','file.txt') # тоже самое что и c:/github/fule.txt

''' построчное чтение файла '''
with open('input.txt') as inf:
    for line in inf:
        line=line.strip()
        print(line)
''' запись в файл -- аналогично чтению'''
with open ('file.txt','w') as ouf :
    ouf.write('text text text\n')
    ouf.write(str(25))