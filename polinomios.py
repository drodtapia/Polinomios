#!/usr/bin/python3
#se importan los modulos necesarios para correr el programa.
import matplotlib.pyplot as plt
import matplotlib
import math
import numpy as np
#Se crea la clase de polinomios.
class pol:	
	#Constructor, que instancia los objetos, siendo el primer termino de la lista el grado n-esimo y el ultimo el grado 0.
    def __init__(self,coeficientes=[]):
    	self.coeficientes = coeficientes
	
	#Representacion en formato string de los polinomios.
    def __str__(self):
    #Se establece el formato de salida, siendo p el polinomio ingresado.
        p = ""
    #Se utiliza el comando for para iterar sobre todos los coeficientes del polinomio y se establece el formato de salida del polinomio.
        for i in range(len(self.coeficientes)):
        	if (i==len(self.coeficientes)-1) and (self.coeficientes[i]>=0):
        		p+="+"+str(self.coeficientes[i])
        	elif (i==len(self.coeficientes)-1) and (self.coeficientes[i]<0):
        		p+=str(self.coeficientes[i])
        	elif (i==len(self.coeficientes)-2) and (self.coeficientes[i]>=0):
        		p+="+"+str(self.coeficientes[i])+"x"
        	elif (i==len(self.coeficientes)-2) and (self.coeficientes[i]<0):
        		p+=str(self.coeficientes[i])+"x"
        	elif (self.coeficientes[i+1]>=0) and (i<len(self.coeficientes)-3):
        		p+=str(self.coeficientes[i])+"x^"+str(len(self.coeficientes)-1-i)+"+"
        	else:
        		p+=str(self.coeficientes[i])+"x^"+str(len(self.coeficientes)-1-i)

        return p
    #Se utilizan metodos especiales para establecer las operaciones basicas de la clase
	#suma
    def __add__(self, C):
    #se crea una lista vacia que contendra los nuevos coeficientes.
        coeficientes_nuevos = []
    #En esta parte se iguala la cantidad de elementos de la lista, rellenando ceros de manera de facilitar la suma y resta.
        if (len(self.coeficientes)>len(C.coeficientes)):
            while (len(self.coeficientes)>len(C.coeficientes)):
                C.coeficientes.insert(0,0)

        elif (len(self.coeficientes)<len(C.coeficientes)):
            while (len(self.coeficientes)<len(C.coeficientes)):
                self.coeficientes.insert(0,0)
        #Se itera y se suma terminos del mismo grado en los polinomios.
        for i in range(len(self.coeficientes)):
            coeficientes_nuevos.append(self.coeficientes[i] + C.coeficientes[i])

        return pol(coeficientes_nuevos)
    #resta
    def __sub__(self, C):
    #se crea una lista vacia que contendra los nuevos coeficientes.
        coeficientes_nuevos = []
    #Se itera y se resta terminos del mismo grado en los polinomios.
        for i in range(len(self.coeficientes)):
            coeficientes_nuevos.append(self.coeficientes[i] - C.coeficientes[i])

        return pol(coeficientes_nuevos)

	#multiplicacion
    def __mul__(self,C):
    #Se genera una lista rellenada con 0, de manera que tenga el numero de terminos del grado alcanzado en la multiplicacion de polinomios. 
        mul = [0]*(len(self.coeficientes)+len(C.coeficientes)-1)
    #Se hace una iteracion anidada sobre grados y coeficientes de cada polinomio, de manera que se realice la multiplicacion de cada coeficiente y se sumen los grados de la multiplicacion de los exponentes
        for A_grado, A_coeficiente in enumerate(self.coeficientes):
            for B_grado, B_coeficiente in enumerate(C.coeficientes):
                mul[A_grado+B_grado]+= A_coeficiente*B_coeficiente
    #Se eliminan los coeficientes ceros que se podrian haber generado en la funcion suma.
        if mul[0]==0:
            while mul[0]==0:
                mul.pop(0)
        return pol(mul)
    #Obtener el coeficiente pedido:
    def __getitem__(self,n):
        return self.coeficientes[n]
    #Evaluar algun valor de x
    def __call__(self,x):
        p_evaluado = 0
        for i in range(len(self.coeficientes)):
            p_evaluado += self.coeficientes[i]*x**(len(self.coeficientes)-1-i)
        return p_evaluado
    #Luego procedemos a crear metodos que nos permitiran realizar operaciones mas sofisticadas.
    #Derivar
    def derivar(self):
        derivada = []
        if (len(self.coeficientes)==1):
            derivada.append(self.coeficientes[0])
        else:
            pass

        for i in range(len(self.coeficientes)-1):
            derivada.append(self.coeficientes[i]*(len(self.coeficientes)-1-i))
        return pol(derivada)
    #integrar
    def integrar(self,cte):
        integral = []
        for i in range(len(self.coeficientes)):
            integral.append(self.coeficientes[i]*(len(self.coeficientes)-i)**(-1))
        integral.append(cte)
        if integral[0]==0:
            while integral[0]==0:
                integral.pop(0)
        return pol(integral)
    #Obtener ceros a traves del metodo de Newton-Raphson.
    def ceros(self,semilla,error=1.e-6):
        x_i = float(semilla)
        while abs(self(x_i)) >= error:
            x_i += -self(x_i)/self.derivar()(x_i)
        return x_i
    #Finalmente btenemos el metodo que permite graficar un polinomio.
    def graficar(self,xmin,xmax,nombre):
    #Se determina el rango que tendra el polinomio
        x = np.arange(xmin,xmax)
        grafico = 0
        for i in range(len(self.coeficientes)):
            grafico += self.coeficientes[i]*x**(len(self.coeficientes)-1-i)
    #Se grafica el grafico deseado con linea punteada en color rojo
        plt.plot(grafico,"r--")
        plt.legend([self.__str__()])
        plt.savefig(nombre)
        plt.show()
