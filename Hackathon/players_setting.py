def create_player(name):  # Создаем игрока с заданным
    # именем и начальными параметрами
    player = {'name': name, 'lives': 0, 'points': 0}
    return player


def set_difficulty(difficulty):  # Устонавливаем количесво жизней в
    # зависимости от сложности игры
    if difficulty == 'easy_words':
        return 5

    if difficulty == 'normal_words':
        return 3

    if difficulty == 'hard_words':
        return 1
    else:
        return 0


def initialize_game():  # Инициализирует игру, создавая двух
    # игроков и устанавливая количество жизней.
    # Возвращает список с двумя словарями.
    player_one_name = input('Введите имя первого игрока: ')
    player_two_name = input('Введите имя второго игрока: ')

    player_one = create_player(player_one_name)
    player_two = create_player(player_two_name)

    difficulty = input('Выберите сложность игры: ')
    lives = set_difficulty(difficulty)

    player_one['lives'] = lives
    player_two['lives'] = lives

    player_list = [player_one, player_two]

    return player_list


game_players = initialize_game()
print('Список игроков: ')
for players in game_players:
    print(players)
