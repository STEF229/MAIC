from core import rules , Color
from faronona.faronona_player import FarononaPlayer
from faronona.faronona_rules import FarononaRules
from faronona.faronona_action import FarononaAction
from faronona.faronona_action import FarononaActionType
import random , copy, json

#  python main.py -ai0 ./faronona/alpha_ah.py -ai1 ./faronona/random_agent.py -s 1 -t 5

class AI(FarononaPlayer):

    name = "AH"
    vale = 0 
    after_demar = {"a": 1, "b1": 1 , "b21": 1,"b22": 1, "c":1, "d":1 , "e1": 1 , "e2": 1 }

    def __init__(self, color):
        super(AI, self).__init__(self.name, color)
        self.position = color.value

    def play(self, state, remain_time):


        def all_move(stat,move, player):

            mov = move.get_action_as_dict()
            at = mov['action']['at']
            to = mov['action']['to']
            a = 0
            b = 0
            results_o, results_a, results_b = [],[], []
            opp_val = -player
             
            results = []
            if (FarononaRules.is_win_approach_move(at, to, stat, player) is not None) and (len(FarononaRules.is_win_approach_move(at, to, stat, player)) != 0):
                
            # between win approach and win remoate, check which can let me gain the more adverse pieces
                a = len(FarononaRules.is_win_approach_move(at, to, stat,player))
                next_state, _a = FarononaRules.make_move(stat,move,player)
                # adver_die += a
                # possible_m = FarononaRules.get_effective_cell_moves(next_state,to)
                # board = stat.get_board()
                fa = FarononaRules.get_player_actions(next_state,player)
                
                
                
                if len(fa)== 0:
                    next_state.winmove = None 
                    next_state.set_next_player(player * -1)
                    results_a = [{"state": next_state, "next_move": fa }]
                else:
                    results_a = [{"state": next_state, "next_move": fa }]
                    # next_player = opp_val
                # else:
                #     next_player = next_state.get_next_player()

               
                # if next_player == player:
                #     next_moves = FarononaRules.get_player_actions(next_state, next_player)

                #     results_a = []
                #     for action in next_moves :
                #         attendu  = all_move(next_state,action, player, adver_die)
                #         for attend in attendu: 
                #             results_a.append(attend)

                
                # else:

                # results_a = [{"state": next_state, "next_move": fa }]
           

            if (FarononaRules.is_win_remote_move(at, to, stat, player) is not None) and (len(FarononaRules.is_win_remote_move(at, to, stat, player)) != 0):
                b = len(FarononaRules.is_win_remote_move(at, to, stat,player))
                next_state, _a = FarononaRules.make_move(stat,move,player)
                # adver_die += b

                fb = FarononaRules.get_player_actions(next_state,player)

                if len(fb)== 0:

                    next_state.winmove = None 
                    next_state.set_next_player(player * -1) 

                    results_b = [{"state": next_state, "next_move": fb }]
                else:
                    results_b = [{"state": next_state, "next_move": fb }]
                    # next_player = opp_val
                # else:
                #     next_player = next_state.get_next_player()


                # if next_player == player:
                #     next_moves = FarononaRules.get_player_actions(next_state, next_player)
                #     results_b = []
                #     for action in next_moves :
                #         attendu  = all_move(next_state,action, player, adver_die)
                #         for atten in attendu: 
                #             results_b.append(atten)       
                 
                # else:
                


            if a == 0 and b == 0:
                fc = []
                results_o = [{"state": stat, "next_move": fc }] 
            
            results = results_a + results_b + results_o
            return results

        def AI_AlphaBeta(depth , startState , player):
            
            possible_move = FarononaRules.get_player_actions(startState,player)
            if len (possible_move) == 1 :
                    return possible_move[0]
            value = -2147483648
            winValue = value
            retBoard = copy.deepcopy(startState)
            retChangePlayer = False
            best_move = 0
            for move in possible_move:
                # print("########### EVA ###########", move, winValue, best_move)

                tmpBoard = copy.deepcopy(startState)

                aa_returnedBoard = all_move(tmpBoard, move, player)
                for m in aa_returnedBoard :
                    returnedBoard , allMoves = m['state'], m['next_move']

                    tmpBoard = copy.deepcopy(returnedBoard)
                    changePlayer = True

                    # liczę kilkukrotne zbicia jako tą samą turę
                    if allMoves != None and len(allMoves) > 0:
                        value = max(value, AlphaBeta(depth, tmpBoard, player, allMoves, True))
                        changePlayer = False
                    else:
                        playerNum = -player
                        
                        movesListtm = FarononaRules.get_player_actions(tmpBoard, playerNum)
                        value = max(value, AlphaBeta(depth - 1, tmpBoard, playerNum, movesListtm, False))

                    if winValue < value:
                        winValue = value
                        retBoard = tmpBoard
                        best_move = move
                        retChangePlayer = changePlayer

            return best_move

        def CalculatePlayerLead(stats, player):

            playerCount = 0
            enemyCount = 0
            opp_val = -player

            info_adv = stats.get_player_info(opp_val)
            enemyCount = int(info_adv["on_board"])

            info_me = stats.get_player_info(player)
            playerCount = int(info_me["on_board"])

            ret = playerCount - enemyCount

            if enemyCount == 0:
                ret = 32767
            elif playerCount == 0:
                ret = -32767
            return ret
        
        def AlphaBeta(depth, board, playerNumber, movesList, maximizing,
                        alpha = -2147483648 , beta = 2147483648):
            # infinityEval = 2147483648
            infinity = 32767
            nodeVal = CalculatePlayerLead(board, playerNumber)
            if depth < 1 or infinity == nodeVal or infinity == -nodeVal:
                if not maximizing:
                    nodeVal *= -1
                return nodeVal

            if maximizing:
                for mov in movesList:
                    tmpBoar = copy.deepcopy(board)


                    a_returnedBoard = all_move(tmpBoar, mov, playerNumber)
                    for n in a_returnedBoard :
                        returnedBoar , allMove = n['state'], n['next_move']
                        tmpBoar = copy.deepcopy(returnedBoar)

                        # liczę kilkukrotne zbicia jako tą samą turę
                        if allMove is not None and len(allMove) > 0:
                            alpha = max(alpha, AlphaBeta(depth, tmpBoar, playerNumber, allMove, True, alpha, beta))
                        else:
                            playerNum = -playerNumber
                            movesListtmp = FarononaRules.get_player_actions(tmpBoar,playerNum)
                            # print("##################000000000000000000000000000##############", movesListtmp)
                            alpha = max(alpha, AlphaBeta(depth - 1, tmpBoar, playerNum, movesListtmp, False, alpha, beta))
                        if alpha >= beta:
                            return beta
                return alpha
            else:
                for moves in movesList:
                    tmpBoa = copy.deepcopy(board)

                    b_returnedBoard = all_move(tmpBoa, moves, playerNumber)
                    for n in b_returnedBoard :
                        returnedBoa , allMov = n['state'], n['next_move']
                        tmpBoa = copy.deepcopy(returnedBoa)

                    # liczę kilkukrotne zbicia jako tą samą turę
                    if allMov is not None and len(allMov) > 0:
                        beta = min(beta, AlphaBeta(depth, tmpBoa, playerNumber, allMov, False, alpha, beta))
                    else:
                        playerNume = -playerNumber
                        movesListtmpe = FarononaRules.get_player_actions(tmpBoa,playerNume)
                        beta = min(beta, AlphaBeta(depth - 1, tmpBoa, playerNume, movesListtmpe, True, alpha, beta))
                    if alpha >= beta:
                        return alpha
                return beta

        
        action = AI_AlphaBeta(depth= 2, startState=state ,player = self.position )
        return action 
