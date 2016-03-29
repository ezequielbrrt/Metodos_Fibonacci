#! /usr/bin/python
# -*- coding: utf-8 -*-

from tqdm import tqdm
from time import time
import math
import Gnuplot	
import matplotlib.pyplot as plt

#########Recursividad#####################
def sol_recursiva(n):
	if n==1 or n==2:
		return 1
	return sol_recursiva(n-1)+sol_recursiva(n-2)
#######################################

#########Iteraciones#################
def sol_iterativa(n):
	a,b = 1,1
	for i in range(n-1):
 		a,b = b,a+b
	return a
######################################

#########Programación Dinámica############
M = {0: 0, 1: 1}
def prog_dinamica(n):
	if n in M:
		return M[n]
	M[n] = prog_dinamica(n - 1) + prog_dinamica(n - 2)
	return M[n]
###################################

########Solución Dorada#############
def potencia(b,n):
    # Caso base
    if n <= 0:
        return 1
    # n par
    if n % 2 == 0:
        pot = potencia(b, n/2)
        return pot * pot
    # n impar
    else:
        pot = potencia(b, (n-1)/2)
        return pot * pot * b
def sol_dorada(n):
	SQRT5 = math.sqrt(5)
	PHI = (SQRT5 + 1)/2
	return int(PHI ** n / SQRT5 + 0.5)
######################################

############Matrices################	
def pow(x, n, I, mult):
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y
def identity_matrix(n):
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]
def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]
def matrices(n):
    F = pow([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return F[0][1]
#####################################



#print "aLGORITMO DE MATRIES",fib(1024)
pruebas = {
	0 : 2** 0, 1 : 2** 1,
	2 : 2** 2, 3 : 2** 3,
	4 : 2** 4, 5 : 2** 5,
	6 : 2** 6, 7 : 2** 7,
	8 : 2** 8, 9 : 2** 9,
	10 : 2** 10, 
}
metodo = {
	1 : sol_recursiva,
	2 : sol_iterativa,
	3 : prog_dinamica,
	4 : sol_dorada,
	5 : matrices, 
}

NUM_METODO = 4
NUM_PRUEBA = 10


def main():
	met1 = [7.10487365723e-05,3.21865081787e-05,2.21729278564e-05,3.69548797607e-05,0.000588893890381,1.24954891205]
	met2 = []
	met3 = []
	met4 = []
	met5 = []
	tiempos = ""
	print pruebas	
	alg = open("tiempos.txt","w")
	alg.close()
	#for x in range(2,11):
	#	alg = open("tiempos.txt","a")
	for i in range(len(pruebas)):
		tiempo_inicial = time() 
		meto =  str(metodo[NUM_METODO](pruebas[i]))
		print len(meto)
		tiempo_final = time()
		#tiempos = tiempos + str(tiempo_final - tiempo_inicial)
		#alg.write(str(tiempo_final - tiempo_inicial)+",")
	"""alg.write("\n")	
				alg.close()
				t= open("tiempos.txt","r").read()
				aux = t.split("\n")
				met2 = str(aux[0]).split(",")
				met3 = str(aux[1]).split(",")
				met4 = str(aux[2]).split(",")
				met5 = str(aux[3]).split(",")
				del met2[-1]
				del met3[-1]
				del met4[-1]
				del met5[-1]
				met2 = map(float,met2)
				met3 = map(float,met3)
				met4 = map(float,met4)
				met5 = map(float,met5)
				gp = Gnuplot.Gnuplot(persist = 1)
				x = [1,2,4,8,16,32,64,128,256,512,1042]
				#plot1 = Gnuplot.PlotItems.Data(x,met1, with_="lines", title="Tiempo/Recursivo")
				plot2 = Gnuplot.PlotItems.Data(x,met2, with_="lines", title="Tiempo/Iterativo")
				plot3 = Gnuplot.PlotItems.Data(x,met3, with_="lines", title="Tiempo/Dinamico")
				plot4 = Gnuplot.PlotItems.Data(x,met4, with_="lines", title="Tiempo/Dorada")
				plot5 = Gnuplot.PlotItems.Data(x,met5, with_="lines", title="Tiempo/Matrices")
				gp.plot(plot2,plot3,plot4,plot5)
			"""

main()

