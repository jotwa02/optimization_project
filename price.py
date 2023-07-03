import numpy as np
import csv
import networkx as nx
import matplotlib.pyplot as plt
# przykładowe wartości Q
Q_values = [0.15, 0.10, 0.11, 0.05, 0.08, 0.12, 0.16]  # m^3/s
# Przykładowe wartości L
values_of_L = [10, 20, 13, 9, 7, 8, 15]  # m
# Krawędzie grafu
edges = [(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (3, 6), (4, 7)]

A = 310
B = 4400
n = 1.5
N = 1.7
R = 1
ni = 0.72
alfa = 0.175
e = 0.5
gamma = (ni * n * alfa * B) / (796.5 * e)

#średnica
def D(Q):
    cz1 = pow((1 / (gamma * R)), (1 / (n + 5.33)))
    cz2 = pow(Q, (3 / (n + 5.33)))
    D = cz1 * cz2  # m
    return D

srednice = []
price = []
for i in range(len(Q_values)):
    sr = round(D(Q_values[i]), 2)
    srednice.append(sr)
print(srednice)

#koszta budowy
def cost(D, L):
    I = (A + B * pow(D, N)) * L
    return I

for i in range(len(srednice)):
    c = round(cost(srednice[i], values_of_L[i]), 2)
    price.append(c)
print(price)


# Tworzenie macierzy kosztów
matrix = np.zeros((len(edges), len(edges)))

# Przypisywanie wag krawędzi z listy price
for i, (u, v) in enumerate(edges):
    cost_val = price[i]
    matrix[u - 1, v - 1] = cost_val
    matrix[v - 1, u - 1] = cost_val

# Zamiana 0 na 9999 w macierzy
matrix[matrix == 0] = 999999

# Wyświetlanie macierzy kosztów
print("Macierz kosztów:")
print(matrix)


G = nx.Graph()

G.add_nodes_from(range(1, len(edges) + 1))

edge_labels = {}
for i, (u, v) in enumerate(edges):
    G.add_edge(u, v)
    edge_labels[(u, v)] = f"Cost: {matrix[u - 1, v - 1]}, Q: {Q_values[i]}"
    edge_labels[(v, u)] = f"Cost: {matrix[v - 1, u - 1]}, Q: {Q_values[i]}"

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, edge_color='black', linewidths=1,
        alpha=0.7)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.savefig("graph.png")
plt.show()

with open("mdk.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(matrix)
