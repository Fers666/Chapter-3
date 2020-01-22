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

with open ("C:/github/file/dataset_3363_4.txt", "r", encoding="utf-8") as inf:
	ouf = open("C:/github/file/otbet.txt", "r+")
	for line in inf:
		count +=1
		line = line.strip().split(';')
		print(line)
		avgrade = (int(line[1]) + int(line[2]) + int(line[3]))/3
		avm += int(line[1])
		avp += int(line[2])
		avr += int(line[3])
		ouf.write(str(avgrade) + "\n")
	ouf.write(str(avm/count) + " ")
	ouf.write(str(avp/count) + " ")
	ouf.write(str(avr/count))
	ouf.close()