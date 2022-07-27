from math import *
from tkinter import *


num = int(input('введите номер уравнения: '))

if num == 1:

  print('* Вероятность безотказной работы *\n')

  vbt = float(input('Введите время в часах: '))
  kofn = float(input('Ведите коэффициент надежности изделия: '))

  p_t = exp((-kofn)*vbt)
  
  print('\nНам из этой строки нужны первые 4 цифры с запятой и полследние цифры после минуса, которые показывают коэффициент:')
  print(p_t)
  
elif num == 2:
    
  print('* Интенсивность отказов n-ого элемента *\n')
  
  vbr = float((input('Введите ВБР для элемента n: ')))
  vbrt = float(input('Введите срок службы в часах: '))


  lambd = -((log10(vbr)/log10(exp(1)))/vbrt)

  l = str(lambd)
  print(f"{l[0:5]} * 10^{l[-3:]}")

  print('\nНам из этой строки нужны первые 4 цифры с запятой и полследние цифры после минуса, которые показывают коэффициент:')
  print(lambd)

elif num == 3:
  
  print('* Коэффициент готовности *\n')

  Tc = int(input('Введите ввремя одного цикла: '))
  Tv = int(input('Введите ввремя восстановления: '))
  Pn = float((input('Введите ВБР для элемента n: ')))

  k_g = ((Tc)/(Tc - Tv * (log10(Pn * Tc)/log10(exp(1)))))

  print(k_g)
         

elif num == 4:
  import this
