from copy import deepcopy

# Author: Benjamin Warren
# Date: 2/28/2021
# Description: The game of Janggi in python!


class Piece:
    """
    Parent class for all pieces, establishes data needed for all pieces which will inherit
    """

    def __init__(self, color, name):
        """
        Init for color and name
        :param color: Team color of piece
        :param name: Name of piece for board display
        """
        self.color = color
        self.name = name

    def set_name(self, name):
        """
        Setter for name
        :param name: Name to be set
        :return: None
        """
        self.name = name

    def set_color(self, color):
        """
        Setter for team color
        :param color: Color of team piece is on
        :return: None
        """
        self.color = color

    def get_color(self):
        """
        Getter for color
        :return: Color of current piece
        """
        return self.color

    def get_name(self):
        """
        Getter for name
        :return: Name of current piece
        """
        return self.name


class Chariot(Piece):
    """
    Chariot class to establish a chariot
    Parent: Piece
    """

    def __init(self, color, name):
        """
        Initializes color and name of chariot using inheritance
        :param color: Team color of chariot
        :param name: Name for board display
        :return: None
        """
        super().__init__(color, name)

    @staticmethod
    def available_move(moveFrom, moveTo, board):
        """
        Static method, validates whether a move for a chariot piece is viable
        :param moveFrom: Location on board to move from
        :param moveTo: Location on board to move to
        :param board: Pass board to check if theres any other conditionals like a piece in the way
        :return: Boolean value of whether move is a valid move
        """
        y1 = moveFrom[0]
        x1 = moveFrom[1:]
        y = moveTo[0]
        x = moveTo[1:]
        if x == x1 and ord(y1) < ord(y):
            loop = True
            count = 0
            block = False
            while loop is True:
                count += 1
                if count + ord(y1) > ord(y):
                    return True
                else:
                    pos = (chr(ord(y1) + count) + str(int(x1)))
                    if type(board.get_piece(pos)) is not PalaceSquare:
                        if type(board.get_piece(pos)) is not EmptySquare:
                            block = True
                if block is True:
                    return False
        elif x == x1 and ord(y1) > ord(y):
            loop = True
            count = 0
            block = False
            while loop is True:
                count -= 1
                if count + ord(y1) < ord(y):
                    return True
                else:
                    pos = (chr(ord(y1) + count) + str(int(x1)))
                    if type(board.get_piece(pos)) is not PalaceSquare:
                        if type(board.get_piece(pos)) is not EmptySquare:
                            block = True
                if block is True:
                    return False
        elif y == y1 and int(x1) < int(x):
            loop = True
            count = 0
            block = False
            while loop is True:
                count += 1
                if count + int(x1) > int(x):
                    return True
                else:
                    pos = (chr(ord(y1)) + str(int(x1) + count))
                    if type(board.get_piece(pos)) is not PalaceSquare:
                        if type(board.get_piece(pos)) is not EmptySquare:
                            block = True
                if block is True:
                    return False
        elif y == y1 and int(x1) > int(x):
            loop = True
            count = 0
            block = False
            while loop is True:
                count -= 1
                if count + int(x1) < int(x):
                    return True
                else:
                    pos = (chr(ord(y1)) + str(int(x1) + count))
                    if type(board.get_piece(pos)) is not PalaceSquare:
                        if type(board.get_piece(pos)) is not EmptySquare:
                            block = True
                if block is True:
                    return False
        elif type(board.get_piece(moveTo)) is PalaceSquare:
            if type(board.get_piece(moveFrom) is PalaceSquare):
                if int(x) == int(x1) + 1 or int(x) == int(x1) - 1:
                    if ord(y) == ord(y1) + 1:
                        return True
                    elif ord(y) == ord(y1) - 1:
                        return True
                elif int(x) == int(x1) + 2 or int(x) == int(x1) - 2:
                    if ord(y) == ord(y1) + 2:
                        return True
                    elif ord(y) == ord(y1) - 2:
                        return True
        else:
            return False


