import networkx as nx
import matplotlib.pyplot as plt

# Kreiramo prazni graf koristeci paket networkx
G = nx.Graph()

# Dodavanje grana (veza) izmedju cvorova sa odgovarajucim tezinama
G.add_edge("Grad 1", "Grad 2", weight=200)
G.add_edge("Grad 1", "Grad 3", weight=300)
G.add_edge("Grad 2", "Grad 4", weight=150)
G.add_edge("Grad 3", "Grad 4", weight=150)
G.add_edge("Grad 4", "Grad 2", weight=20)
G.add_edge("Grad 3", "Grad 1", weight=250)


#Metoda koja pronalazi najkraci put izmedju dva grada koristeci Dijkstra algoritam
def find_shortest_path(graph, start, end):
    path = nx.dijkstra_path(graph, start, end, weight='weight')
    # Pronalazak ukupne udaljenosti za taj najkraci put
    distance = nx.dijkstra_path_length(graph, start, end, weight='weight')
    return path, distance

# Metoda koja pronalazi grad sa najvise letova - grana u grafu. Grad sa najvise grana je onaj koji je povezan sa najvise drugih gradova
def find_city_with_most_flights(graph):
    return max(graph.degree, key=lambda x: x[1])[0]

# Metoda za prikazivanje grafa koristeci biblioteku matplotlib
def plot_graph(graph):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(graph, pos, node_color='red', node_size=700)
    nx.draw_networkx_edges(graph, pos, edge_color='blue', width=2)
    nx.draw_networkx_labels(graph, pos, font_size=15, font_color='white')

    # Prikuplja tezine grana i crta ih kao oznake na grafu
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='black')
    plt.title("Graf letova")
    plt.show()

# Glavna metoda koja koristi prethodno definisane metode da pronadje najkraci put
if __name__ == "__main__":

    start_city = "Grad 1"
    end_city = "Grad 4"

    #Pronalazi najkraci put izmedju gradova i ispisuje ga
    path, distance = find_shortest_path(G, start_city, end_city)
    print(f"najkraci put izmedju {start_city} i {end_city} je: {' -> '.join(path)} sa ukupnom udaljenoscu od {distance} km.")

    # Pronalazi i ispisuje grad sa njavise letova
    city_with_most_flights = find_city_with_most_flights(G)
    print(f"Grad sa najvisee letova: {city_with_most_flights}")

    plot_graph(G)
