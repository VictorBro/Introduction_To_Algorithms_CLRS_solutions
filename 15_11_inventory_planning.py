def h(i):
    return i


def plan_inventory(d, D, n, m, c):
    costs = []
    plan = []

    for i in range(n):
        costs.append([-1] * (D + 1))
        plan.append([-1] * (D + 1))

    costs[0][0] = max(0, c * (d[0] - m))
    for j in range(1, D + 1):
        part_time_cost = max(0, c * (d[0] + j - m))
        costs[0][j] = part_time_cost + h(j)

    for i in range(1, n):
        for j in range(D + 1):
            part_time_cost = max(0, c * (d[i] + j - m))
            costs[i][j] = costs[i - 1][0] + part_time_cost + h(j)
            plan[i][j] = 0
            end = min(D + 1, d[i] + j + 1)
            for k in range(1, end):
                part_time_cost = max(0, c * (d[i] + j - m - k))
                if costs[i][j] > costs[i - 1][k] + part_time_cost + h(j):
                    costs[i][j] = costs[i - 1][k] + part_time_cost + h(j)
                    plan[i][j] = k

    return costs, plan


def print_plan(plan, d, i, j):
    if i == 0:
        print(i, ":", d[i] + j, ", unsold:", j)
        return
    print_plan(plan, d, i - 1, plan[i][j])
    print(i, ":", d[i] + j - plan[i][j], ", unsold:", j)


def main():
    d = [1, 4, 3, 1]
    D = 0
    for x in d:
        D += x
    n = 4
    m = 2
    c = 2
    costs, plan = plan_inventory(d, D, n, m, c)

    for row in costs:
        print(row)
    print()
    for row in plan:
        print(row)
    print()

    print_plan(plan, d, n - 1, 0)


if __name__ == "__main__":
    main()
