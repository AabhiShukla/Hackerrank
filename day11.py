def hourglass_sum(arr, row, col):
  sum = 0
  sum += arr[row][col] + arr[row][col+1] + arr[row][col+2]
  sum += arr[row+1][col+1]
  sum += arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
  return sum

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
    
max_hourglass_sum= -9 * 36
for row in range(0, 4):
    for col in range(0, 4):
      current_hourglass_sum = hourglass_sum(arr, row, col)
      if max_hourglass_sum < current_hourglass_sum:
          max_hourglass_sum = current_hourglass_sum

print (max_hourglass_sum)
