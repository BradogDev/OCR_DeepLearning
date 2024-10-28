import cv2

img = cv2.imread('../Resource/salt_and_pepper.png')
out = cv2.medianBlur(img, 5)
cv2.imshow('Entrada', img)
cv2.imshow('Salida', out)
cv2.waitKey(0)