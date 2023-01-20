import streamlit as st
from PIL import Image
import networkx as nx
from pyvis.network import Network

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()


# st.markdown(
#     """
#     <style>
#     .main {
#         background-color: #F5F5F5;
#     }
#     <style>
#     """,
#     unsafe_allow_html=True
# )


@st.cache
def get_data(filename):
    img = Image.open(filename)

    return img


with header:
    st.title("Welcome to Grace's Graph Visualization Project!")
    st.text('I want to visualize node connections in a smart interactive way')

with dataset:
    st.header("ROI in the historical maps")
    st.text('Show the ROI image')
    img = get_data("images/ROIs_Selden.png")
    st.image(img, caption="ROIs")

with features:
    st.header("Graph features")
    st.markdown('* **1st dimension:** wavelength')
    st.markdown('* **2nd dimension:** wavelength')

with model_training:
    st.header('visualize the layer in GAT')
    st.text('which layer')

    sel_col, disp_col = st.columns(2)

    max_depth = sel_col.slider("select max depth", min_value=10, max_value=100,value=60,step=10)
    n_estimators = sel_col.selectbox('How many',options=[100,200,300,'No limit'],index=0)
    input_feature = sel_col.text_input('which feature?','1st dimension')


