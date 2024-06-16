import random
import os

def generate_matrix(rows, columns):
    matrix = [[random.randint(0, 1) for _ in range(columns)] for _ in range(rows)]
    return matrix

def matrix_to_string(matrix):
    return ''.join(str(cell) for row in matrix for cell in row)

def write_to_file(directory, filename, matrices):
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        for rows, columns, matrix in matrices:
            matrix_str = matrix_to_string(matrix)
            file.write(f"{rows}x{columns}:{matrix_str}\n")

def generate_matrices(num_matrices, num_duplicates):
    matrices = []
    unique_matrices = set()

    while len(unique_matrices) < (num_matrices - num_duplicates):
        rows = random.randint(5, 10)
        columns = random.randint(5, 10)
        matrix = generate_matrix(rows, columns)
        matrix_str = matrix_to_string(matrix)
        unique_matrices.add((rows, columns, matrix_str))

    unique_matrices = list(unique_matrices)

    for rows, columns, matrix_str in unique_matrices:
        matrix = [[int(matrix_str[i * columns + j]) for j in range(columns)] for i in range(rows)]
        matrices.append((rows, columns, matrix))

    for _ in range(num_duplicates):
        rows, columns, matrix_str = random.choice(unique_matrices)
        matrix = [[int(matrix_str[i * columns + j]) for j in range(columns)] for i in range(rows)]
        matrices.append((rows, columns, matrix))

    random.shuffle(matrices)

    return matrices

def main():
    input_directory = "/mnt/input"
    matrices_per_file = 110000
    num_duplicates = 70000

    for i in range(150):
        matrices = generate_matrices(matrices_per_file, num_duplicates)
        filename = f"mat{i+1}.in"
        write_to_file(input_directory, filename, matrices)

if __name__ == "__main__":
    main()