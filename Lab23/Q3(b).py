# 1. Read the file and create a 2D list

grid = []

with open("stringmatrix.dat", "r") as file:

    for line in file:
        row = line.split()
        grid.append(row)

print("2D Matrix:")
print(grid)


# 2. Find number of rows and columns

rows = len(grid)
columns = len(grid[0])

print("\nNumber of Rows:", rows)
print("Number of Columns:", columns)


# 3. Print columns as lists

column_list = []

for j in range(columns):

    col = []

    for i in range(rows):
        col.append(grid[i][j])

    column_list.append(col)

print("\nColumns:")
print(column_list)


# 4. Print diagonal elements in one direction

diagonals = []

for k in range(rows + columns - 1):

    diagonal = []

    for i in range(rows):

        j = k - i

        if j >= 0 and j < columns:
            diagonal.append(grid[i][j])

    diagonals.append(diagonal)

print("\nDiagonal Elements:")
print(diagonals)