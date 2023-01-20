import streamlit as st
from PIL import Image
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

header = st.container()
dataset = st.container()
features = st.container()
graph_visu = st.container()
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

with graph_visu:
    st.header("Pyvis Interactive Graphs")  
    try:  # Save and read graph as HTML file (on Streamlit Sharing)
        path = '/tmp'
        HtmlFile = open(f'{path}/net0_knn.html', 'r', encoding='utf-8')
    except:   # Save and read graph as HTML file (locally)
        path = 'html_files'
        HtmlFile = open(f'{path}/net0_knn.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=435)


with model_training:
    st.header('visualize the layer in GAT')
    st.text('which layer')

    sel_col, disp_col = st.columns(2)

    max_depth = sel_col.slider("select max depth", min_value=10, max_value=100,value=60,step=10)
    n_estimators = sel_col.selectbox('How many',options=[100,200,300,'No limit'],index=0)
    input_feature = sel_col.text_input('which feature?','1st dimension')


