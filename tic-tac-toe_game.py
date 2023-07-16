# ---------< Креcтики-нолики >---------
# Создание игрового поля
game_board = [['-' for _ in range(3)] for _ in range(3)]

# Печать игрового поля в консоль
def print_game_board():
    print('  0 1 2')
    for i in range(3):
        print(i, ' '.join(game_board[i]))

# Функция для осуществления хода
def make_move(player):
    while True:
        row = int(input('Введите номер строки от 0 до 2: '))
        col = int(input('Введите номер столбца от 0 до 2: '))
        if (row and col) in range(3) and game_board[row][col] == '-':
            game_board[row][col] = player
            break
        else:
            print('Некорректный ход! Попробуйте снова.')

# Основная функция игры
def play_game():
    current_player = 'X'
    print('Начинаем игру в Крестики-нолики!')
    print_game_board()
    for _ in range(9):
        print(f'Ход игрока {current_player}:')
        make_move(current_player)
        print_game_board()
        # Проверка на победу
        if winner(current_player):
            print(f'Победил игрок {current_player}!')
            return
        # Переключение игроков
        current_player = 'O' if current_player == 'X' else 'X'
    print('Ничья!')

# Проверка на победу
def winner(player):
    b = game_board
    # Проверка по диагоналям
    if b[0][0] == b[1][1] == b[2][2] == player or b[2][0] == b[1][1] == b[0][2] == player:
        return True
    # Проверка по строкам и столбцам
    for i in range(3):
        if b[0][i] == b[1][i] == b[2][i] == player or b[i][0] == b[i][1] == b[i][2] == player:
            return True
    return False

# Запуск игры
play_game()