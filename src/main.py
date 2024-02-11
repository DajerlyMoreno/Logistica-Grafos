import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, ttk

def agregar_arista(G , u, v, w=1, di=True):
    G.add_edge(u, v, weight=w)

    if not di:
        G.add_edge(v, u, weight=w)

def find_rute():
    origen = origen_entry.get().capitalize()
    destino = destino_entry.get().capitalize()
    
    shortest_path = nx.shortest_path(G, source=origen, target=destino, weight='weight')
    shortest_distance = nx.shortest_path_length(G, source=origen, target=destino, weight='weight')
    resultado_label.config(text=f'\tRuta más corta:\n {shortest_path}  \n Distancia en Km: {shortest_distance}')
    
def show_Grafo(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Logistica MPX")
    plt.show()
    
def grafo(G):
    
    agregar_arista(G, "Sogamoso", "Duitama", 19.9)
    agregar_arista(G, "Bogota", "Cajica", 30.2)
    agregar_arista(G, "Cajica", "Zipaquira", 16.5)
    agregar_arista(G, "Cajica", "Tocancipa", 17)
    agregar_arista(G, "Zipaquira", "Ubate", 43.2)
    agregar_arista(G, "Tocancipa", "Sesquile", 19)
    agregar_arista(G, "Sesquile", "Choconta", 19.4)
    agregar_arista(G, "Ubate", "Choconta", 36.1)
    agregar_arista(G, "Ubate", "Chiquinquira", 52.1)
    agregar_arista(G, "Chiquinquira", "Raquira", 31.1)
    agregar_arista(G, "Raquira", "Villa de leyva", 23.9)
    agregar_arista(G, "Villa de leyva", "Tunja", 38.3)
    agregar_arista(G, "Choconta", "Tunja", 66.6)
    agregar_arista(G, "Tunja", "Arcabuco", 33.9)
    agregar_arista(G, "Tunja", "Paipa", 41.5)
    agregar_arista(G, "Paipa", "Duitama", 13.4)
    agregar_arista(G, "Arcabuco", "Moniquira", 13.4)
    agregar_arista(G, "Moniquira", "Barbosa", 13.4)
    agregar_arista(G, "Barbosa", "Santana", 13.4)
    agregar_arista(G, "Paipa", "Santana", 13.4)


if __name__ == '__main__':
    
    G = nx.Graph()
    grafo(G)
    ventana = tk.Tk()
    ventana.geometry("500x200+800+100")
    ventana.title("Logística MPX")
    
    # Crear etiquetas y campos de entrada para los datos
    origen_label = tk.Label(ventana, text="Origen:")
    origen_label.grid(row=0, column=0)
    origen_entry = tk.Entry(ventana)
    origen_entry.grid(row=0, column=1)
    
    destino_label = tk.Label(ventana, text="Destino:")
    destino_label.grid(row=1, column=0)
    destino_entry = tk.Entry(ventana)
    destino_entry.grid(row=1, column=1)
    
    # Botón para encontrar la ruta más corta
    boton_ruta = tk.Button(ventana, text="Encontrar ruta", command=find_rute)
    boton_ruta.grid(row=2, column=0, columnspan=2)
    
    # Etiqueta para mostrar el resultado de la ruta
    resultado_label = tk.Label(ventana, text="")
    resultado_label.grid(row=3, column=0, columnspan=2)
    

    # Mostrar el grafo
    show_Grafo(G)
    
    ventana.mainloop()

    
    