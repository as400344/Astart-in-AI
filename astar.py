
# add vertext
def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print("Vertex ", v, " already exists.")
    else:
        vertices_no = vertices_no + 1
        graph[v] = []

# create link between adjucent node
def edge(v , adj_v , w):
    global graph
    temp = (adj_v,w)
    graph[v].append(temp)

# adjucent node of vetex
def adj(v):
    global graph
    return graph[v]

H = {}

# add hurastic value
def h(v,w):
    global H
    H[v] = w

# show hurastic value
def hu(v):
    return H[v]

# to choose optimal path 
def astar(root , goal):
    print(root , goal)
    visited = []
    open = {}
    close = {}
    open[root] = 0
    while root!= None:

        for v in open:
            pass
        for neighbour in graph[root]:
            print(neighbour)


graph ={}
vertices_no = 0

# code add data
for _ in range(4):
    add_vertex(input(">"))
print("link")

link = int(input("Number of links>"))

for _ in range(link):
    edge(input("vertext>"),input("adj_vertext>"),int(input("weight>")))

print("Hurastic Value")

for _ in range(4):
    h(input("vertex>"),input("weight>"))

print("optimal path is:",astar(input("root>"),input("goal>")))
