import streamlit as st
import networkx as nx


def output_nodes_and_edges(graph:nx.Graph):
    st.write(graph.nodes)
    st.write(graph.edges)

def count_nodes(graph):
    num_nodes = graph.number_of_nodes()
    st.write(f"Number of nodes: {num_nodes}")

def count_edges(graph):
    num_edges = graph.number_of_edges()
    st.write(f"Number of edges: {num_edges}")




