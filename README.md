# Pencil Sketch Application with Flask and OpenCV

This project is a simple web-based application that allows users to create real-time pencil sketches from their webcam feed. The application uses OpenCV for image processing and Flask for the web interface. Users can start, restart, or stop the camera feed and apply the pencil sketch effect directly from the web interface.

## 🚀 Overview

The **Pencil Sketch Application** captures video input from the webcam, applies image processing techniques such as sharpening and grayscale conversion, and outputs a real-time pencil sketch effect. The project also includes a simple Flask-based UI with buttons to control the application.

## ✨ Features

- **Real-time Video Feed**: Captures video from the webcam and applies a pencil sketch effect in real-time.
- **Sharpened Image Output**: Uses a kernel to sharpen the captured frame before applying the sketch effect.
- **Simple Web Interface**: A Flask web application with buttons to start, restart, or stop the process.
- **Pencil Sketch Effect**: Converts the sharpened image into a pencil sketch using OpenCV's `divide()` function and Gaussian Blur.

## 🛠️ Installation

To set up and run the project locally, follow these steps:

### Clone the Repository


git clone https://github.com/your-github-username/pencil-sketch-app.git
cd pencil-sketch-app

## 📚 Usage

- **Start the Pencil Sketch**: Click the "Start Assistant" button to launch the pencil sketch camera feed.
- **Restart the Sketch**: If you wish to reset the camera feed and sketch, click the "Restart Assistant" button.
- **Stop the Application**: You can stop the Flask server by clicking the "Stop" button, which kills the server.

The application will display three different views:

- **Original Frame**: The raw video feed from your webcam.
- **Sharpened Image**: The image after applying the sharpening kernel.
- **Pencil Sketch**: The final pencil sketch effect created from the sharpened image.

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project or add more features, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Submit a pull request

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📞 Contact

For any questions or support, please contact:

**Abhinav Kavuluru**  
Email: kavuluruabhinav.28@gmail.com

