matrix = [[' ' for i in range(3)] for i in range(3)]
ex_and_oh = ['X', 'O'] * 5
count = 0
matrix_for_print = f"""---------
| {' '.join(matrix[0])} |
| {' '.join(matrix[1])} |
| {' '.join(matrix[2])} |
---------"""
print(matrix_for_print)
play_game = True
while any([i for m in matrix for i in m if i == ' ']):

    coord_input = input('Enter the coordinates: ').split()

    # error if letter
    if len(coord_input[0]) > 2:
        print('You should enter numbers!')

    elif any([coord for coord in coord_input if coord not in ['1', '2', '3']]):
        print('Coordinates should be from 1 to 3!')

    else:
        # error if occupied
        if matrix[int(coord_input[0]) - 1][int(coord_input[1]) - 1] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            # add x and o to the coord
            matrix[int(coord_input[0]) - 1][int(coord_input[1]) - 1] = ex_and_oh[count]
            # switch x and o
            count += 1
            matrix_for_print = f"""---------
| {' '.join(matrix[0])} |
| {' '.join(matrix[1])} |
| {' '.join(matrix[2])} |
---------"""
            print(matrix_for_print)
            # stop if 3 is consecutive
            if matrix[0] == ['X', 'X', 'X'] or \
                    matrix[1] == ['X', 'X', 'X'] or \
                    matrix[2] == ['X', 'X', 'X'] or \
                    (matrix[0][0] == 'X' and matrix[1][0] == 'X' and matrix[2][0] == 'X') or \
                    (matrix[0][1] == 'X' and matrix[1][1] == 'X' and matrix[2][1] == 'X') or \
                    (matrix[0][2] == 'X' and matrix[1][2] == 'X' and matrix[2][2] == 'X') or \
                    (matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X') or \
                    (matrix[0][2] == 'X' and matrix[1][1] == 'X' and matrix[2][0] == 'X'):
                print('X wins')
                break
            elif matrix[0] == ['O', 'O', 'O'] or \
                    matrix[1] == ['O', 'O', 'O'] or \
                    matrix[2] == ['O', 'O', 'O'] or \
                    (matrix[0][0] == 'O' and matrix[1][0] == 'O' and matrix[2][0] == 'O') or \
                    (matrix[0][1] == 'O' and matrix[1][1] == 'O' and matrix[2][1] == 'O') or \
                    (matrix[0][2] == 'O' and matrix[1][2] == 'O' and matrix[2][2] == 'O') or \
                    (matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == 'O') or \
                    (matrix[0][2] == 'O' and matrix[1][1] == 'O' and matrix[2][0] == 'O'):
                print('O wins')
                break
else:
    print('Draw')
