from enum import IntEnum
import numpy


class Vector:
    x: int
    y: int
    value: int

    def __init__(self, x: int, y: int, value: int) -> None:
        self.SetValues(x, y, value)

    def SetValues(self, x: int, y: int, value: int):
        self.value = value
        self.x = x
        self.y = y
        if x < 0:
            self.x = -1
        elif x > 0:
            self.x = 1
        if y < 0:
            self.y = -1
        elif y > 0:
            self.y = 1

    def GetMovement(self):
        return self.x*self.value, self.y*self.value


class Point:
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class PlayerTypeEnum(IntEnum):
    Human = 1
    Computer = 2


class BeatingDirectionEnum(IntEnum):
    noBeat = 1
    forward = 2
    backward = 3


class PositionMoves:
    x: int
    y: int
    moves = numpy.zeros((3, 3))

    def __init__(self, x, y, moves):
        self.x = x
        self.y = y
        self.moves = moves


# class that stores one movement , position at the start of the move, direction of the movement and type of the beat
class Move:
    position: Point
    direction: Vector
    beatType: BeatingDirectionEnum

    def __init__(self, point: Point, movement: Vector, beatType: BeatingDirectionEnum = BeatingDirectionEnum.noBeat):
        self.position = point
        self.direction = movement
        self.beatType = beatType

    def GetNextPosition(self):
        return Point(self.position.x + self.direction.x, self.position.y + self.direction.y)


    #jeżeli można zbijać w obie strony to tworzę 2 osobne ruchy dla łatwości losowania ruchu
    def CreateMovesListFromPositionMoves(moves: PositionMoves):
        res = []
        for i in range(3):
            for j in range(3):
                if moves.moves[i][j] == 4:
                    res.append(Move(Point(moves.x, moves.y),
                               Vector(j-1, i-1, 1), BeatingDirectionEnum.forward))
                    res.append(Move(Point(moves.x, moves.y),
                               Vector(j-1, i-1, 1), BeatingDirectionEnum.backward))
                elif moves.moves[i][j] > 0:
                    res.append(Move(Point(moves.x, moves.y),
                               Vector(j-1, i-1, 1), BeatingDirectionEnum(moves.moves[i][j])))
        return res
