import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun",(20,300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0,255,0), 2)
cv2.putText(img, "Mercury",(110,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Venus",(192,254), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Earth",(288,258), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mars",(286,258), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Jupiter",(20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Saturn",(20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Uranus",(20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Neptune",(20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
#cv2.imwrite("Solar_systemwithname.jpg", img)
cv2.imshow("Output", img)


