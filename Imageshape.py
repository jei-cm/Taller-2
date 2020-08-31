import cv2
import numpy as np
import random


class Imageshape:  # creación clase
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shape = []
        self.num = 0
        self.name_shape = ''
        self.figure = ''

    def generate_shape(self):
        self.num = random.randrange(4)  # generar un número random entre 0 y 3
        self.shape = np.zeros((self.height, self.width, 3), dtype=np.uint8)  # Se crea y almacena una imagen con fondo negro y figura dibujada
        center = (self.width // 2, self.height // 2)  # se define el centro de la imagen creada
        lado = min(self.width, self.height) // 2  # se define longitud del lado para triangulo y cuadrado

        if self.num == 0:  # Triangulo
            h_triangle = int(np.sqrt((lado**2) - (lado**2//2)))  # definicion de la altura del triangulo
            # Como es un triangulo equilatero,para obtener el centro del triangulo se halla la altura con pitagoras
            # El centro en x esta en la mitad del lado de abajo,en y esta en 1/3 de la altura del triangulo
            # se hallaron los puntos para dibujar el triangulo
            p1 = (center[0] - lado // 2, center[1] + h_triangle // 3)  # (x_centro-lado/2, y_centro + h_triangle)
            p2 = (center[0] + lado // 2, center[1] + h_triangle // 3)  # (x_centro+lado/2, y_centro + h_triangle)
            p3 = (center[0], center[1] - 2*h_triangle // 3)  # (x_centro, y_centro - 2* h_triangle//3

            t_cnt = np.array([p1, p2, p3])  # se define un matriz para generar el triangulo
            cv2.drawContours(self.shape, [t_cnt], 0, (255, 255, 0), -1)  # se rellena el triangulo

        if self.num == 1:  # cuadrado rotado (rombo-xd)
            p1 = (center[0] - lado // 2, center[1] + lado // 2)  # punto 1
            p2 = (center[0] + lado // 2, center[1] - lado // 2)  # punto 2
            cv2.rectangle(self.shape, p1, p2, (255, 255, 0), -1)  # creacion del cuadrado usando la función rectangle
            rotate = cv2.getRotationMatrix2D(center, 45, 1)  # rotar el cuadrado
            self.shape = cv2.warpAffine(self.shape, rotate, (self.width, self.height))

        if self.num == 2:  # rectangulo
            p1 = (center[0] - self.width // 4, center[1] + self.height // 4)  # punto 1
            p2 = (center[0] + self.width // 4, center[1] - self.height // 4)  # punto 2
            cv2.rectangle(self.shape, p1, p2, (255, 255, 0), -1)  # creacion rectangulo

        if self.num == 3:  # circulo
            radio = min(self.width, self.height) // 4  # definicion del radio para el circulo
            cv2.circle(self.shape, center, radio, (255, 255, 0), -1)  # creación del circulo

    def show_shape(self):
        cv2.imshow('Imagen', self.shape)  # mostrar la imagen
        cv2.waitKey(5000)  # abrirla durante 5 segundos

    def get_shape(self):
        if self.num == 0:
            self.name_shape = 'Triangle'
        if self.num == 1:
            self.name_shape = 'Square'
        if self.num == 2:
            self.name_shape = 'Rectangle'
        if self.num == 3:
            self.name_shape = 'Circle'
        return self.name_shape  # Retorna el nombre de la figura
        return self.shape  # Retorna la imagen generada

    def what_shape(self):
        gray_image = cv2.cvtColor(self.shape, cv2.COLOR_BGR2GRAY)  # pasar la imagen generada a escala de grises
        ret, binary_shape = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY)  # Binarización de la imagen
        contours, hierarchy = cv2.findContours(binary_shape, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # contorno de la figura

        for n in contours:  # ciclo para recorrer el contorno de la figura
            epsilon = 0.01 * cv2.arcLength(n, True)  # precision de la approx realizada(True indica una curva cerrada)
            approx = cv2.approxPolyDP(n, epsilon, True)  # Se hace un aprox. del contorno de la fig, obteniendo menos vertices
            x, y, w, h = cv2.boundingRect(approx)  # sirve para obtener el aspect_ratio
            aspect_ratio = float(w) / h  # se obtiene el radio entre el ancho y alto de la figura (rectangle-square)
            # con len(approx) se obtienen los vertices obtenidos en approx para cada figura
            if len(approx) == 3:
                self.figure = 'Triangle'
                print(self.figure)
            if len(approx) == 4 and aspect_ratio == 1:  # si el aspect_ratio=1, se tiene un cuadrado
                self.figure = 'Square'
                print(self.figure)
            if len(approx) == 4 and aspect_ratio != 1:
                self.figure = 'Rectangle'
                print(self.figure)
            if len(approx) >= 6:  # con la precision de 1% en epsilon, se obtienen 12 vertices
                self.figure = 'Circle'
                print(self.figure)
        return self.figure

