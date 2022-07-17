import time as tm
import matplotlib.pyplot as plt
import keyboard as kb
import random as rm
plt.xlabel("Problémy")
plt.ylabel("Knížky")
plt.title("Problémy vs. knížky")
mylist = []
mycislo = []
#Počet problémů
x = 0
#Počet iterací
y = 0
#Kolik problémů chci vyzkoušet?
cislo = int(input("Kolik problémů?: ")) +1
times = tm.perf_counter()
#"Mezipaměť" pro x
cislox = 1
m = int(input("Dělitel?: "))
def Plotter():
  plt.plot(mycislo, mylist)
  plt.savefig('graf.png', bbox_inches='tight')
ran = 0
while cislox != cislo:
  x = cislox
  y = 0
  ran = rm.randint(3251, 4362)
  if x % ran == 0:
    Plotter()
  mycislo.append(x)
  if kb.is_pressed("s"):
    print("Proces: ", x , "/", cislo - 1, " | Procenta: ", round((x / cislo) * 100, 2), "%" )
  while x != 0:
    x = x / m
    y = y+1
  mylist.append(y - 1001)
  cislox = cislox +1
Plotter()
timee = tm.perf_counter()
timeo = timee - times
print("Program dofinišoval. Trvalo to ", round(timeo, 2), " sekund.")