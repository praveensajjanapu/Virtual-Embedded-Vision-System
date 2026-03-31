# Virtual Embedded Vision Camera System

# Project Overview
---- This project demonstrates a virtual embedded vision system developed using a laptop environment.
The goal is to simulate how real embedded camera systems work by capturing video, processing frames,
and performing real-time object detection.

----- The system uses a webcam as a replacement for a physical camera module and implements a complete vision 
pipeline including image processing, AI-based detection, and performance monitoring.


# Objectives
The main objectives of this project are:
- To understand embedded vision system architecture  
- To implement real-time video processing  
- To integrate AI-based object detection  
- To simulate camera pipeline behavior using software tools  


# System Architecture
The project follows a simple pipeline structure:

###########  Camera Input → Frame Processing → Object Detection → Output Display  ###########

##### Camera → Processing → YOLO → Output #######

- Camera Input: Webcam used to simulate camera module  
- Processing: OpenCV handles frame operations  
- Detection: YOLO model detects objects  
- Output: Annotated frames displayed in real time  


# Features
- Real-time video capture using webcam  
- Object detection using YOLO (Ultralytics)  
- Frame processing using OpenCV  
- FPS (Frames Per Second) monitoring  
- Image saving functionality  
- Simulated embedded vision pipeline  



# Technologies Used
- Python  
- OpenCV  
- YOLO (Ultralytics)  
- NumPy  
- Basic GStreamer pipeline concepts  


# Setup Instructions

### Step 1: Update System ---bash
sudo apt update
sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip -y

# Install Required Libraries
pip3 install opencv-python numpy ultralytics

# Verify Installation
python3 --version
pip3 --version



###  Run the Project
python3 main.py

---- Once the program starts:
---- Webcam will open
---- Object detection will run in real time
---- FPS will be displayed on screen


#### Controls
Press S → Save detected frame as image
Press ESC → Exit the application
