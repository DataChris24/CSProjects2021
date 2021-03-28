from pa6_base_classes import *
import collections
import networkx as nxg
import matplotlib.pyplot as plt

amGraph = Graph()
actors = {}
movies = {}
movie_actors = {}

def build_initial_Graph():
    '''
    This function builds the initial graph with all conections between all 
    actors.
    '''
    # This reads in the actors file and creates a dictionary
    with open("./data/actors.txt", 'r', encoding="latin-1") as file1:
        for line in file1:
            text1 = line.split("|")
            actors[text1[0]] = text1[1].strip()
    file1.close()

    # This reads in the movies file and creates a dictionary
    with open("./data/movies.txt", 'r', encoding="latin-1") as file2:
        for line in file2:
            text2 = line.split("|")
            movies[text2[0]] = text2[1].strip()
    file2.close()

    # This reads in the movie-actors file and creates a dictionary
    with open("./data/movie-actors.txt", 'r', encoding="latin-1") as file3:
        for line in file3:
            text3 = line.split("|")
            key = text3[0]
            movie_actors.setdefault(key, [])  # this sets up the list for each value to be appended to, setdefault initializes a key if one is not given
            movie_actors[key].append(text3[1].strip())
    file3.close()

    # This goes through the movies-actors dictionary and adds all the vertecies/edges to the graph
    for key, value in movie_actors.items():
        for i in range(len(value)):
            for j in range(i + 1, len(value)):
                amGraph.add_edge(actors.get(value[i]), actors.get(value[j]), movies.get(key))
                amGraph.add_edge(actors.get(value[j]), actors.get(value[i]), movies.get(key))


def build_bfs_Graph():
    '''
    This function builds the BFS subgraph. Creating the shortest path to any 
    actor or actress.
    '''
    bfs = Graph()
    q = collections.deque([amGraph.get_vertex('Kevin Bacon')])
    bfs.add_vertex('Kevin Bacon')

    while q:
        V_dest = q.pop()
        if V_dest.connected_to.items() is not None: 
            for key, value in V_dest.connected_to.items():
                if key.ID not in bfs:
                    V_dest = bfs.get_vertex(V_dest.ID)
                    V_src = bfs.add_vertex(key.ID, V_dest.distance + 1, bfs.get_vertex(V_dest.ID))
                    bfs.add_edge(V_dest.ID, V_src.ID, value)
                    q.appendleft(amGraph.get_vertex(V_src.ID))
    return bfs
build_initial_Graph()
T = build_bfs_Graph()

def find_actor(name):
    '''
    This function finds an actor, if in the BFS subgraph, then prints the steps
    back to Kevin Bacon. Takes the name of the actor/actress, name.
    '''
    curr = T.get_vertex(name)
    if curr is not None:
        next = curr.predecessor
        while next is not None:
            movie = next.connected_to[curr]
            print(curr.ID,
                "appeared in",
                movie,
                "with",
                next.ID)
            curr = next
            next = curr.predecessor
    else:
        print("Actor not connected to Kevin Bacon.")

# The following shows examples of text-based path trace back to Kevin Bacon
# for multiple actors/actresses.
actorsExamples = ["Paul Walker", "Sandra Bullock"]
for actor in actorsExamples:
    print("Finding " + actor + "'s connection:")
    find_actor(actor)
    print("\n")

def visualize_graph(name):
    '''
    This function creates a graph of the specified actor, name, and saves the
    graph as a png file. Also dispalys the graph.
    '''
    viz = nxg.Graph()
    w = 3 # Setting the weight integer

    curr = T.get_vertex(name)
    if curr is not None:
        next = curr.predecessor
        viz.add_node(curr.ID)
        while next is not None:
            movie = next.connected_to[curr]
            viz.add_node(next.ID)
            viz.add_edge(next.ID, curr.ID, weight = w, label = movie, font_color='r')
            curr = next
            next = curr.predecessor
    
    pos = nxg.spring_layout(viz, k=1)
    edge_labels = nxg.get_edge_attributes(viz, 'label')
    nxg.draw(viz, pos, with_labels=True, node_color='lightblue', node_shape='s', node_size=1500, font_size=10, font_weight='bold')
    nxg.draw_networkx_edge_labels(viz, pos, edge_labels, font_color = 'red', font_weight='bold')
    plt.savefig("Bacon.png")
    plt.show()

visualize_graph("Paul Walker")

def high_Bacon():
    '''
    This function finds the actor that has the highest Bacon number
    Returns a tuple with actor name and Bacon number
    '''
    highest = None
    for actor in actors.items():
        temp = actor[1]
        act = T.get_vertex(temp)
        if act:
            if highest is None:
                highest = act
            if act.distance > highest.distance:
                highest = act

    return highest.ID, highest.distance

high = high_Bacon()
print(high[0], " has the highest Bacon number at: ", high[1])

def average_Bacon():
    '''
    This function calculates the average Bacon number
    Returns the average Bacon number
    '''
    num = 0
    sum = 0
    for actor in actors.items():
        act = T.get_vertex(actor[1])
        if act:
            num += 1
            sum += act.distance
    avg = sum / num 
    return avg

average = average_Bacon()
print("The average Bacon number is: {0:.2f}".format(average))

