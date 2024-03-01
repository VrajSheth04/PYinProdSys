import streamlit as st
import uuid
from streamlit_option_menu import option_menu
from tabs import (upload_graph,
                  node_tab,
                  relation_tab,
                  storegraph_tab,
                  visualizegraph_tab,
                  analyzegraph_tab,
                  exportgraph_tab)

st.set_page_config(layout="wide",initial_sidebar_state="auto")

def print_hi(name, age):
    # Use a breakpoint in the code line below to debug your script.
    st.success(f'Hi, {name} you bitch! and You are {age} years old')  # Press Ctrl+F8 to toggle the breakpoint.

def save_node(name,age):
    node_dict = {
        "name": name,
        "age": age,
        "id": str(uuid.uuid4()),
        "Type": "Node"
        }
    st.session_state["node_list"].append(node_dict)

def save_edge(node1, relation, node2):
    edge_dict = {
        "source": node1,
        "target": node2,
        "type": relation
    }
    st.session_state["edge_list"].append(edge_dict)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if "node_list" not in st.session_state:
        st.session_state["node_list"] = []
    if "edge_list" not in st.session_state:
        st.session_state["edge_list"] = []
    if "graph_dict" not in st.session_state:
        st.session_state["graph_dict"] = []
    tab_list = ["Import Graph",
         "Create Your Node",
         "Create Relations Between Your Nodes",
         "Store the graph",
         "Visualise the graph",
         "Analyze graph",
         "Export the graph"]

    st.title('Welcome to My PY World')
    st.subheader(f'This is a fucking Pythonic World! Enter at your own risk')
    import_graph_tab, create_node_tab, create_relation_tab, store_graph_tab, visualize_graph_tab, analyze_graph_tab, export_graph_tab = st.tabs(
        ["Import Graph",
         "Create Your Node Avatar",
         "Create Relations Between Your Nodes",
         "Store the graph",
         "Visualise the graph",
         "Analyze graph",
         "Export the graph"
         ]
    )

    with st.sidebar:
        selected_tab = option_menu("Main Menu",
                               tab_list,
                               icons=['house', 'gear', "arrow-clockwise"],
                               menu_icon="cast", default_index=1,
                               orientation= "vertical" )
        st.write(selected_tab)

    if selected_tab == "Import Graph":
        upload_graph()

    if selected_tab == "Create Your Node":
        node_tab()

    if selected_tab == "Create Relations Between Your Nodes":
        relation_tab()

    if selected_tab == "Store the graph":
        storegraph_tab()

    if selected_tab == "Visualise the graph":
        visualizegraph_tab()

    if selected_tab == "Analyze graph":
       analyzegraph_tab()

    if selected_tab == "Export the graph":
        exportgraph_tab()