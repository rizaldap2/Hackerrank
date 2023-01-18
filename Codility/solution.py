# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A = sorted(set(A))
    for i in range (1,100000):
        if i not in A:
            return i
