import streamlit as st
from PIL import Image
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

header = st.container()
dataset = st.container()
features = st.container()
graph_visu1 = st.container()
graph_visu2 = st.container()
model_training = st.container()


# st.markdown(
#     """
#     <style>
#     .main {
#     background-color: #FFFFFF;
#     }
#     <style>
#     """,
#     unsafe_allow_html=True
# )

st.markdown(
    """
    <style>
    .reportview-container .main .block-container{{
        max-width: {max_width}px;
        padding-top: {padding_top}rem;
        padding-right: {padding_right}rem;
        padding-left: {padding_left}rem;
        padding-bottom: {padding_bottom}rem;
    }}
    .reportview-container .main {{
        color: {COLOR};
        background-color: {BACKGROUND_COLOR};
    }}
    <style>
    """,
    unsafe_allow_html=True
)


@st.cache
def get_data(filename):
    img = Image.open(filename)

    return img


with header:
    st.title("Welcome to Grace's Graph Visualization!")
    st.text('My first Steamlit project. Let\'s visualize Graph Node Connections in a smart way!')

with dataset:
    st.header("ROI in the historical map")
    st.text('Show the ROI image')
    img = get_data("images/ROIs_Selden.png")
    st.image(img, caption="ROIs in the Selden Map")

with features:
    st.header("Graph Construction")
    st.markdown('* **KNN:** conventional k nearest neighbors')
    st.markdown('* **DWKNN:** consider data local density')

with graph_visu1:
    st.header("Pyvis Interactive Graph -- KNN")  
    try:  # Save and read graph as HTML file (on Streamlit Sharing)
        path = '/tmp'
        HtmlFile = open(f'{path}/net0_knn.html', 'r', encoding='utf-8')
    except:   # Save and read graph as HTML file (locally)
        path = 'html_files'
        HtmlFile = open(f'{path}/net0_knn.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=600)


with graph_visu2:
    st.header("Pyvis Interactive Graph -- DWKNN")  
    try:  # Save and read graph as HTML file (on Streamlit Sharing)
        path = '/tmp'
        HtmlFile = open(f'{path}/net0_dwknn.html', 'r', encoding='utf-8')
    except:   # Save and read graph as HTML file (locally)
        path = 'html_files'
        HtmlFile = open(f'{path}/net0_dwknn.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=600)


# with model_training:
#     st.header('visualize the layer in GAT')
#     st.text('which layer')

#     sel_col, disp_col = st.columns(2)

#     max_depth = sel_col.slider("select max depth", min_value=10, max_value=100,value=60,step=10)
#     n_estimators = sel_col.selectbox('How many',options=[100,200,300,'No limit'],index=0)
#     input_feature = sel_col.text_input('which feature?','1st dimension')


