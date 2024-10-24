import cv2  # Import OpenCV for image processing
import matplotlib.pyplot as plt  # Import Matplotlib for displaying images
import easyocr as ocr  # Import EasyOCR for text detection and recognition

# Specify the path to the image file
image_path = r"D:\Modern\projects\opencv_project\data\Text Detection\test1.png"

img = cv2.imread(image_path)  # Read the image from the specified path

# Instantiate the text detector with English language support and CPU processing
reader = ocr.Reader(['en'], gpu=False)

# Detect text in the image using EasyOCR
text_ = reader.readtext(img)

# Set a threshold for text confidence score
threshold = 0.25

# Loop through each detected text item
for t in text_:
    print(t)  # Print the detected text item

    bbox, text, score = t  # Extract the bounding box, detected text, and confidence score

    # Draw a bounding box and put the detected text on the image if the score exceeds the threshold
    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)  # Draw a green rectangle around detected text
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 0, 0), 2)  # Put the detected text on the image

# Convert the image from BGR to RGB format for displaying with Matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()  # Show the processed image with detected text
