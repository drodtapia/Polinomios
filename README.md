# Clases de Polinomios

### Descripción del Programa

Este programa implementa una clase de polinomios en Python que es capaz de realizar varias operaciones básicas y avanzadas, 
incluyendo suma, resta, multiplicación, derivación, integración, encontrar ceros utilizando el método de Newton-Raphson y generar una figura en formato `.png`.

### Clase Pol

La clase `Pol` se encuentra en el archivo `polinomios.py`. Puedes importar esta clase en tu script Python y utilizarla de la siguiente manera:
```python
from polinomios import pol
# Crea dos polinomios

A = pol([1., 2., 1.]) # Representa 1x^2 + 2x + 1
B = pol([1., 1.])     # Representa 1x + 1
# Realiza operaciones básicas
suma = A + B
resta = A - B
multiplicacion = A * B

# Deriva un polinomio
derivada = A.derivar()

# Integra un polinomio
integral = B.integrar()

# Encuentra ceros utilizando el método de Newton-Raphson
ceros = A.ceros()

# Grafico del Polinomio
A.graficar(-10., 10., "grafico.png")
```
### Requisitos y Dependencias
Para correr este programa, necesitarás tener instalado Python 3, así como las siguientes bibliotecas de Python:

- `matplotlib`: Para generar gráficos y figuras en formato PNG.
- `math`: Para realizar operaciones matemáticas.
- `numpy`: Para trabajar con arreglos y operaciones numéricas.
- 
### Ejemplos y Demostraciones

Para probar las clase `pol`, se proporcionan el siguiente script `ejemplo.py`.
A continuación se muestra su demostración:
```bash
$ python3 ejemplo.py
```
![Imagen](https://github.com/drodtapia/Polinomios/blob/main/grafico.png)
```bash
El primer polinomio es A = 0.0x^2+2.0x+1.0
El segundo polinomio es B = +1.0x+1.0

A + B = 0.0x^2+3.0x+2.0
A - B = 0.0x^2+1.0x+0.0
A * B = 2.0x^2+3.0x+1.0

El segundo coeficiente del polinomio A es 2.0
El polinomio B evaluado en x = 3 es 4.0

La derivada del polinomio A es +0.0x+2.0
La integral del polinomio B con constante de integracion 2 es 0.5x^2+1.0x+2.0

Uno de los ceros del polinomio A es -0.5

Se ha guardado una grafica del polinomio A para valores de x entre (-10, 10)
```
### Contribución y Colaboración

¡Tu contribución es bienvenida! Si deseas contribuir con mejoras, correcciones o nuevas características, aquí hay algunas formas de hacerlo:

1. **Informar Problemas:** Si encuentras errores o tienes ideas para nuevas características, por favor abre un problema en el [rastreador de problemas](https://github.com/drodtapia/Polinomios/issues).
   
2. **Enviar Pull Requests:** Si has realizado mejoras en el código, puedes enviar un pull request. Asegúrate de que tu código esté bien probado y documentado.

3. **Comentar y Discutir:** Incluso si no puedes contribuir con código, puedes participar en las discusiones sobre problemas y características. Tus comentarios son valiosos para mejorar el proyecto.

4. **Compartir:** ¡Ayuda a difundir este proyecto compartiéndolo con tus amigos y colegas!

¡Gracias por tu interés en contribuir al proyecto!

### Licencia

Este proyecto está bajo la Licencia [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

Esto significa que puedes:

- Compartir: copiar y redistribuir el material en cualquier medio o formato.
- Adaptar: remezclar, transformar y construir sobre el material.

Bajo los siguientes términos:

- Atribución: debes dar crédito de manera adecuada, proporcionar un enlace a la licencia e indicar si se han realizado cambios. Puedes hacerlo de cualquier manera razonable, pero no de una manera que sugiera que el licenciante te respalda a ti o al uso que haces del material.
- No Comercial: no puedes utilizar el material con fines comerciales.

Leer el texto completo de la licencia [aquí](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

### Créditos y Reconocimientos
Desarrollado por David Rodríguez.

### Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactar a drodtapia@gmail.com.
