import random

class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0
    
    def place_ship(self, ship, start_row, start_col, direction, board):
        positions = []
        if direction == 'H':
            if start_col + self.size > len(board[0]):
                return False
            for i in range(self.size):
                if board[start_row][start_col + i] != ' ':
                    return False
                positions.append((start_row, start_col))
        elif direction == 'V':
            if start_row + self.size > len(board):
                return False
            for i in range(self.size):
                if board[start_row + i][start_col] != ' ':
                    return False
                positions.append((start_row + i, start_col))
        else:
            return False
        
        for pos in positions:
            board[pos[0]][pos[1]] = self.name[0]
        self.positions = positions

    def is_destroyed(self):
        self.hits += 1
        return self.hits == self.size

class Destroyer(Ship):
    def __init__(self):
        super().__init__('Destructor', 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__('Submarino', 3)

class Battleship(Ship):
    def __init__(self):
        super().__init__('Acorazado', 4)

class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.hits = [[' ' for _ in range(10)] for _ in range(10)]

    def place_ships(self):
        ships = [Destroyer(), Submarine(), Battleship()]

        for ship in ships:
            while True:
                print("        Coloca tu {} (Tamaño = {}) en el tablero de 10x10".format(ship.name, ship.size))

                start_col = int(input("            Coordenada inicial [X]: "))
                start_row = int(input("            Coordenada inicial [Y]: "))
                direction = input("            Dirección (H = Horizontal / V = Vertical): ").upper()

                if ship.place_ship(start_row, start_col, direction, self.board):
                    self.ships.append(ship)
                    self.print_board(self.board)
                    break
                else:
                    print("Posición no válida. Inténtalao de nuevo.")
    
    def print_board(self, board):
        for row in board:
            print(" ".join(row))
        print()
    
    def attack(self, opponent):
        while True:
            print("{}, elige una posición para atacar. ".format(self.name))
            row = int(("  · {}, Coordenada Y: "))
            col = int(("  · {}, Coordenada X: "))
            if 10 > col >= 0 and 10 > row >= 0:
                if opponent.board[row][col] == ' ':
                    print("Agua...")
                    self.hits[row][col] = 'A'
                    opponent.board[row][col] = 'A'
                    break
                elif opponent.board[row][col] != 'A':
                    print("¡Tocado!")
                    self.hits[row][col] = 'T'
                    for ship in opponent.ships:
                        if (row, col) in ship.positions:
                            if ship.is_destroyed():
                                print("¡Tocado y hundido!¡Te has cargado el {} del {}!".format(ship.name, opponent.name))
                            break
                    opponent.board[row][col] = 'T'
                    break
                else:
                    print("Ya has atacado esta posición. Inténtalo de nuevo.")
            else:
                print("Posición de ataque no válida. Inténtalo de nuevo.")
    
    def all_ships_sunk(self):
        return all(ship.hits == ship.size for ship in self.ships)

class BattleshipGame:
    def __init__(self):
        self.player1 = Player('JUGADOR 1')
        self.player2 = Player('JUGADOR 2')
    
    def play(self):
        print('''--------------------------------------------------------------
Bienvenido al juego de hundir la flota
--------------------------------------------------------------''')
        print("    {} coloca tus barcos:".format(self.player1.name))
        self.player1.place_ships()
        self.player2.place_ships()

        which_player_starts = random.shuffle([self.player1, self.player2])

        current_player = which_player_starts[0]
        opponent = which_player_starts[1]

        while True:
            current_player.attack(opponent)
            if opponent.all_ships_sunk():
                print("¡El {} ha ganado la partida !".format())
                break
            current_player, opponent = opponent, current_player

# Crea un instancia del juego e inicializalo
game = BattleshipGame()
game.play()
    
            



