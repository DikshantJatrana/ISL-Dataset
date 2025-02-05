import cv2
import os

# Define the words for the dataset
words = ["good", "bad", "easy", "difficult", "strong", "child", "food", "fear", "understand", "practice", "sign", "language", "bye"]
keys = "wertyuiopasdf"  # Keys assigned to each word

# Directory where the images will be stored
directory = 'ISL_Sign_Language/'

# Create the dataset directory if it doesn't exist
if not os.path.exists(directory):
    os.mkdir(directory)

# Create subdirectories for each word
for word in words:
    word_dir = os.path.join(directory, word)
    if not os.path.exists(word_dir):
        os.mkdir(word_dir)

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame from the webcam
    _, frame = cap.read()

    # Get the height and width of the frame
    frame_height, frame_width = frame.shape[:2]

    # Define the region of interest (ROI) for capturing hand and upper body
    roi_x1 = int(frame_width * 0.25)  # 25% from the left
    roi_y1 = int(frame_height * 0.1)  # 10% from the top
    roi_x2 = int(frame_width * 0.75)  # 75% from the left
    roi_y2 = int(frame_height * 0.7)  # 70% from the top

    # Draw a rectangle to define the ROI in the center
    cv2.rectangle(frame, (roi_x1, roi_y1), (roi_x2, roi_y2), (255, 255, 255), 2)

    # Show the frame with the ROI
    cv2.imshow("Frame", frame)

    # Extract the Region of Interest (ROI)
    roi = frame[roi_y1:roi_y2, roi_x1:roi_x2]

    # Convert the ROI to grayscale for consistency
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Resize the image to 128x128 (you can change this based on model input size)
    gray_resized = cv2.resize(gray, (128, 128))

    # Display the ROI
    cv2.imshow("ROI", gray_resized)

    # Keyboard interrupt to capture the data
    interrupt = cv2.waitKey(10)

    # Check if 'q' is pressed to quit
    if interrupt & 0xFF == ord('q'):
        break

    # Capture images for the specified words when respective key is pressed
    for key, word in zip(keys, words):
        if interrupt & 0xFF == ord(key):
            word_dir = os.path.join(directory, word)
            count = len(os.listdir(word_dir))
            file_path = os.path.join(word_dir, f"{count}.jpg")
            cv2.imwrite(file_path, gray_resized)
            print(f"Captured {word} image: {count}.jpg")

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
