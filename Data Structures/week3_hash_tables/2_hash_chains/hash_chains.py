# python3

from collections import deque


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == "check":
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [deque() for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_chain(self, chain):
        print(" ".join(chain))

    def write_search_result(self, was_found):
        print("yes" if was_found else "no")

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            if self.elems[query.ind]:
                self.write_chain(self.elems[query.ind])
        else:
            hash_value = self._hash_func(query.s)
            if query.type == "add":
                if query.s not in self.elems[hash_value]:
                    self.elems[hash_value].appendleft(query.s)
            elif query.type == "del":
                if query.s in self.elems[hash_value]:
                    self.elems[hash_value].remove(query.s)
            elif query.type == "find":
                self.write_search_result(query.s in self.elems[hash_value])

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == "__main__":
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