class Elephant(Piece):
    """
    Elephant class to establish an elephant
    Parent: Piece
    """

    def __init(self, color, name):
        """
        Initializes color and name of elephant using inheritance
        :param color: Team color of elephant
        :param name: Name for board display
        :return: None
        """
        super().__init__(color, name)

    @staticmethod
    def available_move(moveFrom, moveTo, board):
        """
        Static method, validates whether a move for a elephant piece is viable
        :param moveFrom: Location on board to move from
        :param moveTo: Location on board to move to
        :param board: Pass board to check if theres any other conditionals like a piece in the way
        :return: Boolean value of whether move is a valid move
        """
        y1 = moveFrom[0]
        x1 = moveFrom[1:]
        y = moveTo[0]
        x = moveTo[1:]
        if int(x) == int(x1) + 3 and ord(y) == ord(y1) + 2:
            pos = (chr(ord(y1)) + str(int(x1) + 1))
            if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                pos = (chr(ord(y1) + 1) + str(int(x1) + 2))
                if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                    return True
        elif int(x) == int(x1) + 3 and ord(y) == ord(y1) - 2:
            pos = (chr(ord(y1)) + str(int(x1) + 1))
            if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                pos = (chr(ord(y1) - 1) + str(int(x1) + 2))
                if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                    return True
        elif int(x) == int(x1) - 3 and ord(y) == ord(y1) + 2:
            pos = (chr(ord(y1)) + str(int(x1) - 1))
            if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                pos = (chr(ord(y1) + 1) + str(int(x1) - 2))
                if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                    return True
        elif int(x) == int(x1) - 3 and ord(y) == ord(y1) - 2:
            pos = (chr(ord(y1)) + str(int(x1) - 1))
            if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                pos = (chr(ord(y1) - 1) +str(int(x1) - 2))
                if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                    return True
        elif int(x) == int(x1) + 2 and ord(y) == ord(y1) + 3:
            pos = (chr(ord(y1) + 1) + str(int(x1)))
            if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                pos = (chr(ord(y1) + 2) + str(int(x1) + 1))
                if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                    return True
        elif int(x) == int(x1) - 2 and ord(y) == ord(y1) + 3:
            pos = (chr(ord(y1) + 1) + str(int(x1)))
            if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                pos = (chr(ord(y1) + 2) + str(int(x1) - 1))
                if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                    return True
        elif int(x) == int(x1) + 2 and ord(y) == ord(y1) - 3:
            pos = (chr(ord(y1) - 1) + str(int(x1)))
            if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                pos = (chr(ord(y1) - 2) + str(int(x1) + 1))
                if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                    return True
        elif int(x) == int(x1) - 2 and ord(y) == ord(y1) - 3:
            pos = (chr(ord(y1) - 1) + str(int(x1)))
            if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                pos = (chr(ord(y1) - 2) + str(int(x1) - 1))
                if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                    return True
        else:
            return False


class Horse(Piece):
    """
    Horse class to establish a horse
    Parent: Piece
    """

    def __init(self, color, name):
        """
        Initializes color and name of horse using inheritance
        :param color: Team color of horse
        :param name: Name for board display
        :return: None
        """
        super().__init__(color, name)

    @staticmethod
    def available_move(moveFrom, moveTo, board):
        """
        Static method, validates whether a move for a horse piece is viable
        :param moveFrom: Location on board to move from
        :param moveTo: Location on board to move to
        :param board: Pass board to check if theres any other conditionals like a piece in the way
        :return: Boolean value of whether move is a valid move
        """
        y1 = moveFrom[0]
        x1 = moveFrom[1:]
        y = moveTo[0]
        x = moveTo[1:]
        if (int(x) == int(x1) + 2 and ord(y) == ord(y1) + 1) or (int(x) == int(x1) + 2 and ord(y) == ord(y1) - 1):
            pos = (chr(ord(y1)) + str(int(x1) + 1))
            if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                return True
        elif (int(x) == int(x1) - 2 and ord(y) == ord(y1) + 1) or (int(x) == int(x1) - 2 and ord(y) == ord(y1) - 1):
            pos = (chr(ord(y1)) + str(int(x1) - 1))
            if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                return True
        elif (int(x) == int(x1) + 1 and ord(y) == ord(y1) + 2) or (int(x) == int(x1) - 1 and ord(y) == ord(y1) + 2):
            pos = (chr(ord(y1) + 1) + str(int(x1)))
            if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                return True
        elif (int(x) == int(x1) - 1 and ord(y) == ord(y1) - 2) or (int(x) == int(x1) + 1 and ord(y) == ord(y1) - 2):
            pos = (chr(ord(y1) - 1) + str(int(x1)))
            if type(board.get_piece(pos)) is EmptySquare or type(board.get_piece(pos)) is PalaceSquare:
                return True
        else:
            return False


