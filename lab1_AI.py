import streamlit as st
from PIL import Image

st.title("Introduction to Artificial Intelligence")
st.markdown("Lab Report 1 : Breadth-First Search (BFS) & Depth-First Search (DFS)")
st.markdown("Name : Aliyah Afifah binti Azril   |   Student ID : SD23006   |   Section : 02G")

image = Image.open("LabReport_BSD2513_#1.jpg")
st.image(image, caption="Directed Graph", use_container_width=True)

st.divider()

graph = {
  'A' : ['B', 'D'],
  'B' : ['C', 'E', 'G'],
  'C' : ['A'],
  'D' : ['C'],
  'E' : ['H'],
  'F' : [],
  'G' : ['F'],
  'H' : ['F','G']
}

# Breadth-First Search
def bfs(graph, start):
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)
    order = []

    while queue:
        s = queue.pop(0)
        order.append(s)

        for neighbour in sorted(graph[s]):  
            if neighbour not in visited and neighbour not in queue:
                visited.append(neighbour)
                queue.append(neighbour)
    return order

# Depth-First Search 
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    order = []
    if start not in visited:
        order.append(start)
        visited.add(start)
        for neighbour in sorted(graph[start]): 
            order += dfs(graph, neighbour, visited)
    return order

st.subheader("Ununiformed Search Settings")

start_node = st.selectbox("Select starting node:", sorted(graph.keys()), index=0)

if st.button("Run BFS and DFS"):
    bfs_result = bfs(graph, start_node)
    dfs_result = dfs(graph, start_node)

    st.success("✅ ununiformed search completed successfully!")

    st.markdown("### 🔹 Breadth-First Search (BFS) Result")
    st.write(" → ".join(bfs_result))

    st.markdown("### 🔹 Depth-First Search (DFS) Result")
    st.write(" → ".join(dfs_result))

st.divider()
