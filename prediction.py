from matplotlib import pyplot as plt
from create_Segmentation_model import my_Unet
from important_variables import img_height, img_width
import streamlit as st
from PIL import Image
import numpy as np



def segment_image(model_path):
    model = my_Unet(model_path)

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    input_col, output_col = st.columns([1, 1])
    input_col.markdown('## Input Image')
    output_col.markdown('## Location of Fracture')
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')

        image = image.resize((img_width, img_height))
        fig, axes = plt.subplots(dpi = 150)
        axes.imshow(image)
        plt.axis('off')
        input_col.pyplot(fig)
        st.write("")
        
        
        image = np.expand_dims(image, 0)/255

        
        img_pred = np.argmax(model.predict(image), axis=3)[0,:,:]


        for j in range(img_pred.shape[0]):
            if img_pred[j, :].sum() != 0:
                x0 = j
                break

        for j in range(img_pred.shape[0]-1, -1, -1):
            if img_pred[j, :].sum() != 0:
                x1 = j
                break
        
        for j in range(img_pred.shape[1]):
            if img_pred[:, j].sum() != 0:
                y0 = j
                break

        for j in range(img_pred.shape[1]-1, -1, -1):
            if img_pred[:, j].sum() != 0:
                y1 = j
                break

        try:
            c1 = (x0 + x1)//2
            c2 = (y0 + y1)//2

            fig, axes = plt.subplots(dpi = 150)

            axes.imshow(image[0])
            axes.scatter( c2, c1 , s=10000 ,  facecolors='none', edgecolors='blue', linewidth = 4) 
            plt.axis('off')
            output_col.pyplot(fig)

        


        except Exception as e:
            fig, axes = plt.subplots(dpi = 150)

            axes.imshow(image[0])
            left, width = .25, .5
            bottom, height = .25, .5
            right = left + width
            top = bottom + height
            axes.text(0.5*(left+right), 0.5*(bottom+top), "None\nFound!!",
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=40,
                    bbox=dict(boxstyle="round",
                            alpha=0.5,
                            ec=(1., 0.5, 0.5),
                            fc=(1., 0.8, 0.8),
                            ),
                    transform=axes.transAxes)
            plt.axis('off')
            output_col.pyplot(fig)


        # output_col.image(pred, caption='Segmented Image.', use_column_width=True)

        
        