class Guard(Piece):
    """
    Guard class to establish a Guard
    Parent: Piece
    """

    def __init(self, color, name):
        """
        Initializes color and name of guard using inheritance
        :param color: Team color of guard
        :param name: Name for board display
        :return: None
        """
        super().__init__(color, name)

    @staticmethod
    def available_move(moveFrom, moveTo, board):
        """
        Static method, validates whether a move for a general piece is viable
        :param moveFrom: Location on board to move from
        :param moveTo: Location on board to move to
        :param board: Pass board to check if theres any other conditionals like a piece in the way
        :return: Boolean value of whether move is a valid move
        """
        y1 = moveFrom[0]
        x1 = moveFrom[1:]
        y = moveTo[0]
        x = moveTo[1:]
        if type(board.get_piece(moveTo)) is PalaceSquare:
            if int(x) == int(x1) + 1 or int(x) == int(x1) - 1:
                if ord(y) == ord(y1) + 1:
                    return True
                elif ord(y) == ord(y1) - 1:
                    return True
                elif y == y1:
                    return True
            if ord(y) == ord(y1) + 1 or ord(y) == ord(y1) - 1:
                if int(x) == int(x1) + 1:
                    return True
                elif int(x) == int(x1) - 1:
                    return True
                elif x == x1:
                    return True


class General(Piece):
    """
    General class to establish a general
    Parent: Piece
    """

    def __init(self, color, name):
        """
        Initializes color and name of general using inheritance
        :param color: Team color of general
        :param name: Name for board display
        :return: None
        """
        super().__init__(color, name)

    @staticmethod
    def available_move(moveFrom, moveTo, board):
        """
        Static method, validates whether a move for a general piece is viable
        :param moveFrom: Location on board to move from
        :param moveTo: Location on board to move to
        :param board: Pass board to check if theres any other conditionals like a piece in the way
        :return: Boolean value of whether move is a valid move
        """
        y1 = moveFrom[0]
        x1 = moveFrom[1:]
        y = moveTo[0]
        x = moveTo[1:]
        if type(board.get_piece(moveTo)) is PalaceSquare:
            if int(x) == int(x1) + 1 or int(x) == int(x1) - 1:
                if ord(y) == ord(y1) + 1:
                    return True
                elif ord(y) == ord(y1) - 1:
                    return True
                elif y == y1:
                    return True
            if ord(y) == ord(y1) + 1 or ord(y) == ord(y1) - 1:
                if int(x) == int(x1) + 1:
                    return True
                elif int(x) == int(x1) - 1:
                    return True
                elif x == x1:
                    return True


