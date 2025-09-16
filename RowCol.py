# Python_HW1


rows = int(input("Enter row: "))
cols = int(input("Enter col: "))


matrix = []
for i in range(rows):
    row_data = []
    print(f"Row {i+1}")
    for j in range(cols):
        num = float(input(f"Enter number{j+1}: "))
        row_data.append(num)
    matrix.append(row_data)


print("\nThe numbers are:")
for row in matrix:
    print(" ".join(str(x) for x in row))


search_num = float(input("\nSearch: "))


found_positions = []
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == search_num:
            found_positions.append((i, j))  # tuple of (row, col)

if found_positions:
    print(f"\nNumber {search_num} found at:")
    for pos in found_positions:
        print(f"Row {pos[0]}, Col {pos[1]}")
else:
    print(f"\nNumber {search_num} not found.")