MAX_REV = 0
MAX_REV_IDX = 1


def plan_investment(r, investments, years, d, f1, f2):
    revenue = []
    invest_plan = []
    max_rev_per_year = []
    for i in range(years):
        revenue.append([0] * investments)
        invest_plan.append([-1] * investments)
        max_rev_per_year.append([0] * 2)

    for inv in range(investments):
        revenue[0][inv] = d * r[inv][0]
        if revenue[0][inv] > max_rev_per_year[0][MAX_REV]:
            max_rev_per_year[0][MAX_REV] = revenue[0][inv]
            max_rev_per_year[0][MAX_REV_IDX] = inv

    for year in range(1, years):
        for inv in range(investments):
            if max_rev_per_year[year - 1][MAX_REV_IDX] == inv:
                revenue[year][inv] = revenue[year - 1][inv] * r[inv][year] - f1
                invest_plan[year][inv] = inv
            else:
                if max_rev_per_year[year - 1][MAX_REV] - f2 > revenue[year - 1][inv] - f1:
                    revenue[year][inv] = max_rev_per_year[year - 1][MAX_REV] * r[inv][year] - f2
                    invest_plan[year][inv] = max_rev_per_year[year - 1][MAX_REV_IDX]
                else:
                    revenue[year][inv] = revenue[year - 1][inv] * r[inv][year] - f1
                    invest_plan[year][inv] = inv
            if revenue[year][inv] > max_rev_per_year[year][MAX_REV]:
                max_rev_per_year[year][MAX_REV] = revenue[year][inv]
                max_rev_per_year[year][MAX_REV_IDX] = inv

    return revenue, invest_plan, max_rev_per_year


def print_invest_plan(invest_plan, year, inv):
    if year == 0:
        print(inv, end="->")
        return
    print_invest_plan(invest_plan, year - 1, invest_plan[year][inv])
    print(inv, end="->")


def main():
    f1 = 5000
    f2 = 10000
    d = 10000
    r = [[4, 1, 4, 1, 3, 2],
         [1, 5, 2, 5, 3, 1],
         [2, 1, 2, 2, 1, 2],
         [3, 3, 3, 1, 1, 2],
         [2, 1, 3, 3, 3, 1]]
    investments = len(r)
    years = len(r[0])
    revenue, invest_plan, max_rev_per_year = plan_investment(r, investments, years, d, f1, f2)

    for row in revenue:
        print(row)
    print()
    for row in invest_plan:
        print(row)
    print()
    for row in max_rev_per_year:
        print(row)
    print()

    print_invest_plan(invest_plan, years - 1, max_rev_per_year[years - 1][MAX_REV_IDX])
    print()


if __name__ == "__main__":
    main()