class Cannon(Piece):
    """
    Cannon class to establish a cannon
    Parent: Piece
    """

    def __init(self, color, name):
        """
        Initializes color and name of cannon using inheritance
        :param color: Team color of cannon
        :param name: Name for board display
        :return: None
        """
        super().__init__(color, name)

    @staticmethod
    def available_move(moveFrom, moveTo, board):
        """
        Static method, validates whether a move for a cannon piece is viable
        :param moveFrom: Location on board to move from
        :param moveTo: Location on board to move to
        :param board: Pass board to check if theres any other conditionals like a piece in the way
        :return: Boolean value of whether move is a valid move
        """
        y1 = moveFrom[0]
        x1 = moveFrom[1:]
        y = moveTo[0]
        x = moveTo[1:]
        if type(board.get_piece(moveTo)) is not Cannon:
            if y1 == y and int(x) > int(x1):
                loop = True
                count = 0
                jump = False
                block = False
                while loop is True:
                    count += 1
                    pos = (chr(ord(y1)) + str(int(x1) + count))
                    if int(x1) + count >= int(x):
                        loop  = False
                    else:
                        if jump is True:
                            if type(board.get_piece(pos)) is not EmptySquare:
                                if type(board.get_piece(pos)) is not PalaceSquare:
                                    block = True
                        elif type(board.get_piece(pos)) is not EmptySquare:
                            if type(board.get_piece(pos)) is not PalaceSquare:
                                if type(board.get_piece(pos)) is not Cannon:
                                    jump = True
                if jump is True:
                    if block is False:
                        return True
                else:
                    return False
            elif y1 == y and int(x) < int(x1):
                loop = True
                count = 0
                jump = False
                block = False
                while loop is True:
                    count -= 1
                    pos = (chr(ord(y1)) + str(int(x1) + count))
                    if int(x1) + count <= int(x):
                        loop = False
                    else:
                        if jump is True:
                            if type(board.get_piece(pos)) is not EmptySquare:
                                if type(board.get_piece(pos)) is not PalaceSquare:
                                    block = True
                        elif type(board.get_piece(pos)) is not EmptySquare:
                            if type(board.get_piece(pos)) is not PalaceSquare:
                                if type(board.get_piece(pos)) is not Cannon:
                                    jump = True
                if jump is True:
                    if block is False:
                        return True
                else:
                    return False
            elif x == x1 and ord(y) > ord(y1):
                loop = True
                count = 0
                jump = False
                block = False
                while loop is True:
                    count += 1
                    pos = (chr(ord(y1) + count) + str(int(x1)))
                    if ord(y1) + count >= ord(y):
                        loop = False
                    else:
                        if jump is True:
                            if type(board.get_piece(pos)) is not EmptySquare:
                                if type(board.get_piece(pos)) is not PalaceSquare:
                                    block = True
                        elif type(board.get_piece(pos)) is not EmptySquare:
                            if type(board.get_piece(pos)) is not PalaceSquare:
                                if type(board.get_piece(pos)) is not Cannon:
                                    jump = True
                if jump is True:
                    if block is False:
                        return True
                else:
                    return False
            elif x == x1 and ord(y) < ord(y1):
                loop = True
                count = 0
                jump = False
                block = False
                while loop is True:
                    count -= 1
                    pos = (chr(ord(y1) + count) + str(int(x1)))
                    if ord(y1) + count == ord(y):
                        loop = False
                    else:
                        if jump is True:
                            if type(board.get_piece(pos)) is not EmptySquare :
                                if type(board.get_piece(pos)) is not PalaceSquare:
                                    block = True
                        elif type(board.get_piece(pos)) is not EmptySquare:
                            if type(board.get_piece(pos)) is not PalaceSquare:
                                if type(board.get_piece(pos)) is not Cannon:
                                    jump = True
                if jump is True:
                    if block is False:
                        return True
                else:
                    return False
        else:
            return False


