def compute(pieces_possibles, reste_a_rendre) -> tuple[int, list[int]]:
    print(f"compute called with reste_a_rendre={reste_a_rendre}")
    if reste_a_rendre == 0:
        return 0, []

    if reste_a_rendre in pieces_possibles:
        return 1, [reste_a_rendre]

    # prend la plus grande piece <= reste
    piece = max(p for p in pieces_possibles if p <= reste_a_rendre)

    # recurse sur le reste restant apres avoir pris cette piece
    nb, rendu = compute(pieces_possibles, reste_a_rendre - piece)
    return nb + 1, [piece] + rendu

pieces_table = [1, 2, 5, 10, 20, 50]
reste_a_rendre = 68

print(compute(pieces_table, reste_a_rendre))