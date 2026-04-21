
# Fire Detection using YOLOv8

This project demonstrates fire detection in videos using the YOLOv8 object detection model. The system processes video frames, detects fire, and highlights the detected regions with bounding boxes.

## Demo Video
Watch the demo video on YouTube to see the system in action:

[![ Demo](https://img.youtube.com/vi/AtcrRrPUqS8/0.jpg)](https://youtu.be/AtcrRrPUqS8)


## Directory Structure

```
Senario_1_(Fire)/
├── data/
│   └── Fire_1.mp4          # Input video for fire detection
├── utils/
│   └── fireDetect.py       # Python script for fire detection
├── weights/
│   └── yolov8n.pt          # YOLOv8 model weights
└── Readme.md               # Project documentation
```

## Requirements

- Python 3.8 or higher
- Required Python libraries:
  - `opencv-python`
  - `ultralytics`

Install the dependencies using the following command:

```bash
pip install opencv-python ultralytics
```

## How to Run

1. Place the input video (`Fire_1.mp4`) in the `data/` directory.
2. Ensure the YOLOv8 model weights (`yolov8n.pt`) are in the `weights/` directory.
3. Run the fire detection script:

```bash
python fireDetect.py
```

4. The output video with fire detection will be saved as `output_fire_detection.mp4` in the current directory.

## Features

- Detects fire in video frames using YOLOv8.
- Highlights detected fire regions with red bounding boxes.
- Saves the processed video with detections.

## Notes

- The input video path and model weights path can be modified in the `fireDetect.py` script.
- Ensure the video resolution and frame rate are compatible with your system's capabilities.

## Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for the object detection model.
- OpenCV for video processing.

---

## License 
This Reposetory is for educational purpose only.
