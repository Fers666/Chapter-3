'''Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
import requests'''

download_link = 'https://stepic.org/media/attachments/course67/3.6.3/'
filename = '699991.txt'

while filename:#пока filename имеет значение
    print(filename)
    r = requests.get(download_link + filename)#запрашиваем ссылку на новый файл
    filename = None if r.text.startswith('We') else r.text #file name будет равен None если в файле первая строка начинается на we,
    # в противном случае filename присваием имя новго фалйа ( которое указано по ссылку r )

print(r.text)