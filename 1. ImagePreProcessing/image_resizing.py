import cv2

img = cv2.imread('../Resource/deskew_box.png')
cv2.imshow("Original", img)
# Using dsize
print(img.shape)   
out = cv2.resize(img, (200,200))
print(out.shape)

# Using fx and fy
out1 = cv2.resize(img, None, fx=2, fy=2)
cv2.imshow("Redimensionado", out)
cv2.waitKey(0)
print(out1.shape)
