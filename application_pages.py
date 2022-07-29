import streamlit as st
from important_variables import theme_image_name, model_path_unet, model_path_encoder_decoder
from prediction import segment_image

def main():
    st.sidebar.image(theme_image_name)

    st.sidebar.title("Control Panel")

    type_model = st.sidebar.radio("Select Type of Model: ", ('Unet Model', 'Simple Encoder Decoder'))

    if type_model == 'Unet Model':
        st.title(f"Bone fracture localization using {type_model}")

        segment_image(model_path_unet)

    elif type_model == 'Simple Encoder Decoder':
        st.title(f"Bone fracture localization using {type_model}")

        segment_image(model_path_encoder_decoder)

    

def homepage():
    home_image = st.image(theme_image_name)

    c1, c2, c3 = st.columns([2,1,2])


    c2.markdown('')
    c2.markdown('')
    continue_forward = c2.button('Continue >>>')

    st.session_state['home_page'] = False    

    if continue_forward:
        print('going to the application!!')
        home_image.empty()
        main()


