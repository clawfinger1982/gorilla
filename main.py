# 8. В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу
import random
import os
with open('3.txt','r',encoding='utf-8') as f:
    s=f.readlines()
    # print(s)
    marks=0 # сумма оценок
    count=0 # количество оценок
    print('Оценка ниже 3:')
    for i in s:
        mark=int(i[i.find(' '):]) # выделяем оценку
        marks+=mark
        count+=1
        e=round(float(marks/count),1) # средняя оценка
        if mark<3:
            print(i[:i.find(' ')])
    print('Средний балл: ',e)
