"""Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента
выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667"""

avm, avp, avr, count = 0, 0, 0, 0
lst=[]
sm=0
with open('C:/github/file/dataset_3363_4.txt') as inf:
    for l in inf :# цикл всех строк
        l=l.split(';')
        for i in l[1::]: #цикл с первого элемента , что бы не считать фамилии
            sm+=int(i)# сумма всех балов
        l.append(sm/3)
        lst.append(l)
        sm=0
mat=0
fiz=0
rus=0
for x in lst:#сумма всех оценок у всех абитурьентов
    mat+=int(x[1])
    fiz+=int(x[2])
    rus+=int(x[3])
for x in lst:
    print(x)
print(mat/len(lst),fiz/len(lst),rus/len(lst))
with open('C:/github/file/otbet.txt','w') as ouf :
    for x in lst :
        ouf.write(str(x))
