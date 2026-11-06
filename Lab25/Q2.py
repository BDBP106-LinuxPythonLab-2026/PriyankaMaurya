import time

# Custom decorator for measuring matrix multiplication time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\n[Timer] Matrix multiplication completed in {end_time - start_time:.6f} seconds.")
        return result
    return wrapper


class LinearAlgebra:
    def __init__(self, A=None, B=None):
        self._A = A if A is not None else []
        self._B = B if B is not None else []

    # Getter property for matrices A and B
    @property
    def matrices(self):
        return self._A, self._B

    # Setter property to update matrices A and B
    @matrices.setter
    def matrices(self, matrices_tuple):
        new_A, new_B = matrices_tuple
        self._A = new_A
        self._B = new_B

    # Instance method for matrix multiplication with timing decorator
    @timing_decorator
    def multiply(self):
        if not self._A or not self._B:
            raise ValueError("Matrices A and B must not be empty.")

        rows_A = len(self._A)
        cols_A = len(self._A[0])
        rows_B = len(self._B)
        cols_B = len(self._B[0])

        # Validate dimensions for matrix multiplication
        if cols_A != rows_B:
            raise ValueError(
                f"Cannot multiply: Columns of Matrix A ({cols_A}) must match Rows of Matrix B ({rows_B})."
            )

        # Initialize result matrix with zeros (dimensions: rows_A x cols_B)
        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

        # Perform matrix multiplication using nested loops
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += self._A[i][k] * self._B[k][j]

        return result


# Helper function to get matrix input from the user
def input_matrix(matrix_name):
    print(f"\n--- Enter details for Matrix {matrix_name} ---")
    rows = int(input(f"Enter number of rows for {matrix_name}: "))
    cols = int(input(f"Enter number of columns for {matrix_name}: "))

    matrix = []
    print(f"Enter elements for Matrix {matrix_name} row by row (space-separated):")
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError(f"Expected {cols} elements, but got {len(row)}.")
        matrix.append(row)

    return matrix