def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            try:
                element = int(input(f"Enter element for row {i + 1}, column {j + 1}: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                return None
            row.append(element)
        matrix.append(row)
    return matrix


def calculate_determinant(matrix):
    # The function takes a square matrix matrix as input

    n = len(matrix)
    # It first determines the size of the matrix by obtaining the length of the matrix list

    if n == 1:
        # Base cases
        return matrix[0][0]
    # elif n == 2:
    #     return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0

    # Laplace expansion
    # The function creates a submatrix by removing the first row and the corresponding column
    for j in range(n):
        submatrix = []
        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    row.append(matrix[i][k])
            submatrix.append(row)
        # Calculate the determinant of the submatrix.
        subdet = calculate_determinant(submatrix)
        # The results from all columns are summed up to obtain the determinant of the original matrix.
        det += (-1) ** j * matrix[0][j] * subdet

    return det


def main():
    n = 0
    while n <= 0:
        try:
            n = int(input("Enter the size of the matrix: "))
            if n <= 0:
                print("Invalid size. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    matrix = create_matrix(n)

    if matrix is not None:
        determinant = calculate_determinant(matrix)

        print("Matrix:")
        for row in matrix:
            print(row)

        print("Determinant:", determinant)


if __name__ == "__main__":
    main()
