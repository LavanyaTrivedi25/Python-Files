import cv2
import numpy as np
import tensorflow as tf
model = tf.keras.models.load_model("keras_model.h5")
video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    img = cv2.resize(frame, (244,244))
    testImage = np.array(img, dtype = np.float32)
    testImage = np.expand_dims(testImage, axis = 0)
    normalizedImage = testImage/255.0
    prediction = model.predict(normalizedImage)
    print("prediction: ", prediction)
    cv2.imshow("result", frame)
    key = cv2.waitKey(1)
    if key == 32:
        break
video.release()
