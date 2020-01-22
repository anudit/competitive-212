# arr=[]
# rows = int(input())
# while (rows):
#     arr.append(list(map(int,input().split())))
#     rows-=1

arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
a = arr
ending_row = len(arr)
ending_col = len(arr[0])

starting_row = 0; starting_col = 0

while (starting_row < ending_row and starting_col < ending_col) :

    for i in range(starting_col, ending_col) :
        print(a[starting_row][i], end = " ")

    starting_row += 1

    for i in range(starting_row, ending_row) :
        print(a[i][ending_col - 1], end = " ")

    ending_col -= 1

    if (starting_row < ending_row) :

        for i in range(ending_col - 1, (starting_col - 1), -1) :
            print(a[ending_row - 1][i], end = " ")

        ending_row -= 1

    if (starting_col < ending_col) :
        for i in range(ending_row - 1, starting_row - 1, -1) :
            print(a[i][starting_col], end = " ")

        starting_col += 1
