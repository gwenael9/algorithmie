"""
NightWay - Trouver le chemin le moins risqué après une soirée
Algorithme de Dijkstra simplifié
"""

import heapq  # file de priorité (min-heap) pour extraire toujours le nœud le plus proche
from typing import Tuple, List

# Données hardcodées
LIAISONS = [
    ("Bar Central", "Rue Victor Hugo", 20),      # (départ, arrivée, risque/poids de l'arête)
    ("Rue Victor Hugo", "Place République", 30),
    ("Bar Central", "Rue des Lilas", 50),
    ("Rue des Lilas", "Place République", 10),
    ("Place République", "Domicile", 15),
    ("Rue Victor Hugo", "Domicile", 40)
]

def find_safest_path() -> Tuple[List[str], int]:
    start = "Bar Central"  # nœud de départ
    end = "Domicile"       # nœud d'arrivée

    # Construire le graphe
    graph = {}  # dict: nœud -> liste de (voisin, poids)
    for depart, destination, score in LIAISONS:
        if depart not in graph:
            graph[depart] = []          # initialise la liste si le nœud n'existe pas encore
        graph[depart].append((destination, score))  # ajoute l'arête sortante

    # Dijkstra
    distances = {start: 0}      # distance connue la plus courte jusqu'à chaque nœud (0 pour le départ)
    parent = {start: None}      # permet de reconstruire le chemin en remontant les prédécesseurs
    pq = [(0, start)]           # tas (distance, nœud), on part avec le nœud de départ à distance 0
    visited = set()             # nœuds déjà traités définitivement

    while pq:  # tant qu'il reste des nœuds à explorer
        current_dist, current = heapq.heappop(pq)  # récupère le nœud non traité de plus petite distance

        if current in visited:
            continue  # déjà traité via un autre chemin plus court, on ignore ce doublon du tas
        visited.add(current)  # on fige la distance de ce nœud, elle est optimale

        if current == end:
            break  # arrivée trouvée, plus la peine de continuer

        for neighbor, risk in graph.get(current, []):  # parcourt les voisins du nœud courant
            if neighbor in visited:
                continue  # déjà optimal, inutile de le remettre à jour

            new_dist = current_dist + risk  # distance potentielle en passant par current
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist       # on a trouvé un chemin plus court vers neighbor
                parent[neighbor] = current           # on mémorise par où on est passé
                heapq.heappush(pq, (new_dist, neighbor))  # à explorer plus tard, avec sa nouvelle distance

    # Reconstruire le chemin
    path = []
    node = end
    while node is not None:
        path.append(node)       # ajoute le nœud courant
        node = parent.get(node) # remonte vers son prédécesseur (None quand on atteint le départ)
    path.reverse()  # le chemin a été construit à l'envers (arrivée -> départ), on le remet dans le bon sens

    return path, distances[end]  # chemin trouvé + risque total cumulé


if __name__ == "__main__":
    path, risk = find_safest_path()
    print(f"Chemin: {' → '.join(path)}")
    print(f"Risque total: {risk}")