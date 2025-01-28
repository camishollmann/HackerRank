# Problem statement:
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    max_score = max(arr)
    runner_up = max([score for score in arr if score != max_score])
    print(runner_up)