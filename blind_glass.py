import cv2
import numpy as np
import pyttsx3

# Voice engine
engine = pyttsx3.init()

# Camera start
cap = cv2.VideoCapture(0)

# First frame read
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Difference between frames
    diff = cv2.absdiff(prev_gray, gray)

    # Threshold (noise remove)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Count white pixels
    change = np.sum(thresh)

    if change > 500000:
        cv2.putText(frame, "OBJECT DETECTED", (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        engine.say("Something ahead")
        engine.runAndWait()

    cv2.imshow("Camera", frame)

    prev_gray = gray

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
