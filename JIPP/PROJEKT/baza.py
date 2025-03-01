n = 4  # mamy 4 wierzchołki od 1 do 4

# macierz odległości między wierzchołkami
# (np. dist[1][2] = 10 oznacza, że podróż od 1 do 2 kosztuje 10).
dist = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [
        0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]

# memo zapamiętuje wyniki
memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]


def fun(i, mask):
    # funkcja rekursywna fun
    # i - aktualny wierzchołek w którym jesteśmy
    # mask - to liczba binarna, której bity oznaczają odwiedzone wierzchołki
    if mask == ((1 << i) | 3):
        return dist[1][i]
    # warunek bazowy, jeśli mask zawiera tylko i oraz 1 (((1 << i) | 3)),
    # to znaczy, że odwiedziliśmy wszystkie inne miasta i musimy wrócić do 1.
    # Koszt powrotu to dist[1][i].


    # obliczanie wyniku rekursywnie
    if memo[i][mask] != -1:
        return memo[i][mask]
    #jeśli wynik jest zapisany w memo, zwracamy go od razu

    res = 10**9  # wynik tego pod-problemu

    # W przeciwnym razie próbujemy wszystkie możliwe j, które są w mask,
    # ale nie są i ani 1, i sprawdzamy, jaka trasa daje najniższy koszt.


    for j in range(1, n+1):
        if (mask & (1 << j)) != 0 and j != i and j != 1:
            res = min(res, fun(j, mask & (~(1 << i))) + dist[j][i])
    memo[i][mask] = res  # zapamiętywanie wartości minimalnej
    return res


# Pętla startowa
ans = 10**9
for i in range(1, n+1):
    # Próbujemy zacząć trasę od każdego wierzchołka i, odwiedzając wszystkie inne i wracając do 1.
    # then return from i taking the shortest route to 1

    ans = min(ans, fun(i, (1 << (n+1))-1) + dist[i][1])

    # Przechodzimy przez fun(i, (1 << (n+1))-1), co oznacza,
    # że początkowo wszystkie wierzchołki są w mask.

print("The cost of most efficient tour = " + str(ans))

    # program wypisuje minimalny koszt całej trasy TSP.

