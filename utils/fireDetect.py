import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('../weights/yolov8n.pt')  # Path to the YOLOv8 model

# Path to the input video
video_path = '../data/Fire_1.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Set custom video dimensions
frame_width = 640  # Desired width
frame_height = 480  # Desired height
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object to save the output
out = cv2.VideoWriter('output_fire_detection.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform fire detection using YOLOv8
    results = model(frame)

    # Iterate through detections
    for result in results[0].boxes:  # Access the first result and its bounding boxes
        x1, y1, x2, y2 = result.xyxy[0]  # Bounding box coordinates
        conf = result.conf[0]  # Confidence score
        cls = result.cls[0]  # Class ID
        label = f"Fire: {conf:.2f}"
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)  # Red box for fire
        cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


    # Display the frame (optional)
    cv2.imshow('Fire Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()