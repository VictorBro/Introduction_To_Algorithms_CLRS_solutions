def find_second_smallest(A):
    n = len(A)
    losers = []
    prev_winners = [i for i in range(n)]  # indexes of previous winners

    for i in range(n):
        losers.append([])  # array of arrays

    prev_winners_num = n
    while prev_winners_num > 1:
        winners = []
        for i in range(0, prev_winners_num - 1, 2):
            first_participant_idx = prev_winners[i]
            second_participant_idx = prev_winners[i + 1]
            if A[first_participant_idx] <= A[second_participant_idx]:
                winners.append(first_participant_idx)
                losers[first_participant_idx].append(second_participant_idx)
            else:
                winners.append(second_participant_idx)
                losers[second_participant_idx].append(first_participant_idx)
        if prev_winners_num % 2 != 0:
            winners.append(prev_winners[prev_winners_num - 1])
        prev_winners = winners
        prev_winners_num = len(prev_winners)

    winner = prev_winners[0]
    print(winner)
    second_min = losers[winner][0]
    for i in range(len(losers[winner])):
        if A[second_min] > A[losers[winner][i]]:
            second_min = losers[winner][i]

    return second_min


def main():
    A = [7, 1, 2, 5, 4, 8, 9, 3, 6]
    print(find_second_smallest(A))


if __name__ == "__main__":
    main()