class Soldier(Piece):
    """
    Soldier class to establish a soldier
    Parent: Piece
    """

    def __init(self, color, name):
        """
        Initializes color and name of soldier using inheritance
        :param color: Team color of soldier
        :param name: Name for board display
        :return: None
        """
        super().__init__(color, name)

    @staticmethod
    def available_move(moveFrom, moveTo, board):
        """
        Static method, validates whether a move for a soldier piece is viable
        :param moveFrom: Location on board to move from
        :param moveTo: Location on board to move to
        :param board: Pass board to check if theres any other conditionals like a piece in the way
        :return: Boolean value of whether move is a valid move
        """
        if board.get_piece(moveFrom).get_color() == "red":
            y = moveFrom[0]
            x = moveFrom[1:]
            y1 = moveTo[0]
            x1 = moveTo[1:]
            if int(x1) == int(x) + 1:
                if y == y1:
                    return True
            elif ord(y1) == ord(y) + 1:
                if x == x1:
                    return True
            elif ord(y1) == ord(y) - 1:
                if x == x1:
                    return True
            elif type(board.get_piece(moveTo)) is PalaceSquare and type(board.get_piece(moveFrom)) is PalaceSquare:
                if int(x1) == int(x) - 1:
                    if ord(y1) == ord(y) + 1:
                        return True
                    elif ord(y1) == ord(y) - 1:
                        return True
            else:
                return False
        elif board.get_piece(moveFrom).get_color() == "blue":
            y = moveFrom[0]
            x = moveFrom[1:]
            y1 = moveTo[0]
            x1 = moveTo[1:]
            if int(x1) == int(x) - 1:
                if y == y1:
                    return True
            elif ord(y1) == ord(y) + 1:
                if x == x1:
                    return True
            elif ord(y1) == ord(y) - 1:
                if x == x1:
                    return True
            elif type(board.get_piece(moveTo)) is PalaceSquare and type(board.get_piece(moveFrom)) is PalaceSquare:
                if int(x1) == int(x) - 1:
                    if ord(y1) == ord(y) + 1:
                        return True
                    elif ord(y1) == ord(y) - 1:
                        return True
            else:
                return False


class EmptySquare(Piece):
    """
    Empty square class creates an empty square that's not a palace square on the board
    """

    def __init(self, color, name):
        """
        Initializes an empty square
        :param color: Will be given a None value assignment
        :param name: For display purposes, most likely "[     ]"
        :return: None
        """
        super().__init__(color, name)


class PalaceSquare(Piece):
    """
    Palace square class creates a palace square for either blue or red teams
    """

    def __init(self, color, name):
        """
        Initializes with a team color and name
        :param color: Either red or blue depending on side of board
        :param name: Most likely an "XXXXXX" or "000000" depending on team for display purposes
        :return:
        """
        super().__init__(color, name)


