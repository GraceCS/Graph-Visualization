import streamlit as st
from PIL import Image
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

# @st.cache
# def get_data(filename):
#     img = Image.open(filename)

#     return img

st.set_page_config(page_title="Graph Visu App", page_icon=":snowflake:", layout="wide")

st.title("Welcome to Grace's Graph Visualization!")

with st.container():
    st.sidebar.header("Intro")
    st.sidebar.write('My first Steamlit project :snowflake:. Let\'s visualize Graph Node Connections in a smart way! Powered by Pyvis.')


with st.container():
    st.sidebar.header("ROIs in the Selden Map")
    col1, col2 = st.sidebar.columns(2)
    col1.image("images/ROI_1.png",width=100)


# @st.cache
# def tab_operation(pathname):
#     try:  # Save and read graph as HTML file (on Streamlit Sharing)
#         path = '/tmp'
#         HtmlFile = open(f'{path}/'+pathname, 'r', encoding='utf-8')
#     except:   # Save and read graph as HTML file (locally)
#         path = 'html_files'
#         HtmlFile = open(f'{path}/'+pathname, 'r', encoding='utf-8')

#     # Load HTML file in HTML component for display on Streamlit page
#     return components.html(HtmlFile.read(), height=500)


# use radio button
with st.container():
    st.sidebar.header("Graph Construction Approach")
    genre = st.sidebar.radio(label="", options=('KNN', 'DWKNN', 'Spatial-Spectral Graph'), label_visibility="collapsed")

    if genre == 'KNN':
        st.write('KNN decides graph connections via conventional K nearnest neighbors')
        # tab_operation('net0_knn.html')
    elif genre == 'DWKNN':
        st.write("Density-weighted KNN considers local data density to assign adaptive number of neighbors")
    else:
        st.write("Add spatial connections and form a Spatial-Spectral graph")


with st.container():
    st.sidebar.header("Attention Mechanism")
    option = st.sidebar.selectbox(
    'What attention mechanism would you like to use?',
    ('GAT', 'SAD'))

    st.write('You selected:', option)

    # genre = st.sidebar.radio(label="", options=("GAT",), label_visibility="collapsed")
    # if genre == 'GAT':
    #     st.write('GAT adopts a single-layer feed-forward neural network to learn masked attension scores')


tab1, tab2, tab3, tab4 = st.tabs(["KNN Graph", "DWKNN Graph", "Spatial-Spectral Graph", "GAT"])


with tab1:
    st.header("KNN Graph")
    try:  # Save and read graph as HTML file (on Streamlit Sharing)
        path = '/tmp'
        HtmlFile = open(f'{path}/net0_knn.html', 'r', encoding='utf-8')
    except:   # Save and read graph as HTML file (locally)
        path = 'html_files'
        HtmlFile = open(f'{path}/net0_knn.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=500)


with tab2:
    st.header("DWKNN Graph")
    try:  # Save and read graph as HTML file (on Streamlit Sharing)
        path = '/tmp'
        HtmlFile = open(f'{path}/net0_dwknn.html', 'r', encoding='utf-8')
    except:   # Save and read graph as HTML file (locally)
        path = 'html_files'
        HtmlFile = open(f'{path}/net0_dwknn.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=500)


with tab3:
   st.header("Spatial-Spectral Graph")
   st.write("Upcoming")


with tab4:
    st.header("GAT")
    try:  # Save and read graph as HTML file (on Streamlit Sharing)
        path = '/tmp'
        HtmlFile = open(f'{path}/net_toy1.html', 'r', encoding='utf-8')
    except:   # Save and read graph as HTML file (locally)
        path = 'html_files'
        HtmlFile = open(f'{path}/net_toy1.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=500)