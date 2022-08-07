def miniMaxSum(arr):
    # Write your code here
    lowest_number = arr[0]
    highest_number = 0
    sum = 0

    for i in range(len(arr)):
        current_number = arr[i]
        if current_number > highest_number:
            highest_number = current_number
        if current_number < lowest_number:
            lowest_number = current_number
        sum += current_number
    print(f'{sum - highest_number} {sum - lowest_number}')