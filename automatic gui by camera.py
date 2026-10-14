"""import cv2
import mediapipe as mp
import pyautogui
import math

# Initialize camera
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hand Detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Get screen width and height for mapping hand coordinates to the screen
screen_width, screen_height = pyautogui.size()

# Prevent PyAutoGUI fail-safe exception when moving mouse to corners
pyautogui.FAILSAFE = False

print("Virtual Air Mouse active. Pinch index and thumb to click. Press 'q' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the frame horizontally for a mirror-like natural experience
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to find hands
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw hand landmarks on the video feed
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract landmarks for Index Finger Tip (ID 8) and Thumb Tip (ID 4)
            index_finger = hand_landmarks.landmark[8]
            thumb_finger = hand_landmarks.landmark[4]

            # Convert normalized coordinates to pixel values
            x_index = int(index_finger.x * frame_width)
            y_index = int(index_finger.y * frame_height)
            
            x_thumb = int(thumb_finger.x * frame_width)
            y_thumb = int(thumb_finger.y * frame_height)

            # Map the index finger position to screen resolution
            # We add a margin so you don't have to stretch your hand to reach screen corners
            screen_x = int(index_finger.x * screen_width)
            screen_y = int(index_finger.y * screen_height)

            # Move the computer mouse cursor
            try:
                pyautogui.moveTo(screen_x, screen_y)
            except Exception:
                pass

            # Calculate distance between thumb and index finger to detect a "pinch" (Click action)
            distance = math.hypot(x_index - x_thumb, y_index - y_thumb)

            # If fingers are close together (pinch gesture), trigger a left click
            if distance < 35:
                cv2.circle(frame, (x_index, y_index), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()
                pyautogui.sleep(0.2)  # Small delay to prevent double-clicking too fast
            else:
                cv2.circle(frame, (x_index, y_index), 10, (0, 0, 255), cv2.FILLED)

    # Display the webcam window
    cv2.imshow("Virtual Air Mouse", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()"""



# ---------------------------------------------------------------------------------


"""import cv2
import mediapipe as mp
import pyautogui
import math

# Initialize camera
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hand Detector (bypassing drawing utils to avoid matplotlib bugs)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Get screen width and height for mapping hand coordinates to the screen
screen_width, screen_height = pyautogui.size()

# Prevent PyAutoGUI fail-safe exception when moving mouse to corners
pyautogui.FAILSAFE = False

print("Virtual Air Mouse active. Pinch index and thumb to click. Press 'q' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the frame horizontally for a mirror-like natural experience
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to find hands
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Extract landmarks for Index Finger Tip (ID 8) and Thumb Tip (ID 4)
            index_finger = hand_landmarks.landmark[8]
            thumb_finger = hand_landmarks.landmark[4]

            # Convert normalized coordinates to pixel values
            x_index = int(index_finger.x * frame_width)
            y_index = int(index_finger.y * frame_height)
            
            x_thumb = int(thumb_finger.x * frame_width)
            y_thumb = int(thumb_finger.y * frame_height)

            # Map the index finger position to screen resolution
            screen_x = int(index_finger.x * screen_width)
            screen_y = int(index_finger.y * screen_height)

            # Move the computer mouse cursor
            try:
                pyautogui.moveTo(screen_x, screen_y)
            except Exception:
                pass

            # Calculate distance between thumb and index finger to detect a "pinch" (Click action)
            distance = math.hypot(x_index - x_thumb, y_index - y_thumb)

            # If fingers are close together (pinch gesture), trigger a left click
            if distance < 35:
                cv2.circle(frame, (x_index, y_index), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()
                pyautogui.sleep(0.2)  # Small delay to prevent double-clicking too fast
            else:
                cv2.circle(frame, (x_index, y_index), 10, (0, 0, 255), cv2.FILLED)

    # Display the webcam window
    cv2.imshow("Virtual Air Mouse", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()"""


# ---------------------------------------------------------------------------------



import cv2
import numpy as np
import pyautogui

# Initialize the laptop webcam
cap = cv2.VideoCapture(0)

# Get computer screen dimensions to scale cursor movement accurately
screen_width, screen_height = pyautogui.size()

# Disable PyAutoGUI fail-safe triggers when cursor hits edge limits
pyautogui.FAILSAFE = False

# Define HSV color range for a bright object (Default set for a bright blue marker cap)
# Note: You can tune these lower/upper bounds depending on the color object you use.
lower_color = np.array([90, 80, 80])
upper_color = np.array([120, 255, 255])

print("Color-Tracking Air Mouse initialized.")
print("Hold a bright sky blue object in front of the camera to move the mouse.")
print("Press 'q' on your keyboard to quit.")
is_dragging = False
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Error: Camera feed unavailable.")
        break

    # Flip the frame horizontally for mirror-image natural control
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    # Convert BGR frame to HSV color space for stable color tracking
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a binary mask isolating the target color range
    color_mask = cv2.inRange(hsv_frame, lower_color, upper_color)

    # Apply morphological cleaning to remove pixel noise and small artifacts
    color_mask = cv2.erode(color_mask, None, iterations=2)
    color_mask = cv2.dilate(color_mask, None, iterations=2)

    # Find contours (outlines) of the isolated color regions
    contours, _ = cv2.findContours(color_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Identify the largest contour matching the color filter criteria
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Ignore small accidental specks of color
        if cv2.contourArea(largest_contour) > 400:
            # Find the minimum enclosing circle around the color blob
            ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)
            center = (int(x), int(y))
            
            # Draw visual indicators on the webcam feedback window
            cv2.circle(frame, center, int(radius), (0, 255, 0), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), cv2.FILLED)

            # Map webcam coordinate space to full computer screen resolution
            target_x = int((x / frame_width) * screen_width)
            target_y = int((y / frame_height) * screen_height)

            # Move mouse cursor smoothly to tracked position
            try:
                pyautogui.moveTo(target_x, target_y)
            except Exception:
                pass

    # Display the processed live video feed
    cv2.imshow("Color-Tracking Air Mouse", frame)

    # Terminate loop safely upon pressing 'q'
    key = cv2.waitKey(1) & 0xFF
    if key == ord('d'):
        if not is_dragging:
            pyautogui.mouseDown()
            is_dragging = True
        else:
            pyautogui.mouseUp()
            is_dragging = False
    elif key == ord('q'):
        break

# Release camera resources and destroy all active GUI windows
cap.release()
cv2.destroyAllWindows()
