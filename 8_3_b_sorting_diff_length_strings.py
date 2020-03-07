class WordWithLen:
    def __init__(self, word=""):
        self.word = word
        self.len = len(word)


def get_max_length(words_with_len, n):
    max_length = 0
    for i in range(n):
        if words_with_len[i].len > max_length:
            max_length = words_with_len[i].len
    return max_length


def counting_sort(words_with_len, n, char_idx):
    k = 27  # num of characters in English alphabet + 1 extra
    B = [WordWithLen()] * n
    C = [0] * k

    for i in range(n):
        if words_with_len[i].len <= char_idx:
            C[0] += 1
        else:
            index = ord(words_with_len[i].word[char_idx]) - ord('a') + 1
            C[index] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        if words_with_len[i].len <= char_idx:
            B[C[0] - 1] = words_with_len[i]
            C[0] -= 1
        else:
            index = ord(words_with_len[i].word[char_idx]) - ord('a') + 1
            B[C[index] - 1] = words_with_len[i]
            C[index] -= 1
    for i in range(n):
        words_with_len[i] = B[i]


def radix_sort(words):
    n = len(words)
    if n == 0:
        return

    words_with_len = []
    for i in range(n):
        words_with_len.append(WordWithLen(words[i]))

    max_length = get_max_length(words_with_len, n)
    if max_length == 0:
        return

    for i in range(max_length - 1, -1, -1):
        counting_sort(words_with_len, n, i)
    for i in range(n):
        print(words_with_len[i].word, words_with_len[i].len)


def main():
    words = ["b", "ab", "a", "ca", "c", "abb", "abab"]
    radix_sort(words)


if __name__ == "__main__":
    main()
