def dot_product(a,b):
    if len(a)!=len(b):
        print("Size of both vector should be same")
        return None
    else:
        result=0
        for i in range(len(a)):
            result += a[i]*b[i]
        return result

def matrix_vector(A, v):

    if len(A[0]) != len(v):
        print("Matrix columns and vector size should be same")
        return None

    result = []
    for i in range(len(A)):
        total = 0
        for j in range(len(v)):
            total += A[i][j] * v[j]
        result.append(total)
    return result

def matrix_matrix(A, B):
    if len(A[0]) != len(B):
        print("Size mismatch")
        return None

    result = []
    for i in range(len(A)):
        row = []

        for j in range(len(B[0])):
            total = 0

            for k in range(len(B)):
                total += A[i][k] * B[k][j]

            row.append(total)
        result.append(row)
    return result

def cross_product(a, b):

    if len(a) != 3 or len(b) != 3:
        print("Both vectors must have 3 elements")
        return None

    result = [a[1]*b[2] - a[2]*b[1],
              a[2]*b[0] - a[0]*b[2],
              a[0]*b[1] - a[1]*b[0]]
    return result