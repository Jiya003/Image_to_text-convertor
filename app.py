import streamlit as st
from PIL import Image
import pytesseract
import os

# Set up the Streamlit app
st.title('Image to Text Converter')

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

    # Convert the image to text
    im = Image.open(uploaded_file)
    
    # Input for language
    language = st.text_input("Type the language of the scanned document (3 letter ID):", "eng")

    if st.button('Convert to Text'):
        # Extract text
        text = pytesseract.image_to_string(im, lang=language)

        # Display the text
        st.subheader('Extracted Text:')
        st.write(text)

        # Input for file name
        filename = st.text_input("Type output file name:", "output")

        if st.button('Save to File'):
            # Save text to file
            output_filename = f"{filename}-{language}.txt"
            with open(output_filename, "w") as file:
                file.write(text)

            st.success(f'Text has been saved to {output_filename}')
