"""
NightWay - Trouver le chemin le moins risqué après une soirée
Algorithme de Dijkstra simplifié
"""

import heapq
from typing import Tuple, List

# Données hardcodées
LIAISONS = [
    ("Bar Central", "Rue Victor Hugo", 20),
    ("Rue Victor Hugo", "Place République", 30),
    ("Bar Central", "Rue des Lilas", 50),
    ("Rue des Lilas", "Place République", 10),
    ("Place République", "Domicile", 15),
    ("Rue Victor Hugo", "Domicile", 40)
]

def find_safest_path() -> Tuple[List[str], int]:
    start = "Bar Central"
    end = "Domicile"

    # Construire le graphe
    graph = {}
    for depart, destination, score in LIAISONS:
        if depart not in graph:
            graph[depart] = []
        graph[depart].append((destination, score))
    
    # Dijkstra
    distances = {start: 0}
    parent = {start: None}
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        visited.add(current)
        
        if current == end:
            break
        
        for neighbor, risk in graph.get(current, []):
            if neighbor in visited:
                continue
            
            new_dist = current_dist + risk
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parent[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))
    
    # Reconstruire le chemin
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    
    return path, distances[end]


if __name__ == "__main__":
    path, risk = find_safest_path()
    print(f"Chemin: {' → '.join(path)}")
    print(f"Risque total: {risk}")