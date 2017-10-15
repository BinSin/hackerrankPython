n = int(input())
arr = map(int, input().split())
# sorted : 정렬
# [order] : order번째 값 출력
# order를 이용하면 sort 후 원하는 값 출력할 때 편하다.
# 밑은 정렬 후 -2 이므로 두번째로 큰 값 출력
print(sorted(list(set(arr)))[-2])
