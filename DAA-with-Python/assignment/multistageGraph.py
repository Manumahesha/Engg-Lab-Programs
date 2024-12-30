import networkx as nx

def create_multistage_graph():
    G = nx.DiGraph()
    
    num_stages = int(input("Enter the number of stages: "))
    num_vertices = 0
    
    for stage in range(1, num_stages + 1):
        num_vertices_in_stage = int(input(f"Enter the number of vertices in stage {stage}: "))
        
        for _ in range(num_vertices_in_stage):
            G.add_node(num_vertices)
            num_vertices += 1
            
            if stage > 1:
                for prev_vertex in G.nodes:
                    if G.nodes[prev_vertex]['stage'] == stage - 1:
                        weight = int(input(f"Enter the weight between vertex {prev_vertex} and vertex {num_vertices}: "))
                        G.add_edge(prev_vertex, num_vertices, weight=weight)
                        
        for vertex in G.nodes:
            G.nodes[vertex]['stage'] = stage
            
    return G

def find_optimal_path(G):
    optimal_path = nx.shortest_path(G, source=0, target=G.number_of_nodes() - 1, weight='weight')
    return optimal_path

def main():
    multistage_graph = create_multistage_graph()
    optimal_path = find_optimal_path(multistage_graph)
    
    print("Optimal Path:", optimal_path)

if _name_ == "_main_":
    main()
