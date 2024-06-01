# MultiLanguage_invoice_analyzer

This project is a Streamlit-based web application designed to analyze invoices in multiple languages using Google Generative AI's "gemini-pro-vision" model. The application allows users to input text prompts and upload invoice images for analysis. Here's a detailed summary of the project:

**Setup and Configuration:**


The application uses Streamlit for the web interface and the Google Generative AI library for content generation.
The Google Generative AI is configured with an API key.

**Loading the Model:**

The "gemini-pro-vision" model from Google Generative AI is loaded for use in generating responses based on the input text and image data.

**Functions:**

get_response(input, image, prompt): Generates a response using the AI model based on the input text, uploaded image, and a predefined prompt.
input_image_setup(uploaded_img): Prepares the uploaded image for processing by converting it to the required format.

**Streamlit Interface:**


Initializes the app and sets up session state to maintain conversation history.
Configures the page with a title and header.
Provides a text input field for the user to enter prompts and a file uploader for the image (supports jpg, jpeg, png formats).
Displays the uploaded image on the interface.

**Processing User Input:**

When the "Analyze the Invoice" button is clicked, the uploaded image is processed and analyzed using the predefined prompt about invoice understanding.
The response from the AI model is displayed on the interface and added to the conversation history.

**Displaying Conversation History:**

The conversation history between the user and the AI model is displayed, showing both user prompts and model responses.
This application facilitates interactive analysis of invoice images with multilingual support, leveraging advanced AI for understanding and generating content based on the invoice details.






