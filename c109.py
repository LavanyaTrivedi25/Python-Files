import cv2
import math
import mediapipe as mp
from pynput.mouse import Button, Controller
import pyautogui

mouse=Controller()

cap = cv2.VideoCapture(0)

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
height  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

(screen_width, screen_height) = pyautogui.size()

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

tipIds = [4, 8, 12, 16, 20]

pinch=False

# Define a function to count fingers
def countFingers(image, hand_landmarks, handNo=0):

	global pinch

	if hand_landmarks:
		# Get all Landmarks of the FIRST Hand VISIBLE
		landmarks = hand_landmarks[handNo].landmark

		# Count Fingers        
		fingers = []

		for lm_index in tipIds:
			# Get Finger Tip and Bottom y Position Value
			finger_tip_y = landmarks[lm_index].y 
			finger_bottom_y = landmarks[lm_index - 2].y

			# Check if ANY FINGER is OPEN or CLOSED
			if lm_index !=4:
				if finger_tip_y < finger_bottom_y:
					fingers.append(1)


				if finger_tip_y > finger_bottom_y:
					fingers.append(0)

		totalFingers = fingers.count(1)

		# PINCH

		# Draw a LINE between FINGER TIP and THUMB TIP
		fingerx = int((landmarks[8].x)*width)
		fingery = int((landmarks[8].y)*height)
		thumbx = int((landmarks[4].x)*width)
		thumby = int((landmarks[4].y)*height)
		cv2.line(image, (fingerx, fingery), (thumbx, thumby), (255,0,0), 3)

		# Draw a CIRCLE on CENTER of the LINE between FINGER TIP and THUMB TIP
		centerx = int((fingerx+thumbx)/2)
		centery = int((fingery+thumby)/2)
		cv2.circle(image, (centerx, centery), 3, (0,0,255), 3)

		# Calculate DISTANCE between FINGER TIP and THUMB TIP

		distance = math.sqrt(((fingerx - thumbx)**2)+ ((fingery - thumby)**2))
		#print(distance)
		print("Computer Screen Size", screen_width, screen_height, "Output window size", width, height)
		print("Mouse Position", mouse.position, "center", centerx, centery)
		
		# Set Mouse Position on the Screen Relative to the Output Window Size	
		rmousex = (centerx/width)*screen_width
		rmousey = (centery/height)*screen_height
		mouse.position = (rmousex, rmousey)

		# Check PINCH Formation Conditions
		if distance > 40:
			if pinch == True:
				pinch = False			
				mouse.release(Button.left)

		if distance <= 40 :
			if(pinch==False):
				pinch=True
				mouse.press(Button.left)


# Define a function to 
def drawHandLanmarks(image, hand_landmarks):

    # Darw connections between landmark points
    if hand_landmarks:

      for landmarks in hand_landmarks:
               
        mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)



while True:
	success, image = cap.read()
	
	image = cv2.flip(image, 1)

	# Detect the Hands Landmarks 
	results = hands.process(image)

	# Get landmark position from the processed result
	hand_landmarks = results.multi_hand_landmarks

	# Draw Landmarks
	drawHandLanmarks(image, hand_landmarks)

	# Get Hand Fingers Position        
	countFingers(image, hand_landmarks)

	cv2.imshow("Media Controller", image)

	# Quit the window on pressing Sapcebar key
	key = cv2.waitKey(1)
	if key == 27:
		break

cv2.destroyAllWindows()
