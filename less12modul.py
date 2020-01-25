import sys #список аргументов командной строки
print(len(sys.argv))

import subprocess #позволяет выводить внешние процессы
subprocess.call(['python','-h'])