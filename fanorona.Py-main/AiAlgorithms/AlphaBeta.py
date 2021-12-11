from Players import Player
from fanorona import Board
from Players import infinityEval, infinity


class AlphaBeta:
    player: 'Player' = None

    def __init__(self, player):
        self.player = player

    def AI_AlphaBeta(self, depth: int, board: 'Board'):
        movesList = board.GetAllPlayerMovements(self.player.playerNumber)

        value = -infinityEval
        winValue = value
        retBoard = Board()
        retBoard.fields = board.fields.copy()
        retChangePlayer = False

        for move in movesList:
            tmpBoard = Board()
            tmpBoard.fields = board.fields.copy()
            returnedBoard, allMoves = Player.MakeMove(tmpBoard, move)

            tmpBoard.fields = returnedBoard.copy()
            changePlayer = True

            # liczę kilkukrotne zbicia jako tą samą turę
            if allMoves != None and len(allMoves) > 0:
                value = max(value, self.AlphaBeta(depth, tmpBoard, self.player.playerNumber, allMoves, True))
                changePlayer = False
            else:
                playerNum = 1
                if self.player.playerNumber == 1:
                    playerNum = 2
                movesListtmp = tmpBoard.GetAllPlayerMovements(playerNum)
                value = max(value, self.AlphaBeta(depth - 1, tmpBoard, playerNum, movesListtmp, False))

            if winValue < value:
                winValue = value
                retBoard = tmpBoard
                retChangePlayer = changePlayer

        return winValue, retBoard.fields, retChangePlayer

    def AlphaBeta(self, depth: int, board: Board, playerNumber: int, movesList: list, maximizing: bool,
                  alpha: float = -infinityEval, beta: float = infinityEval):
        nodeVal = board.CalculatePlayerLead(playerNumber)
        if depth < 1 or infinity == nodeVal or infinity == -nodeVal:
            if not maximizing:
                nodeVal *= -1
            return nodeVal

        if maximizing:
            for move in movesList:
                tmpBoard = Board()
                tmpBoard.fields = board.fields.copy()
                returnedBoard, allMoves = Player.MakeMove(tmpBoard, move)
                tmpBoard.fields = returnedBoard.copy()

                # liczę kilkukrotne zbicia jako tą samą turę
                if allMoves is not None and len(allMoves) > 0:
                    alpha = max(alpha, self.AlphaBeta(depth, tmpBoard, playerNumber, allMoves, True, alpha, beta))
                else:
                    playerNum = 1
                    if playerNumber == 1:
                        playerNum = 2
                    movesListtmp = tmpBoard.GetAllPlayerMovements(playerNum)
                    alpha = max(alpha, self.AlphaBeta(depth - 1, tmpBoard, playerNum, movesListtmp, False, alpha, beta))
                if alpha >= beta:
                    return beta
            return alpha
        else:
            for move in movesList:
                tmpBoard = Board()
                tmpBoard.fields = board.fields.copy()
                returnedBoard, allMoves = Player.MakeMove(tmpBoard, move)
                tmpBoard.fields = returnedBoard.copy()

                # liczę kilkukrotne zbicia jako tą samą turę
                if allMoves is not None and len(allMoves) > 0:
                    beta = min(beta, self.AlphaBeta(depth, tmpBoard, playerNumber, allMoves, False, alpha, beta))
                else:
                    playerNum = 1
                    if playerNumber == 1:
                        playerNum = 2
                    movesListtmp = tmpBoard.GetAllPlayerMovements(playerNum)
                    beta = min(beta, self.AlphaBeta(depth - 1, tmpBoard, playerNum, movesListtmp, True, alpha, beta))
                if alpha >= beta:
                    return alpha
            return beta
