import numpy as np
import cv2
#vision artificial Act10 NC 0120
# Lee la imagen en escala de grises
img = cv2.imread("corneliovega.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("corneliovega 0120", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Linea
print("La linea 0120")
# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)

# Abre la ventana con la imagen
cv2.imshow("corneliovega 0120", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#El circulo
print("El circulo 0120")
# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)

# Abre la ventana con la imagen
cv2.imshow("corneliovega 0120", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#El texto
print("El texto 0120")
# Añade a la imagen el texto "hola, soy nicole" en color blanco
img = cv2.putText(img, "Example Text", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)

# Abre la ventana con la imagen
cv2.imshow("corneliovega 0120", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#El trackbars
print("El trackbars 0120")
def on_trackbar(val):
    pass

# Crea a una imagen negra, y una ventana llamada 'corneliovega 0120'
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('corneliovega 0120')

# Crea tres trackbar en la ventana
cv2.createTrackbar('R', 'corneliovega 0120', 0, 255, on_trackbar)
cv2.createTrackbar('G', 'corneliovega 0120', 0, 255, on_trackbar)
cv2.createTrackbar('B', 'corneliovega 0120', 0, 255, on_trackbar)

while True:
    # 1. Muestra la ventana primero
    cv2.imshow('corneliovega 0120', img)

    # 2. Revisa las teclas y si la ventana sigue abierta
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or cv2.getWindowProperty('corneliovega 0120', cv2.WND_PROP_VISIBLE) < 1:
        break

    # 3. Obtiene las posiciones de los trackbars
    r = cv2.getTrackbarPos('R', 'corneliovega 0120')
    g = cv2.getTrackbarPos('G', 'corneliovega 0120')
    b = cv2.getTrackbarPos('B', 'corneliovega 0120')

    # 4. Actualiza la imagen
    img[:] = [b, g, r]

cv2.destroyAllWindows()

# El thresholding
print("El thresholding 0120")

# Cambia 'corneliovega 01201.png' por el archivo original que sí tienes en tu carpeta:
img = cv2.imread('corneliovega.jpg', 0)

ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('BINARY', thr1)
cv2.imshow('BINARY_INV', thr2)
cv2.imshow('TRUNC', thr3)
cv2.imshow('TOZERO', thr4)
cv2.imshow('TOZERO_INV', thr5)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("programa realizado por Nicole Robles NC 0120")