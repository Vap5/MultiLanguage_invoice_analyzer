import streamlit as sl
import os
import io
from PIL import Image
import google.generativeai as genai

genai.configure(api_key='Write your API key')

#Load Gemini-pro Vision

model=genai.GenerativeModel('gemini-pro-vision')

def get_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_img):
    if uploaded_img is not None:
        bytes_data=uploaded_img.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_img.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("File not uploaded")


#Initialization of app
#Create or retrieve the conversation history
if 'conversation_history' not in sl.session_state:
    sl.session_state['conversation_history'] = []

sl.set_page_config(page_title="Multilanguage Invoice analyzer")
sl.header("Multilanguage Invoice analyzer")
input=sl.text_input("Input prompt: ",key='input')   # User input
uploaded_img=sl.file_uploader("Upload an image.....",type=['jpg','jpeg','png'])

image=""
if uploaded_img is not None:
    image=Image.open(uploaded_img)
    sl.image(image,caption="Uploaded image.", use_column_width=True)

submit=sl.button("Analyze the Invoice")

input_prompt=""" 
            You are an expert in understanding invoices. I will upload an image as invoice 
            and will have to answer any questions based on the uploaded invoice image"""

if submit:
    image_data=input_image_setup(uploaded_img)
    response=get_response(input_prompt,image_data,input)
    sl.subheader("The response is: ")
    sl.session_state['conversation_history'].append(("You: " + input, "Model: " + response))

    # sl.write(response)
#Display conversation history
for user, model_response in sl.session_state['conversation_history']:
    sl.text(user)
    sl.text(model_response)
