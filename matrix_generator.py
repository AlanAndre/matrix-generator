import numpy as np
running = True


def mult_const():
    print('Enter size matrix:')
    rows1, columns1 = map(int, input().split(' '))
    print('Enter matrix:')
    mat1 = np.array([input().split() for _ in range(rows1)], float)
    const = float(input('Enter constant:'))
    print('The result is:')
    for i in np.multiply(mat1, const):
        print(' '.join(map(str, i)))


def addition_matrices():
    print('Enter size of first matrix:')
    rows1, columns1 = map(int, input().split(' '))
    print('Enter first matrix:')
    mat1 = np.array([input().split() for _ in range(rows1)], float)
    print('Enter size of second matrix:')
    rows2, columns2 = map(int, input().split(' '))
    print('Enter second matrix:')
    mat2 = np.array([input().split() for _ in range(rows2)], float)

    if rows1 == rows2 and columns1 == columns2:
        print('The result is:')
        for i in np.add(mat1, mat2):
            print(' '.join(map(str, i)))
    else:
        print('The operation cannot be performed.')


def mult_matrices():
    print('Enter size of first matrix:')
    rows1, columns1 = map(int, input().split(' '))
    print('Enter first matrix:')
    mat1 = np.array([input().split() for _ in range(rows1)], float)
    print('Enter size of second matrix:')
    rows2, columns2 = map(int, input().split(' '))
    print('Enter second matrix:')
    mat2 = np.array([input().split() for _ in range(rows2)], float)

    if columns1 == rows2:
        print('The result is:')
        for i in np.matmul(mat1, mat2):
            print(' '.join(map(str, i)))
    else:
        print('The operation cannot be performed.')


def transpose_matrix():

    user_transpose_choice = input("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice:""")
    print('Enter size matrix:')
    rows1, columns1 = map(int, input().split(' '))
    print('Enter matrix:')
    mat1 = np.array([input().split() for _ in range(rows1)], float)
    trans_matrix = mat1
    if user_transpose_choice == '1':
        trans_matrix = mat1.transpose()
    elif user_transpose_choice == '2':
        trans_matrix = np.rot90(mat1, -1)
        trans_matrix = np.flip(trans_matrix, 0)
    elif user_transpose_choice == '3':
        trans_matrix = np.flip(mat1, 1)
    elif user_transpose_choice == '4':
        trans_matrix = np.flip(mat1, 0)
    print('The result is:')
    for i in trans_matrix:
        print(' '.join(map(str, i)))


def determinant():
    print('Enter matrix size:')
    rows1, columns1 = map(int, input().split(' '))
    print('Enter matrix:')
    mat1 = np.array([input().split() for _ in range(rows1)], float)
    if rows1 == columns1:
        print(np.linalg.det(mat1))
    else:
        print('The matrix must be square!')


def inverse():
    print('Enter matrix size:')
    rows1, columns1 = map(int, input().split(' '))
    print('Enter matrix:')
    mat1 = np.array([input().split() for _ in range(rows1)], float)
    print('The result is')
    for i in np.linalg.inv(mat1):
        print(' '.join(map(str, i)))
    print()


def menu():
    global running
    users_choice = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice:""")
    if users_choice == '1':
        addition_matrices()
    elif users_choice == '2':
        mult_const()
    elif users_choice == '3':
        mult_matrices()
    elif users_choice == '4':
        transpose_matrix()
    elif users_choice == '5':
        determinant()
    elif users_choice == '6':
        inverse()
    elif users_choice == '0':
        running = False


while running:
    menu()
