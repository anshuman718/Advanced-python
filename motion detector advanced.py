import cv2
import time
import winsound  # Built-in library for Windows audio alerts

# Initialize the laptop webcam
cap = cv2.VideoCapture(0)

# Allow the camera to warm up
time.sleep(2)

# Read the first frame
ret, frame1 = cap.read()
if not ret:
    print("Error: Could not access the webcam.")
    cap.release()
    exit()

# Convert to grayscale and blur
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

print("Motion detection with audio alert active. Press 'q' to stop.")

# Variable to control the beep frequency so it doesn't beep continuously on every single frame
last_beep_time = 0

while cap.isOpened():
    ret, frame2 = cap.read()
    if not ret:
        break

    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    # Compute absolute difference
    diff = cv2.absdiff(gray1, gray2)
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) < 1500:
            continue
        
        motion_detected = True
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 0, 255), 2)

    if motion_detected:
        cv2.putText(frame2, "WARNING: MOVEMENT DETECTED!", (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        
        # Trigger an audio beep (Frequency: 2500Hz, Duration: 150ms)
        # We add a timer check so it doesn't spam the beep 30 times a second
        current_time = time.time()
        if current_time - last_beep_time > 0.5:  # Beeps at most once every 0.5 seconds
            try:
                winsound.Beep(2500, 150)
            except RuntimeError:
                pass
            last_beep_time = current_time

    cv2.imshow("Laptop Motion Detector with Alarm", frame2)
    gray1 = gray2

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()