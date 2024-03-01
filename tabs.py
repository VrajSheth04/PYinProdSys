import streamlit as st
import json
import uuid
from model import metamodel_dict
import graphviz
from streamlit_agraph import agraph, Node, Edge, Config
import networkx as nx
from graphFunction import count_nodes, count_edges, output_nodes_and_edges

def upload_graph():
    uploaded_graph = st.file_uploader("Upload an existing graph", type="json")
    if uploaded_graph is not None:
        uploaded_graph_dict = json.load(uploaded_graph)
        uploaded_nodes = uploaded_graph_dict["nodes"]
        uploaded_edges = uploaded_graph_dict["edges"]
        st.write(uploaded_graph_dict)
    else:
        st.info("Please upload a graph if available")

    update_graph_button = st.button("Update Graph via the upload", use_container_width=True, type="primary")
    if update_graph_button and uploaded_graph is not None:
        st.session_state["node_list"] = uploaded_nodes
        st.session_state["edge_list"] = uploaded_edges

def node_tab():
    name_node = st.text_input("Type in the name of the bitch trying to enter this Pythonic world")
    age_node = int(st.number_input("Type in your age you bitch", value=0))
    print_hi(name_node, age_node)
    save_node_button = st.button("Enter the Pythonic World", use_container_width=True, type="primary")
    if save_node_button:
        save_node(name_node, age_node)
    st.write(st.session_state["node_list"])

def relation_tab():
    Node1_col, relation_col, Node2_col = st.columns(3)
    node_list = st.session_state["node_list"]
    node_name_list = []
    for node in node_list:
        node_name_list.append(node["name"])
    with Node1_col:
        node1_select = st.selectbox("Select the first Node", options=node_name_list, key=Node1_col)
    with relation_col:
        # logic
        relation_list = metamodel_dict["edges"]
        # UI rendering
        relation_name = st.selectbox("Specify your Nodeic relation",
                                     options=["Ally with", "Parent of", "Demigod of", "Offspring of", "Colleague of"])
    with Node2_col:
        node2_select = st.selectbox("Select the second Node", options=node_name_list, key=Node2_col)
    store_edge_button = st.button("Store Relation Between your Nodes", use_container_width=True, type="primary")
    if store_edge_button:
        save_edge(node1_select, relation_name, node2_select)
    st.write(f"{node1_select} is {relation_name} {node2_select}")

    st.write(st.session_state["node_list"])


def storegraph_tab():
    with st.expander("Show individual lists"):
        st.json(st.session_state["node_list"], expanded=False)
        st.json(st.session_state["edge_list"], expanded=False)

    graph_dict = {
        "nodes": st.session_state["node_list"],
        "edges": st.session_state["edge_list"],
    }
    st.session_state["graph_dict"] = graph_dict

    with st.expander("Show graph JSON", expanded=False):
        st.json(st.session_state["graph_dict"])

def visualizegraph_tab():
    with st.expander("Graphviz Visualization"):
        graph = graphviz.Digraph()
        graph_dict = st.session_state["graph_dict"]
        node_list = graph_dict["nodes"]
        edge_list = graph_dict["edges"]
        for node in node_list:
            node_name = node["name"]
            graph.node(node_name)
        for edge in edge_list:
            source = edge["source"]
            target = edge["target"]
            label = edge["type"]
            graph.edge(source, target, label)
        st.graphviz_chart(graph)

    with st.expander("Streamlit Visualization"):
        nodes = []
        edges = []

        node_list = graph_dict["nodes"]
        edge_list = graph_dict["edges"]

        for node in node_list:
            nodes.append(Node(id=node['name'], label=node["name"]))

        for edge in edge_list:
            edges.append(Edge(source=edge['source'], target=edge['target'], label=edge["type"]))

        config = Config(width=500,
                        height=500,
                        directed=True,
                        physics=True,
                        hierarchical=False,
                        nodeHighlightBehaviour=True,
                        highlightColor="#F7A7A6",  # or "blue"
                        collapsible=False
                        )
        return_value = agraph(nodes=nodes, edges=edges, config=config)

def analyzegraph_tab():
    G = nx.Graph()
    graph_dict = st.session_state["graph_dict"]
    node_list = graph_dict["nodes"]
    edge_list = graph_dict["edges"]
    node_tuples_list = []
    edge_tuples_list = []

    for node in node_list:
        node_tuple = (node["name"], node)
        node_tuples_list.append(node_tuple)

    for edge in edge_list:
        edge_tuple = (edge["source"], edge["target"], edge)
        edge_tuples_list.append(edge_tuple)

    G.add_nodes_from(node_tuples_list)
    G.add_edges_from(edge_tuples_list)

    select_function = st.selectbox(label="Select Function", options={"Output nodes and edges", "Count Nodes"})
    if select_function == "Output nodes and edges":
        output_nodes_and_edges(graph=G)

    elif select_function == "Count Nodes":
        count_nodes(graph=G)
        count_edges(graph=G)

    st.write(G.nodes)
    st.write(G.edges)


def exportgraph_tab():
    graph_string = json.dumps(st.session_state["graph_dict"])
    st.download_button(
        "Export Graph to JSON",
        file_name="graph.json",
        mime="application/json",
        data=graph_string,
        use_container_width=True,
        type="primary"
    )


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