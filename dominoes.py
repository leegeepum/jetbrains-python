import random


def create_set():
    return [[i, j] for i in range(7) for j in range(i, 7)]


def set_split(composition):
    random.shuffle(composition)
    stock = composition[:14]
    comp = composition[14:21]
    user = composition[21:28]
    return stock, comp, user


def starting():
    domino_set = create_set()
    while True:
        stock, comp_set, user_set = set_split(domino_set)
        if double_set(comp_set) or double_set(user_set):
            break
    comp_max = max(comp_set)
    user_max = max(user_set)
    if snake(comp_max, user_max) == 'comp':
        domino_snake = [comp_max]
        status = 'player'
        comp_set.remove(comp_max)
    else:
        domino_snake = [user_max]
        status = 'computer'
        user_set.remove(user_max)
    return stock, comp_set, user_set, domino_snake, status


def snake(comp, user):
    if sum(comp) > sum(user):
        return 'comp'
    else:
        return 'user'


def double_set(composition):
    for i in composition:
        if len(set(i)) == 1:
            return True


def show_your_pieces(your_pieces):
    print("\nYour pieces:", len(your_pieces))
    for i, piece in enumerate(your_pieces):
        print(f"{i+1}:{piece}")


def get_move(user_pieces, comp_pieces, stock, snake, who):
    pieces = user_pieces if who == 'user' else comp_pieces
    if who == 'user':
        while True:
            num = input()
            if (num.startswith('-') and len(num) == 2 and num[1:].isdigit() or num.isdigit()) and -len(pieces) <= int(num) <= len(pieces):
                if int(num) == 0 or checking_move(int(num), snake, pieces):
                    break
                else:
                    print("Illegal move. Please try again.")
            else:
                print("Invalid input. Please try again.")
    elif who == 'comp':
        while True:
            num = random.randint(-len(pieces), len(pieces))
            if len(stock) != 0 and num == 0 or num != 0 and checking_move(num, snake, pieces):
                break
    num = int(num)
    if num != 0:
        domino = pieces.pop(abs(num) - 1)
        snake = correct_place(num, snake, domino)
    else:
        if len(stock) != 0:
            pieces.append(stock.pop(random.randrange(0, len(stock))))
    user_pieces = pieces if who == 'user' else user_pieces
    comp_pieces = pieces if who == 'comp' else comp_pieces
    return user_pieces, comp_pieces, stock, snake


def checking_move(num, snake, pieces):
    snake = snake[-1][-1] if num > 0 else snake[0][0]
    if snake in pieces[abs(num) - 1]:
        return True
    else:
        return False


def correct_place(num, snake, domino):
    snake_num = snake[-1][-1] if num > 0 else snake[0][0]
    domino_num = domino[0] if num > 0 else domino[-1]
    if snake_num != domino_num:
        domino.reverse()
    if num > 0:
        snake.append(domino)
    else:
        snake.insert(0, domino)
    return snake


def show_state():
    global stock_pieces
    global computer_pieces
    global user_pieces
    global domino_snake
    global who
    global state
    print('=' * 70)
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}")
    print(f"\n{str(domino_snake)[1:-1].replace('], [', '][')}" if len(domino_snake) <= 6
          else f"\n{str(domino_snake[:3])[1:-1].replace('], [', '][')}...\
{str(domino_snake[-3:])[1:-1].replace('], [', '][')}")
    show_your_pieces(user_pieces)
    if game_status() == "user won":
        state = "The game is over. You won!"
    elif game_status() == "comp won":
        state = "The game is over. The computer won!"
    elif game_status() == 'draw':
        state = "The game is over. It's a draw!"
    elif who == "user":
        state = "It's your turn to make a move. Enter your command."
    elif who == "comp":
        state = "Computer is about to make a move. Press Enter to continue..."
    print(f"\nStatus: {state}")


def game_status():
    if len(user_pieces) == 0 or len(computer_pieces) == 0:
        if len(user_pieces) == 0:
            status = "user won"
            return status
        elif len(computer_pieces) == 0:
            status = "comp won"
            return status
    elif len(domino_snake) != 0 and domino_snake[0][0] == domino_snake[-1][1] and str(domino_snake).count(str(domino_snake[0][0])) == 8:
        return 'draw'
    else:
        return False


stock_pieces, computer_pieces, user_pieces, domino_snake, status = starting()
players = ('user', 'comp') if status == 'player' else ('comp', 'user')
while True:
    for who in players:
        show_state()
        if game_status():
            exit()
        if who == 'comp':
            input()
        user_pieces, computer_pieces, stock_pieces, domino_snake = get_move(user_pieces, computer_pieces, stock_pieces, domino_snake, who)
