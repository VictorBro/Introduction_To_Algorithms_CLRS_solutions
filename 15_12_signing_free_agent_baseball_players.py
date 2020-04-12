# https://www.codesdope.com/course/algorithms-knapsack-problem/


class Player:
    def __init__(self, id, position, vorp, cost):
        self.id = id
        self.position = position
        self.vorp = vorp
        self.cost = cost

    def __str__(self):
        return "(" + str(self.id) + "," + str(self.position) + "," + str(self.vorp) + "," + str(self.cost) + ")"


def merge(free_agents, start, mid, end):
    left = free_agents[start: mid + 1]
    right = free_agents[mid + 1: end + 1]
    n_left = mid + 1 - start
    n_right = end - mid
    i = j = 0
    k = start

    while i < n_left and j < n_right:
        if left[i].position < right[j].position:
            free_agents[k] = left[i]
            i += 1
        elif left[i].position == right[j].position:
            if left[i].vorp <= right[j].vorp:
                free_agents[k] = left[i]
                i += 1
            else:
                free_agents[k] = right[j]
                j += 1
        else:
            free_agents[k] = right[j]
            j += 1
        k += 1

    while i < n_left:
        free_agents[k] = left[i]
        i += 1
        k += 1

    while j < n_right:
        free_agents[k] = right[j]
        j += 1
        k += 1


def sort_players(free_agents, start, end):
    if start < end:
        mid = (start + end) // 2
        sort_players(free_agents, start, mid)
        sort_players(free_agents, mid + 1, end)
        merge(free_agents, start, mid, end)


def get_player_list_and_cost(p, players_by_pos, i, j, final_player_list):
    if i >= 0 and p[i][j] > 0:
        while i > 0 and p[i][j] == p[i - 1][j]:
            i -= 1
        for player in players_by_pos[i]:
            if player.id == p[i][j]:
                w = player.cost // 100000
                cost = player.cost
                cost += get_player_list_and_cost(p, players_by_pos, i - 1, j - w, final_player_list)
                final_player_list[i] = p[i][j]
                return cost
    return 0


def sign_players(n, free_agents, x):
    players = len(free_agents)
    sort_players(free_agents, 0, players - 1)  # O(p log p)
    players_by_pos = []
    for i in range(n):
        players_by_pos.append([])
    for player in free_agents:
        players_by_pos[player.position - 1].append(player)

    c = []
    p = []
    k = x // 100000
    for i in range(n):  # S(nk + p)
        c.append([0] * (k + 1))
        p.append([0] * (k + 1))

    for j in range(k + 1):
        for player in players_by_pos[0]:
            if player.cost <= j * 100000 and player.vorp > c[0][j]:
                c[0][j] = player.vorp
                p[0][j] = player.id
    for i in range(1, n):
        for j in range(1, k + 1):
            c[i][j] = c[i - 1][j]
            p[i][j] = p[i - 1][j]
            for player in players_by_pos[i]:  # O(kp)
                w = player.cost // 100000
                if player.cost <= j * 100000 and player.vorp + c[i - 1][j - w] > c[i][j]:
                    c[i][j] = player.vorp + c[i - 1][j - w]
                    p[i][j] = player.id

    for row in c:
        print(row)
    print()
    for row in p:
        print(row)
    print()

    final_player_list = [0] * n
    cost = 0
    cost += get_player_list_and_cost(p, players_by_pos, n - 1, k, final_player_list)
    print("total VORP:", c[n - 1][k])
    print("total cost:", cost)
    print(final_player_list)


def main():
    n = 5
    free_agents = [Player(2, 1, 15, 300000),
                   Player(1, 1, 13, 200000),
                   Player(3, 2, 7, 300000),
                   Player(4, 2, 5, 200000),
                   Player(5, 3, 7, 100000),
                   Player(6, 3, 8, 300000),
                   Player(7, 4, 10, 100000),
                   Player(9, 4, 16, 200000),
                   Player(8, 4, 15, 200000),
                   Player(10, 5, 15, 200000),
                   Player(11, 5, 16, 200000)]
    x = 1000000
    sign_players(n, free_agents, x)


if __name__ == "__main__":
    main()