class Board:
    """
    Board class contains the game board and any relevant information on the current game board
    """

    def __init__(self):
        """
        Initializes board here using a dict layout, and whose turn starts the game
        """
        self.board = {}
        self.turn = "blue"
        for row in range(1, 11, 1):
            for col in range(ord('a'), ord('i') + 1):
                if (chr(col) + str(row)) in ('d1', 'd2', 'd3', 'e1', 'e2', 'e3', 'f1', 'f2', 'f3'):
                    self.board[chr(col) + str(row)] = PalaceSquare("red", "XXXXXXXXXXXX")
                elif (chr(col) + str(row)) in ('d8', 'd9', 'd10', 'e8', 'e9', 'e10', 'f8', 'f9', 'f10'):
                    self.board[chr(col) + str(row)] = PalaceSquare("blue", "000000000000")
                else:
                    ' Types that can go in self.board '
                    self.board[chr(col) + str(row)] = Soldier("red", "RedSoldier")
                    self.board[chr(col) + str(row)] = Elephant("red", "RedElephant")
                    self.board[chr(col) + str(row)] = Horse("red", "RedHorse")
                    self.board[chr(col) + str(row)] = Guard("red", "RedGuard")
                    self.board[chr(col) + str(row)] = Chariot("red", "RedChariot")
                    self.board[chr(col) + str(row)] = Cannon("red", "RedCannon")
                    self.board[chr(col) + str(row)] = General("red", "RedGeneral")
                    self.board[chr(col) + str(row)] = EmptySquare(None, "[          ]")

    def get_board(self):
        return self.board

    def start_game(self):
        """
        start_game function will modify start-up board, adding piece objects to their correct start position
        :return:None
        """

        for row in range(1, 11, 1):
            for col in range(ord('a'), ord('i') + 1):
                pos = (chr(col) + str(row))
                if pos in ('a4', 'c4', 'e4', 'g4', 'i4'):
                    self.board[pos] = Soldier("red", " RedSoldier ")
                elif pos in ('b1', 'g1'):
                    self.board[pos] = Elephant("red", "RedElephant ")
                elif pos in ('c1', 'h1'):
                    self.board[pos] = Horse("red", "  RedHorse  ")
                elif pos in ('d1', 'f1'):
                    self.board[pos] = Guard("red", "  RedGuard  ")
                elif pos in ('a1', 'i1'):
                    self.board[pos] = Chariot("red", " RedChariot ")
                elif pos in ('b3', 'h3'):
                    self.board[pos] = Cannon("red", "  RedCannon ")
                elif pos in 'e2':
                    self.board[pos] = General("red", " RedGeneral ")
                if pos in ('a7', 'c7', 'e7', 'g7', 'i7'):
                    self.board[pos] = Soldier("blue", "BlueSoldier ")
                elif pos in ('b10', 'g10'):
                    self.board[pos] = Elephant("blue", "BlueElephant")
                elif pos in ('c10', 'h10'):
                    self.board[pos] = Horse("blue", "  BlueHorse ")
                elif pos in ('d10', 'f10'):
                    self.board[pos] = Guard("blue", "  BlueGuard ")
                elif pos in ('a10', 'i10'):
                    self.board[pos] = Chariot("blue", "BlueChariot ")
                elif pos in ('b8', 'h8'):
                    self.board[pos] = Cannon("blue", " BlueCannon ")
                elif pos in 'e9':
                    self.board[pos] = General("blue", "BlueGeneral ")

    def update_board(self, moveFrom, moveTo, jGame):
        """
        Updates board calling piece validation method, and then updating if it passes validation
        :param moveFrom: Position to moveFrom (piece selection)
        :param moveTo: Position to move to
        :param jGame: Current running JanggiGame class object
        :return: Boolean on whether move is successful or not
        """
        if type(self.board[moveFrom]) == EmptySquare or type(self.board[moveFrom]) == PalaceSquare:
            return False
        if jGame.get_game_state() == "Unfinished":
            if not jGame.get_in_check(self.board[moveFrom].get_color()):
                for row in range(1, 11, 1):
                    for col in range(ord('a'), ord('i') + 1):
                        pos = (chr(col) + str(row))
                        if moveFrom in pos and self.turn == self.board[pos].get_color():
                            if not self.board[pos].available_move(moveFrom, moveTo, self):
                                return False
                            Temp = self.board[pos]
                            if pos in ('d1', 'd2', 'd3', 'e1', 'e2', 'e3', 'f1', 'f2', 'f3'):
                                self.board[pos] = PalaceSquare("red", "XXXXXXXXXXXX")
                            elif pos in ('d8', 'd9', 'd10', 'e8', 'e9', 'e10', 'f8', 'f9', 'f10'):
                                self.board[chr(col) + str(row)] = PalaceSquare("blue", "000000000000")
                            else:
                                self.board[pos] = EmptySquare(None, "[          ]")
                            for row2 in range(1, 11, 1):
                                for col2 in range(ord('a'), ord('i') + 1):
                                    pos = (chr(col2) + str(row2))
                                    if moveTo in pos:
                                        self.board[pos] = Temp
                                        self.set_turn()
                                        jGame.is_in_check(self.board[pos].get_color())
                                        if self.checkmate(self.board[pos].get_color()):
                                            if self.board[pos].get_color() == "red":
                                                jGame.set_game_sate("RED_WON")
                                            else:
                                                jGame.set_game_sate("BLUE_WON")
                                        return True
                        elif moveFrom in pos:
                            return False
            else:
                simBoard = deepcopy(self)
                for row in range(1, 11, 1):
                    for col in range(ord('a'), ord('i') + 1):
                        pos = (chr(col) + str(row))
                        if moveFrom in pos and simBoard.turn == simBoard.board[pos].get_color():
                            if not simBoard.board[pos].available_move(moveFrom, moveTo, simBoard):
                                return False
                            Temp = simBoard.board[pos]
                            if pos in ('d1', 'd2', 'd3', 'e1', 'e2', 'e3', 'f1', 'f2', 'f3'):
                                simBoard.board[pos] = PalaceSquare("red", "XXXXXXXXXXXX")
                            elif pos in ('d8', 'd9', 'd10', 'e8', 'e9', 'e10', 'f8', 'f9', 'f10'):
                                simBoard.board[chr(col) + str(row)] = PalaceSquare("blue", "000000000000")
                            else:
                                simBoard.board[pos] = EmptySquare(None, "[          ]")
                            for row2 in range(1, 11, 1):
                                for col2 in range(ord('a'), ord('i') + 1):
                                    pos = (chr(col2) + str(row2))
                                    if moveTo in pos:
                                        simBoard.board[pos] = Temp
                                        simBoard.set_turn()
                                        if simBoard.color_in_check(simBoard, simBoard.board[pos].get_color()):
                                            return False
                                        else:
                                            jGame.set_in_check(self.board[moveFrom].get_color(), False)
                                            return self.update_board(moveFrom, moveTo, jGame)
                        elif moveFrom in pos:
                            return False
        else:
            ret_str = str("Game Finished " + jGame.get_game_state())
            return ret_str

    def checkmate(self, color):
        """
        Checks for checkmate, calls on several helper functions
        :param color: Color of team to check for checkmate
        :return: Boolean on whether that team is in checkmate
        """
        colorpieces = []
        GenPosition = None
        for row in range(1, 11, 1):  # Find generals position for colored team
            for col in range(ord('a'), ord('i') + 1):
                pos = (chr(col) + str(row))
                if type(self.board[pos]) is General:
                    if self.board[pos].get_color() == color:
                        GenPosition = pos
        for row in range(1, 11, 1):  # Make a list of all pieces on colored team including general
            for col in range(ord('a'), ord('i') + 1):
                pos = (chr(col) + str(row))
                if self.board[pos].get_color() == self.board[GenPosition].get_color():
                    if type(self.board[pos]) is not PalaceSquare:
                        if type(self.board[pos]) is not EmptySquare:
                            colorpieces.append(pos)
        move_list = self.list_moves(colorpieces)
        if self.find_checkmate(move_list):
            return True
        else:
            return False

    def list_moves(self, colorPieces):
        """
        Creates a list of all possible moves for a list of pieces passed to it
        :param colorPieces: List of positions where an entire teams pieces are located
        :return: A list containing an ordered pair of a move from and a move to location that is legal
        """
        moveFromList = []
        moveToList = []
        for piece in colorPieces:  # Go through every piece in passed list
            for row in range(1, 11, 1):
                for col in range(ord('a'), ord('i') + 1):
                    moveTo = (chr(col) + str(row))
                    if self.board[piece].available_move(piece, moveTo, self):  # If the move for a piece is legal
                        moveFromList.append(piece)  # Store that move
                        moveToList.append(moveTo)
        a_zip = zip(moveFromList, moveToList)  # Zips together the lists to create ordered pairs
        zipped_list = list(a_zip)
        return zipped_list

    def find_checkmate(self, list_moves):
        """
        Go through a list of legal moves and create a simulation board to try them
        :param list_moves: List of legal moves
        :return: False if a legal move results in getting out of check
        """
        for move in list_moves:  # Try each move
            simBoard = deepcopy(self)  # Copy board to not mess with original
            moveFrom = move[0]
            moveTo = move[1]
            Temp = simBoard.board[moveFrom]
            simBoard.board[moveTo] = Temp
            if self.color_in_check(simBoard, Temp.get_color()):  # Check if team can escape check
                continue
            else:
                return False  # Team can escape check

    @staticmethod
    def color_in_check(board, color):
        """
        Checks if a team is in check after a move
        :param color: Color team to check
        :param board: Board to use, either a simulation board or the actual game board
        :return: Boolean on whether that team is in check
        """
        Gen = []
        for row in range(1, 11, 1):
            for col in range(ord('a'), ord('i') + 1):
                pos = (chr(col) + str(row))
                if type(board.board[pos]) is General:
                    Gen.append(pos)
        for row in range(1, 11, 1):
            for col in range(ord('a'), ord('i') + 1):
                pos = (chr(col) + str(row))
                if type(board.board[pos]) is not EmptySquare:
                    if type(board.board[pos]) is not PalaceSquare:
                        if color == "red":
                            if board.board[pos].available_move(pos, Gen[0], board):
                                if board.board[pos].get_color() != "red":
                                    return True
                        elif color == "blue":
                            if board.board[pos].available_move(pos, Gen[1], board):
                                if board.board[pos].get_color() != "blue":
                                    return True
        return False

    def set_turn(self):
        """
        Method called by update board to change turn after successful move
        :return: None
        """
        if self.turn == "red":
            self.turn = "blue"
        else:
            self.turn = "red"

    def get_piece(self, pos):
        """
        Method that takes a position on the board and returns the piece at the position
        :param pos: algebraic notation position on board
        :return: piece at that position
        """
        return self.board[pos]

    def print_board(self):
        """
        Extra function for debugging to display board
        :return: None
        """
        i = 0
        list_board = []
        for row in range(1, 11, 1):
            for column in self.board:
                if str(row) in column and i < 9:
                    list_board.append(self.board[column].get_name())
                    i += 1
            print(list_board)
            list_board = []
            i = 0
        print("\n\n")


