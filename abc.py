import sys

H, M = map(int, sys.stdin.readline().split())
P = int(sys.stdin.readline())
print((H + (M + P) // 60) % 24, (M + P) % 60)
