import streamlit as st
from PIL import Image
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

@st.cache
def show_img(filename):
    img = Image.open(filename)
    # col1.image(filename, width=100)

    return img

# @st.cache(suppress_st_warning=True, allow_output_mutation=True)
# def load_graph(filename):
#     st.write("Cache miss: load_graph(", filename, ") ran")
#     try:  # Save and read graph as HTML file (on Streamlit Sharing)
#         path = '/tmp'
#         HtmlFile = open(f'{path}/' + filename, 'r', encoding='utf-8')
#     except:   # Save and read graph as HTML file (locally)
#         path = 'html_files'
#         HtmlFile = open(f'{path}/' + filename, 'r', encoding='utf-8')

#     return {"output": HtmlFile}


st.set_page_config(page_title="Graph Visu App", page_icon=":snowflake:", layout="wide")

st.title("Welcome to Grace's Graph Visualization!")

with st.container():
    st.sidebar.header("Intro")
    st.sidebar.write('My first Steamlit project :snowflake:. Let\'s visualize Graph Node Connections in a smart way! Powered by Pyvis.')


with st.container():
    st.sidebar.header("ROIs in the Selden Map")
    col1, col2 = st.sidebar.columns(2)
    # col1.image("images/ROI_1.png",width=100)
    col1.image(show_img("images/ROI_200p.png"))
    col2.write("There are 200 pixels drawn from the ROI to build its graph visualization.")
    col2.markdown('* *5 classes*')
    col2.markdown('* *40px/class*')
    

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
    'Which layer of attention matrix to visualize?',
    ('GAT Hidden Layer', 'GAT Output Layer'))

    if option == 'GAT Hidden Layer':
        st.write('Visualize the attention scores between nodes in the hidden layer')
        # tab_operation('net0_knn.html')
    elif option == 'GAT Output Layer':
        st.write("Visualize the attention scores between nodes in the output layer")
   
    # st.write('You selected:', option)

    # genre = st.sidebar.radio(label="", options=("GAT",), label_visibility="collapsed")
    # if genre == 'GAT':
    #     st.write('GAT adopts a single-layer feed-forward neural network to learn masked attension scores')


tab1, tab2, tab3, tab4, tab5 = st.tabs(["KNN Graph", "DWKNN Graph", "Spatial-Spectral Graph", "GAT_Hidden_Head1", "GAT_Output"])


with tab1:
    st.header("KNN Graph")
    try:  # Save and read graph as HTML file (on Streamlit Sharing)
        path = '/tmp'
        HtmlFile = open(f'{path}/net_knn_200.html', 'r', encoding='utf-8')
    except:   # Save and read graph as HTML file (locally)
        path = 'html_files'
        HtmlFile = open(f'{path}/net_knn_200.html', 'r', encoding='utf-8')

    # HtmlFile = load_graph('net_knn_200.html')['output']
    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=500)


with tab2:
    st.header("DWKNN Graph")
    try:  # Save and read graph as HTML file (on Streamlit Sharing)
        path = '/tmp'
        HtmlFile = open(f'{path}/net_dwknn_200.html', 'r', encoding='utf-8')
    except:   # Save and read graph as HTML file (locally)
        path = 'html_files'
        HtmlFile = open(f'{path}/net_dwknn_200.html', 'r', encoding='utf-8')

    # HtmlFile = load_graph('net_dwknn_200.html')['output']
    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=500)


with tab3:
    st.header("Spatial-Spectral Graph")
    try:  # Save and read graph as HTML file (on Streamlit Sharing)
        path = '/tmp'
        HtmlFile = open(f'{path}/net0_ssg_200.html', 'r', encoding='utf-8')
    except:   # Save and read graph as HTML file (locally)
        path = 'html_files'
        HtmlFile = open(f'{path}/net0_ssg_200.html', 'r', encoding='utf-8')

    # HtmlFile = load_graph('net0_ssg_200.html')['output']
    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=500)


with tab4:
    st.header("GAT_Hidden_Head1")
    try:  # Save and read graph as HTML file (on Streamlit Sharing)
        path = '/tmp'
        HtmlFile = open(f'{path}/net_Att_hid01_200.html', 'r', encoding='utf-8')
    except:   # Save and read graph as HTML file (locally)
        path = 'html_files'
        HtmlFile = open(f'{path}/net_Att_hid01_200.html', 'r', encoding='utf-8')

    # HtmlFile = load_graph('net_Att_hid01_200.html')['output']
    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=500)


with tab5:
    st.header("GAT_Output")
    try:  # Save and read graph as HTML file (on Streamlit Sharing)
        path = '/tmp'
        HtmlFile = open(f'{path}/net_Att_out_200.html', 'r', encoding='utf-8')
    except:   # Save and read graph as HTML file (locally)
        path = 'html_files'
        HtmlFile = open(f'{path}/net_Att_out_200.html', 'r', encoding='utf-8')

    # HtmlFile = load_graph('net_Att_out_200.html')['output']
    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=500)