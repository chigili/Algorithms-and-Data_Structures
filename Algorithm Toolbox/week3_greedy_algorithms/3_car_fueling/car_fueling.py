class Solution:
    def minRefills(self, S, N, reach):
        stops = 0
        left = 0

        while left < N - 1:
            right = left
            while right + 1 < N and S[right + 1] - S[left] <= reach:
                right += 1
            if right == left:
                return -1
            stops += 1 if right < N - 1 else 0
            left = right
        return stops


if __name__ == "__main__":
    target = int(input())
    reach = int(input())
    N = int(input()) + 2  # +1 for the beginning stop and +1 for the target stop
    stops = [0]
    stops.extend(map(int, input().split()))
    stops.append(target)
    solution = Solution()
    ans = solution.minRefills(stops, N, reach)
    print(ans)
