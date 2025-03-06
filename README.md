# Facial Emotion Recognition with DeepFace and Gradio

## Overview

This project implements a facial emotion recognition system using the DeepFace library and Gradio for a user-friendly interface. Users can upload images, and the system will analyze the facial expressions to determine the dominant emotion.

## Features

- Real-time emotion detection from uploaded images.
- User-friendly web interface powered by Gradio.
- Supports multiple emotions including happy, sad, angry, surprise, fear, disgust, and neutral.

## Requirements

- Python 3.6 or higher
- Libraries:
  - `deepface`
  - `gradio`
  - `opencv-python`


## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/facial-emotion-recognition.git
   cd facial-emotion-recognition
```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Haar Cascade for Face Detection:**
   - Download the `haarcascade_frontalface_default.xml` file from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in the project directory.

## Usage

1. **Run the Application:**
   Execute the following command in your terminal:
   ```bash
   python app.py
   ```

2. **Access the Web Interface:**
   - Open your web browser and go to the URL provided in the terminal (usually `http://localhost:7860`).

3. **Upload an Image:**
   - Click on the upload button to select an image file from your computer.

4. **View Results:**
   - The application will display the dominant emotion detected in the uploaded image.


## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [DeepFace](https://github.com/serengil/deepface) for the facial analysis library.
- [Gradio](https://gradio.app/) for the easy-to-use web interface framework.
- [OpenCV](https://opencv.org/) for the computer vision library.

---

