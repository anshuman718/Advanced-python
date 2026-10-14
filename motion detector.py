import cv2 # cv2 is the OpenCV library for computer vision tasks.It provides functions for image and video processing, including reading from webcams, manipulating images, and detecting motion.
import time

# Initialize the laptop webcam (0 is usually the default built-in camera)
cap = cv2.VideoCapture(0)

# Allow the camera to warm up
time.sleep(2)

# Read the first frame
ret, frame1 = cap.read()
if not ret:
    print("Error: Could not access the webcam.")
    cap.release()
    exit()

# Convert the first frame to grayscale and apply Gaussian blur to remove noise
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

print("Motion detection active. Press 'q' on your keyboard to stop.")

while cap.isOpened():
    ret, frame2 = cap.read()
    if not ret:
        break

    # Convert the current frame to grayscale and blur it
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    # Compute the absolute difference between the previous frame and current frame
    diff = cv2.absdiff(gray1, gray2)

    # Apply thresholding to isolate significant changes
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

    # Dilate the thresholded image to fill in gaps
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours (outlines) of the moving objects
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False
    for contour in contours:
        # Ignore small movements (like lighting changes or camera noise)
        if cv2.contourArea(contour) < 1:
            continue
        
        motion_detected = True
        # Draw a dark black bounding box around the moving object
        ((x, y), radius) = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        
        # Draw the red circle
        cv2.circle(frame2, center, radius, (0, 0, 0), 2)


# To draw a red rectangle around the moving object, you can use the following line instead of the circle:
        # cv2.rectangle(frame2, (x, y), (x + w, y, h), (0, 0, 255), 2)  # Red rectangle
    
    
    # Trigger warning if motion is detected
    if motion_detected:
        cv2.putText(frame2, "WARNING: MOVEMENT DETECTED!", (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Display the live video feed
    cv2.imshow("Laptop Motion Detector", frame2)

    # Update the reference frame for the next iteration
    gray1 = gray2

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Clean up and close windows
cap.release()
cv2.destroyAllWindows()