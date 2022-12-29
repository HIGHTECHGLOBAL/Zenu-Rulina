import cv2

for i in range(38):
    imagen = cv2.imread('images/'+str(i+1)+'.jpg')
    imagen = cv2.medianBlur(imagen,5)
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    bordes = cv2.Canny(grises, 100, 200)

    contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    img_contor = cv2.drawContours(imagen, contornos, -1, (0,255,255), 2)

    cv2.imwrite('resultado-filtros/Imagen con contornos'+str(i+1)+'.jpg',img_contor)
    cv2.imwrite('resultado-filtros/bordes'+str(i+1)+'.jpg',bordes)








'''import numpy as np
import cv2
 
# Cargamos la imagen
original = cv2.imread("images/5.jpg")
#cv2.imshow("original", original)

# Convertimos a escala de grises
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
 
canny = cv2.Canny(gris, 50, 500)
 
cv2.imshow("canny", canny)

# Buscamos los contornos
(contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Mostramos el número de monedas por consola
print("He encontrado {} objetos".format(len(contornos)))

cv2.drawContours(gris,contornos,-1,(0,255,34), 2)
cv2.imshow("contornos", gris)

cv2.waitKey(0)'''