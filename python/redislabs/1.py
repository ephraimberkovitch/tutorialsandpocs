# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import math

def solution(A):
    N = len(A)
    maximums_for_left = [-2000000000] * (N-1)
    maximums_for_right = [-2000000000] * (N-1)
    max_part1 = -2000000000
    max_part2 = -2000000000
    K = 0
    while K<N-1:
        if A[K]>max_part1:
            max_part1 = A[K]
        maximums_for_left[K] = max_part1
        K += 1
    K = N-2
    while K>=0:
        if A[K+1]>max_part2:
            max_part2 = A[K]
        maximums_for_right[K] = max_part2
        K -= 1
    max_difference = 0
    for K in range(N-1):
        difference = int(math.fabs(maximums_for_left[K]-maximums_for_right[K]))
        if difference>max_difference:
            max_difference = difference
    return max_difference

print(solution([1,3,-3]))