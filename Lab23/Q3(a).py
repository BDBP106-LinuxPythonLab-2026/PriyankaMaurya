# Create a string matrix file

with open("stringmatrix.dat", "w") as file:

    for i in range(3):
        for j in range(4):
            letter = chr(65 + i * 4 + j)
            file.write(letter + " ")

        file.write("\n")

print("File created successfully!")