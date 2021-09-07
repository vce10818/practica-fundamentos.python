import random

# Para importar necesitas:
# python -m pip install -U pip
# python -m pip install -U matplotlib
import matplotlib.pyplot as qq

#Generacion de numeros aleatorios en py
print(random.randrange(10 , 100 , 2))


     #Reacomodar una lista al azar
#Muestra lista
lista = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
print('lista original ' , lista)
#Mezcla los datos al azar 
random.shuffle(lista)
#Mezcla los datos al azar y los muestra
print('lista desordenada ->' , lista)


#       Genera una grafica de campana GAUSS
#Genera los datos de la grafica
campana = [random.gauss(1 , 0.5) for i in range (1000)]
#genera la grafica
qq.hist(campana , bins= 15) 
#la muestra
qq.show()