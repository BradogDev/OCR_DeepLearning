import cv2
import pytesseract

img = cv2.imread('../Resource/voucherTIA.png')
#img = cv2.imread('../Resource/skew_normal.PNG')

cv2.imshow("Original Image", img)

#CONVIERTE A ESCALA DE GRISES
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Image Gray", img_gray)

ret, thresh = cv2.threshold(img_gray, 70, 255, cv2.THRESH_BINARY)

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(thresh, config= r"--psm 11", lang='spa')

out = pytesseract.image_to_string(img_gray, lang='spa')
#print(pytesseract.get_languages())

print(out)
cv2.waitKey(0)