class JanggiGame:
    """
    Game class, calls functions to establish board, starts and ends game
    """

    def __init__(self):
        """
        Creates board and starts game, initializes data members that store critical runtime information
        """
        self.board = Board()
        self.board.start_game()
        self.game_state = 'Unfinished'
        self.in_check = {"blue": False, "red": False}

    def set_game_sate(self, state):
        """
        Method for changing game state to "Finished"
        :param state:
        :return: None
        """
        self.game_state = state

    def get_game_state(self):
        """
        Method for checking current game state
        :return: Current game state
        """
        return self.game_state

    def set_in_check(self, color, check):
        """
        Setter for setting in_check, only used in making a move out of check
        :param color: Color of team to change in_check
        :param check: Check status (boolean)
        :return: None
        """
        self.in_check[color] = check

    def get_in_check(self, color):
        """
        Getter for in_check
        :param color: Color of team to check
        :return: in_check for a colored team
        """
        return self.in_check[color]

    def is_in_check(self, color):
        """
        Checks if a team is in check
        :param color: Color team to check
        :return: Boolean on whether that team is in check
        """
        Gen = []
        for row in range(1, 11, 1):
            for col in range(ord('a'), ord('i') + 1):
                pos = (chr(col) + str(row))
                if type(self.board.get_piece(pos)) is General:
                    Gen.append(pos)
        for row in range(1, 11, 1):
            for col in range(ord('a'), ord('i') + 1):
                pos = (chr(col) + str(row))
                if type(self.board.get_piece(pos)) is not EmptySquare:
                    if type(self.board.get_piece(pos)) is not PalaceSquare:
                        if color == "red":
                            if self.board.get_piece(pos).available_move(pos, Gen[0], self.board):
                                if self.board.get_piece(pos).get_color() != "red":
                                    self.in_check["red"] = True
                                    return True
                        elif color == "blue":
                            if self.board.get_piece(pos).available_move(pos, Gen[1], self.board):
                                if self.board.get_piece(pos).get_color() != "blue":
                                    self.in_check["blue"] = True
                                    return True
        self.in_check[color] = False
        return self.in_check[color]

    def make_move(self, moveFrom, moveTo):
        """
        Function that calls board update for move validation/making
        :param moveFrom: Position to move from
        :param moveTo: Position to move to
        :return: Boolean on whether move could have been made or not
        """
        if moveTo == moveFrom:
            self.board.set_turn()
            return True
        print("Attempting: ", moveFrom, "->", moveTo)
        return self.board.update_board(moveFrom, moveTo, self)
