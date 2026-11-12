N, M = map(int, input().split())
arr = []
min_num_in_row = 1

for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    if min(row) > min_num_in_row:
        min_num_in_row = min(row)
        tar_idx = i
    
print(min(arr[tar_idx]))