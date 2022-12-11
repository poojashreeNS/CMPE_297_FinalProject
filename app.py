#importing the libraries
import streamlit as st
import joblib
from PIL import Image
from skimage.transform import resize
import numpy as np
import time
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, RobertaTokenizerFast


#loading the image captioning model created during out modelling phase
model = VisionEncoderDecoderModel.from_pretrained("./Image_Cationing_VIT_Roberta_iter2")
tokenizer = RobertaTokenizerFast.from_pretrained("./Byte_tokenizer")
feature_extractor = ViTFeatureExtractor.from_pretrained("google/vit-base-patch16-224-in21k")

def predict2(temp):
    output_string = tokenizer.decode(model.generate(feature_extractor(temp, return_tensors="pt").pixel_values)[0])
    return output_string


# Designing the interface
st.title("Image Captioning App")
# For newline
st.write('\n')

image = Image.open('images/kids running in snow.jpg')
show = st.image(image, use_column_width=True)
st.write('\n')

st.sidebar.title("Upload Image")

#Disabling warning
st.set_option('deprecation.showfileUploaderEncoding', False)

#Choose your own image
uploaded_file = st.sidebar.file_uploader(" ",type=['png', 'jpg', 'jpeg'] )

if uploaded_file is not None:
    
    u_img = Image.open(uploaded_file)
    show.image(u_img, 'Uploaded Image', use_column_width=True)


    p_img = Image.open(uploaded_file).convert("RGB")

# For newline
st.sidebar.write('\n')
    
if st.sidebar.button("Click Here to Generation Caption"):
    
    if uploaded_file is None:
        
        st.sidebar.write("Please upload an Image to generate Captions")
    
    else:
        
        with st.spinner('Generating caption for the image ...'):
            
            output_string = prediction2 = predict2(p_img)
            time.sleep(2)
            st.success('Done!')
            
        # st.sidebar.header("Algorithm Predicts: ")
        
        # st.sidebar.write(output_string, '\n' )
        st.write(output_string)
    
    
    
