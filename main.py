import streamlit as st
from dotenv import load_dotenv
from PIL import Image
from groq import Groq
import os
import base64
import time

# Load the environment variable
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def encode_image(uploaded_file):
    return base64.b64encode(uploaded_file.getvalue()).decode("utf-8")

# Get response from the image and prompt
def get_response(base64_image, prompt, temperature, max_tokens, top_p):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p
    )

    return chat_completion.choices[0].message.content

# Set the page Configuration
st.set_page_config(page_title="Fitbot",layout="wide")

# Set the Sidebar Configuration
st.sidebar.title("Fitbot Configuration")
temperature = st.sidebar.slider("Temperature", min_value = 0.0, max_value=1.0, value=0.5, step=0.1)
max_tokens = st.sidebar.slider("Max_Tokens", min_value = 100, max_value = 1000, value = 100, step = 100)
top_p = st.sidebar.slider("Top P", min_value = 0.0, max_value = 1.0, value = 0.9, step = 0.1)
top_k = st.sidebar.slider("Top K", min_value = 0, max_value = 100, value = 40, step = 1)
st.title("Fitbot")

file_upload = st.file_uploader("Upload an image", type = ["jpg", "png", "jpeg"])


if file_upload is not None:
    with st.expander("Uploaded Image"):
        image = Image.open(file_upload)  # works directly with the uploaded file object
        st.image(image, caption="Uploaded Image", width = 200)

    # Set the Prompt    
    prompt = st.text_input("Ask your question")

    if st.button("Submit"):
        with st.spinner("Generating_response..."):
            time.sleep(2) 
        st.write(get_response(encode_image(file_upload), prompt, temperature, max_tokens, top_p))