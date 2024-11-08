import cv2
img = cv2.imread('../Resource/salt_and_pepper.png')

cv2.imshow('Entrada', img)

# Convertir a escala de grises
out = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Salida', out)
cv2.waitKey(0)