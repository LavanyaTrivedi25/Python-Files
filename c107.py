import cv2
import mediapipe as mp
captureVid = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5)

def drawlandHandmarks(img, handLandmarks):
    if handLandmarks:
        for landM in handLandmarks:
            mpDraw.draw_landmarks(img, landM, mpHands.HAND_CONNECTIONS)
    
while True:
    success, img = captureVid.read()
    output = hands.process(img)
    handLandmarks = output.multi_hand_landmarks
    drawlandHandmarks(img, handLandmarks)
    cv2.imshow("display", img)
