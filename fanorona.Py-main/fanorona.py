from typing import ForwardRef
import numpy
from primitives import *
infinity = 32767


class Board:
    fields = numpy.zeros((5, 9))

    def __init__(self) -> None:
        self.fields[:2][:] = 1
        self.fields[2][:4:2] = 1
        self.fields[2][1:4:2] = 2

        self.fields[2][5::2] = 1
        self.fields[2][6::2] = 2
        self.fields[3:][:] = 2


    # if x + y %2 == 0 to ruchy 8 ruchów else 4
    #FIXME nie zwraca wszystkich ruchow
    def GetAllPlayerMovements(self, player: int):
        moves = []
        for i in range(5):
            for j in range(9):
                if self.fields[i][j] == player:
                    move = self.GetEmptyPlacesForMovement(j, i)
                    if any(1 in sublist for sublist in move):
                        self.FindBeatingPossibleMoves(player, j, i, move)
                        self.RefineMoves(move)
                        tmpMoves = Move.CreateMovesListFromPositionMoves(PositionMoves(j, i, move))
                        for move in tmpMoves:
                            moves.append(move)

        # jeżeli istnieją zbijające ruchy to je wywalam
        areBeatableMoves = False
        for move in moves:
            if int(move.beatType) > 1:
                areBeatableMoves = True
                break
        if areBeatableMoves:
            i = 0
            while i < len(moves):
                if int(moves[i].beatType) == 1:
                    moves.pop(i)
                else:
                    i += 1
        return moves

    def RefineMoves(self, moves: list):
        doRefine = False
        for move in moves:
            for x in move:
                if x > 1:
                    doRefine = True
        if doRefine:
            for move in moves:
                for x in move:
                    if x == 1:
                        x = 0
        return doRefine

    def FindBeatingPossibleMoves(self, player: int, x: int, y: int, moves):
        dirX = 0
        dirY = 0
        for i in range(3):
            for j in range(3):
                dirX = j - 1
                dirY = i - 1
                if moves[i][j] == 1:
                    moves[i][j] = self.CheckFrontandBackForBeat(
                        player, x, y, dirX, dirY)

    # returns 1 if movement is possible without beating
    # 2 if movement is possible with forward beat
    # 3 if movement is possible with backward beat and
    # 4 if movement is possible with both forward and backward

    def CheckFrontandBackForBeat(self, player, x, y, dirX, dirY) -> int:
        enemy = 1
        if player == 1:
            enemy = 2
        forward = False
        backward = False
        # check front
        tmpX = x + 2 * dirX
        tmpY = y + 2 * dirY
        if tmpX < 9 and tmpY < 5 and tmpX >= 0 and tmpY >= 0:
            forward = (self.fields[tmpY][tmpX] == enemy)
        # check back
        tmpX = x - dirX
        tmpY = y - dirY
        if tmpX < 9 and tmpY < 5 and tmpX >= 0 and tmpY >= 0:
            backward = (self.fields[tmpY][tmpX] == enemy)
        if forward and backward:
            return 4
        if backward:
            return 3
        if forward:
            return 2
        return 1

    def GetEmptyPlacesForMovement(self, x: int, y: int):
        tmpX = x
        tmpY = y
        res = numpy.zeros((3, 3))

        if (x + y) % 2 == 0:
            for i in range(3):
                for j in range(3):
                    res[i][j] = self.IsEmpty(y + i - 1, x + j - 1)
        else:
            res[1][2] = self.IsEmpty(y, x + 1)
            res[1][0] = self.IsEmpty(y, x - 1)
            res[2][1] = self.IsEmpty(y + 1, x)
            res[0][1] = self.IsEmpty(y - 1, x)
        # print(res[:][:])
        return res

    def IsEmpty(self, y, x) -> bool:
        if 0 <= x < 9 and 0 <= y < 5:
            return self.fields[y][x] == 0
        else:
            return False

    # def move(self, x, y, xDest, yDest) -> bool:

    def CalculatePlayerLead(self, playerNumber: int) -> int:
        playerCount = 0
        enemyCount = 0
        for i in range(5):
            for j in range(9):
                if self.fields[i][j] == playerNumber:
                    playerCount += 1
                elif self.fields[i][j] != 0:
                    enemyCount += 1
        ret = playerCount - enemyCount
        if enemyCount == 0:
            ret = infinity
        elif playerCount == 0:
            ret = -infinity
        return ret



#class env:
#    board: Board
#    player1 = Player(PlayerTypeEnum.Human, "1")
#    player2 = Player(PlayerTypeEnum.Human, "2")
#
#    def __init__(self) -> None:
#        pass
