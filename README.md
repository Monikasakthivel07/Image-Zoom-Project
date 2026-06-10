# Image Zoom Project

A computer vision-based application that enables users to control image zoom functionality through real-time hand gestures. The project leverages MediaPipe's hand-tracking capabilities and OpenCV image processing to create a touch-free, intuitive user interaction experience.

## Overview

This project demonstrates the integration of computer vision and human-computer interaction by allowing users to zoom images using hand gestures captured through a webcam. The system detects hand landmarks in real time, calculates finger movement patterns, and dynamically adjusts image scaling based on user gestures.

## Features

* Real-time hand gesture recognition
* Dynamic image zoom in and zoom out functionality
* Accurate hand landmark detection using MediaPipe
* Webcam-based interaction
* Responsive and intuitive user experience
* Lightweight and efficient implementation
* Web interface support using HTML, CSS, and JavaScript

## Technologies Used

### Computer Vision

* Python
* OpenCV
* MediaPipe

### Frontend

* HTML5
* CSS3
* JavaScript

### Development Tools

* Visual Studio Code
* Git
* GitHub

## Project Structure

```text
Image_Zoom-Project/
│
├── FaceTracking.py
├── hand_zoom.py
├── Front.html
├── styles.css
├── script.js
├── background.jpg
├── image.png
├── hand_landmarker.task
└── mediapipe/
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/PARAMASIVAM52/Image_Zoom-Project.git
cd Image_Zoom-Project
```

### Install Dependencies

```bash
pip install opencv-python mediapipe numpy
```

## Usage

Run the hand gesture zoom application:

```bash
python hand_zoom.py
```

Run the face tracking module:

```bash
python FaceTracking.py
```

To access the web interface, open:

```text
Front.html
```

in your preferred browser.

## How It Works

1. The webcam captures live video input.
2. MediaPipe detects and tracks hand landmarks.
3. Finger distance is measured in real time.
4. Gesture movements are interpreted as zoom commands.
5. The image scale is updated dynamically based on user interaction.

## Applications

* Touchless User Interfaces
* Smart Image Viewers
* Educational Demonstrations
* Interactive Kiosk Systems
* Accessibility Solutions
* Computer Vision Research Projects

## Future Enhancements

* Multi-hand gesture support
* Gesture-based image rotation
* Advanced gesture recognition models
* Mobile device compatibility
* Voice and gesture integrated controls

## Author

**MONIKA S**

B.Tech Information Technology

GitHub: https://github.com/Monikasakthivel07

## License

This project is intended for educational and learning purposes. Feel free to use, modify, and extend the project with proper attribution.

---

If you find this project useful, consider giving it a star on GitHub.
