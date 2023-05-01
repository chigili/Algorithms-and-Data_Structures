def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(" ".join(map(str, output)))


def get_occurrences(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i : i + len(pattern)] == pattern
    ]


class RabinKarp:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, pattern, text):
        self.text = text
        self.pattern = pattern

        self.n = len(self.pattern)
        self._pattern_hash = self._hash_func(self.pattern)

    def _hash_func(self, string):
        res = 0
        for c in reversed(string):
            res = (res * self._multiplier + ord(c)) % self._prime
        return res

    def _precompute_hashes(self, text, pattern_size):
        hashes = [0 for _ in range(len(text) - pattern_size + 1)]

        i_start = len(text) - pattern_size
        i_end = len(text)
        last_substring = text[i_start:i_end]

        hashes[len(text) - pattern_size] = self._hash_func(last_substring)

        y = 1
        for _ in range(pattern_size):
            y = (y * self._multiplier) % self._prime

        for i in range(len(text) - pattern_size - 1, -1, -1):
            hashes[i] = (
                self._multiplier * hashes[i + 1]
                + ord(text[i])
                - ord(text[i + pattern_size]) * y
            ) % self._prime

        return hashes

    def find_occurrences(self):
        """
        Print all the positions of the occurrences of pattern in text
        in the ascending order. Use 0-based indexing of positions in
        the text.
        """
        result = []

        hashes = self._precompute_hashes(self.text, len(self.pattern))

        for i in range(len(self.text) - len(self.pattern) + 1):
            substring = self.text[i : (i + self.n)]
            substring_hash = hashes[i]

            if substring_hash != self._pattern_hash:
                continue
            else:
                if substring == self.pattern:
                    result.append(i)
        return result


if __name__ == "__main__":
    pattern, text = read_input()
    rkp = RabinKarp(pattern, text)
    print_occurrences(rkp.find_occurrences())
