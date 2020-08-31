from Imageshape import *

x1 = Imageshape(int(input('Ingrese el ancho de la imagen:')), int(input('Ingrese el alto de la imagen:')))  # Pedir dimensiones de imagen
x1.generate_shape()  # primer metodo:Generar la figura
x1.show_shape()  # Segundo metodo: Visualizar la imagen
name_figure = x1.get_shape()  # Tercer metodo: Retornar nombre de la figura
figure = x1.what_shape()  # Cuarto metodo: Clasificar y retornar la figura
# Condicional para indicar si la clasificación fue correcta o incorrecta
if name_figure == name_figure:
    print('La clasificación es correcta.')
else:
    print('La clasificación no es correcta.')
