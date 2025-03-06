import subprocess

subprocess.run(["pip3", "install", "opencv-python", "numpy", "deepface", "gradio","moviepy","tf-keras"])

def predict(image):

    import cv2
    from deepface import DeepFace
    import numpy as np

    # detector = FER(mtcnn=True)

    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    result = DeepFace.analyze(image,actions=['emotion'],enforce_detection=False)

    print(result)
    return result[0]['dominant_emotion']

import gradio as gr

iface = gr.Interface(
    fn=predict,
    inputs = gr.Image(type='numpy'),
    outputs = 'label',
    live=True,
    title="Facial Expression Recognition",
    description="Please upload a image to see the expression of the person in the image. Detected label will be seen on the output side"
)

iface.launch()