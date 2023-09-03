import streamlit as st
import numpy as np
import cv2
from modelhandling4 import load_model, predict_digit
from streamlit_drawable_canvas import st_canvas
# Load the pretrained model
model = load_model()  # Replace with the path to your model

st.title("Handwritten Digit Classifier 3.0")

# Create a canvas for drawing
canvas = st_canvas(
    fill_color="black",
    stroke_width=20,
    stroke_color="#FFFFFF",
    background_color="#000000",
    width=320,
    height=320,
)

# Process and classify the drawn digit
def process_and_classify(image_data):
    # Convert to grayscale and resize
    greyscale = cv2.cvtColor(image_data, cv2.COLOR_RGB2GRAY)
    input_image_resized = cv2.resize(greyscale, (28, 28))
    
    # Normalize and reshape
    input_image_resized = input_image_resized / 255.0
    input_reshape = input_image_resized.reshape(1, 28, 28)
    
    return input_reshape

classify_button = st.button("Classify")

if classify_button:
    # Get the drawing from the canvas
    img_data = canvas.image_data.astype(np.uint8)
    # Process and classify the drawn digit
    input_reshape = process_and_classify(img_data)
    #predict_image = preprocessing(img)
    
    # Perform prediction
    prediction = predict_digit(model, input_reshape)
    
    st.write("Prediction:", prediction)