import cv2

# Open the first camera device
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("❌ Error: Could not open camera.")
    exit()

print("✅ Camera opened successfully. Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to grab frame")
        break

    # Display the resulting frame
    cv2.imshow('Raspberry Pi Camera', frame)

    # Exit with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and destroy window
cap.release()
cv2.destroyAllWindows()
