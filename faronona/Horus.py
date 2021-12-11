
from core import rules , Color
from faronona.faronona_player import FarononaPlayer
from faronona.faronona_rules import FarononaRules
from faronona.faronona_action import FarononaAction
from faronona.faronona_action import FarononaActionType
import random , copy, json

#  python main.py -ai0 ./faronona/Horus.py -ai1 ./faronona/horus_agent_w.py -s 1 -t 5


class AI(FarononaPlayer):

    name = "Dieu AT"
    vale = 0 
    after_demar = {"a": 1, "b1": 1 , "b21": 1,"b22": 1, "c":1, "d":1 , "e1": 1 , "e2": 1 }

    def __init__(self, color):
        super(AI, self).__init__(self.name, color)
        self.position = color.value

    def play(self, state, remain_time):

        def demarage(state, player):
            # opposant= {"1":-1, "-1":1}
            opp_val = -player
            if ((self.vale == 1) and (state.get_latest_player() is None) ):
                at, to = (1,5), (2,4)
                a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)

            if ((self.vale == 2) and (state.get_latest_player()== opp_val) ):
                at, to = (2,5), (2,4)
                a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                next_state, _a = FarononaRules.make_move(state,a_act,player)

            if ((self.vale == 3) and (state.get_latest_player()== player) ):
                at, to = (2,4), (1,4)
                a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)

            return a_act

        def demarage_def(state, player):
            # opposant= {"1":-1, "-1":1}
            opp_val = -player
            latest_move = state.get_latest_move()
            at , to = latest_move['action']['at'], latest_move['action']['to']

            if((state.get_latest_player()== opp_val) ) and ((at == (1,3) and (to == (2,4)))):
            
            
                at, to = (4,5), (3,5)
                a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)

            return a_act

        def cas_a (val): # cas A B1 D

            if val == 1:

                if self.vale == 4 :
                    at, to = (1,3), (2,2)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["a"] = "a"
                    self.after_demar["b1"] = "b1"

                if self.vale == 5  :
                    at, to = (2,2), (2,3)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)
                    self.after_demar["a"] = "a"
                    self.after_demar["b1"] = "b1"

                if self.vale == 6  :
                    at, to = (2,3), (3,3)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["a"] = "a"
                    self.after_demar["b1"] = "b1"

                if self.vale == 7  :
                    at, to = (3,3), (3,4)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)
                    self.after_demar = {"a": 2, "b1": 2 , "b21": 2,"b22": 2, "c":2, "d":2 , "e1": 2 , "e2": 2 }

            if val == 2:

                if self.vale == 4 :
                    at, to = (1,5), (2,5)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["d"] = "d"
                    self.after_demar["e1"] = "e1"
                    self.after_demar["e2"] = "e2"

                if self.vale == 5  :
                    at, to = (2,5), (2,4)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)
                    self.after_demar["d"] = "d"
                    self.after_demar["e1"] = "e1"
                    self.after_demar["e2"] = "e2"

                if self.vale == 6  :
                    at, to = (2,4), (3,5)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["d"] = "d"
                    self.after_demar["e1"] = "e1"
                    self.after_demar["e2"] = "e2"

                if self.vale == 7  :
                    at, to = (3,5), (3,4)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)
                    self.after_demar = {"a": 2, "b1": 2 , "b21": 2,"b22": 2, "c":2, "d":2 , "e1": 2 , "e2": 2 }

                    

            
            return a_act



        def cas_b (val): # cas B21 B22 C

            if val == 1:
               
                if self.vale == 4 :

                    at, to = (0,4), (1,5)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["b21"] = "b21"
                if self.vale == 5 :
                    at, to = (1,5), (2,4)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["b21"] = "b21"
                if self.vale == 6 :
                    at, to = (2,4), (3,5)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["b21"] = "b21"
                if self.vale == 7 :
                    at, to = (3,5), (3,4)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)
                    self.after_demar = {"a": 2, "b1": 2 , "b21": 2,"b22": 2, "c":2, "d":2 , "e1": 2 , "e2": 2 }


            elif val ==2 :

                if self.vale == 4 :
                    at, to = (1,2), (2,2)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["b22"] = "b22"
                if self.vale == 5 :
                    at, to = (2,2), (2,3)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)
                    self.after_demar["b22"] = "b22"
                if self.vale == 6 :
                    at, to = (2,3), (3,3)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["b22"] = "b22"
                if self.vale == 7 :
                    at, to = (3,3), (3,2)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)
                    self.after_demar = {"a": 2, "b1": 2 , "b21": 2,"b22": 2, "c":2, "d":2 , "e1": 2 , "e2": 2 }


            elif val == 3 :

                if self.vale == 4 :
                    at, to = (1,3), (2,4)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["c"] = "c"
                if self.vale == 5 :
                    at, to = (2,4), (2,3)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["c"] = "c"
                if self.vale == 6 :
                    at, to = (2,3), (3,3)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["c"] = "c"
                if self.vale == 7 :
                    at, to = (3,3), (3,2)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["c"] = "c"

                if self.vale == 8 :
                    at, to = (3,2), (2,2)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)
                    self.after_demar["c"] = "c"

                if self.vale == 9 :
                    at, to = (2,2), (3,1)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    self.after_demar["c"] = "c"

                if self.vale == 10 :
                    at, to =  (3,1), (2,1)
                    a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)
                    self.after_demar = {"a": 2, "b1": 2 , "b21": 2,"b22": 2, "c":2, "d":2 , "e1": 2 , "e2": 2 }

                    
            
            return a_act

        def al_move(stat,move, player):

            mov = move.get_action_as_dict()
            at = mov['action']['at']
            to = mov['action']['to']
            a = 0
            b = 0
            results_o, results_a, results_b = [],[], []
            opp_val = -player
             
            results = []
            if (FarononaRules.is_win_approach_move(at, to, stat, player) is not None) and (len(FarononaRules.is_win_approach_move(at, to, stat, player)) != 0):
                
                a = len(FarononaRules.is_win_approach_move(at, to, stat,player))
                next_state, _a = FarononaRules.make_move(stat,move,player)
               
                fa = FarononaRules.get_player_actions(next_state,player)
                
                
                
                if len(fa)== 0:
                    next_state.winmove = None 
                    next_state.set_next_player(player * -1)
                    results_a = [{"state": next_state, "next_move": fa }]
                else:
                    results_a = [{"state": next_state, "next_move": fa }]
                

            if (FarononaRules.is_win_remote_move(at, to, stat, player) is not None) and (len(FarononaRules.is_win_remote_move(at, to, stat, player)) != 0):
                b = len(FarononaRules.is_win_remote_move(at, to, stat,player))
                next_state, _a = FarononaRules.make_move(stat,move,player)

                fb = FarononaRules.get_player_actions(next_state,player)

                if len(fb)== 0:

                    next_state.winmove = None 
                    next_state.set_next_player(player * -1) 

                    results_b = [{"state": next_state, "next_move": fb }]
                else:
                    results_b = [{"state": next_state, "next_move": fb }]
                 


            if a == 0 and b == 0:
                fc = []
                results_o = [{"state": stat, "next_move": fc }] 
            
            results = results_a + results_b + results_o
            return results

        def AI_AlphaBeta(depth , startState , player, chass = []):
            
            if len (chass) == 0:
                possible_move = FarononaRules.get_player_actions(startState,player)
                if len (possible_move) == 1 :
                        return possible_move[0]
                value = -2147483648
                winValue = value
                retBoard = copy.deepcopy(startState)
                retChangePlayer = False
                best_move = 0
                for move in possible_move:

                    tmpBoard = copy.deepcopy(startState)

                    aa_returnedBoard = al_move(tmpBoard, move, player)
                    for m in aa_returnedBoard :
                        returnedBoard , allMoves = m['state'], m['next_move']

                        tmpBoard = copy.deepcopy(returnedBoard)
                        changePlayer = True

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
            else:
                # print("#####..... think ......###############")
                value = -2147483648
                winValue = value
                retBoard = copy.deepcopy(startState)
                retChangePlayer = False
                best_move = 0
                for move in chass:

                    tmpBoard = copy.deepcopy(startState)

                    aa_returnedBoard = al_move(tmpBoard, move, player)
                    for m in aa_returnedBoard :
                        returnedBoard , allMoves = m['state'], m['next_move']

                        tmpBoard = copy.deepcopy(returnedBoard)
                        changePlayer = True

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

            infinity = 32767
            nodeVal = CalculatePlayerLead(board, playerNumber)
            if depth < 1 or infinity == nodeVal or infinity == -nodeVal:
                if not maximizing:
                    nodeVal *= -1
                return nodeVal

            if maximizing:
                for mov in movesList:
                    tmpBoar = copy.deepcopy(board)


                    a_returnedBoard = al_move(tmpBoar, mov, playerNumber)
                    for n in a_returnedBoard :
                        returnedBoar , allMove = n['state'], n['next_move']
                        tmpBoar = copy.deepcopy(returnedBoar)

                        if allMove is not None and len(allMove) > 0:
                            alpha = max(alpha, AlphaBeta(depth, tmpBoar, playerNumber, allMove, True, alpha, beta))
                        else:
                            playerNum = -playerNumber
                            movesListtmp = FarononaRules.get_player_actions(tmpBoar,playerNum)

                            alpha = max(alpha, AlphaBeta(depth - 1, tmpBoar, playerNum, movesListtmp, False, alpha, beta))
                        if alpha >= beta:
                            return beta
                return alpha
            else:
                for moves in movesList:
                    tmpBoa = copy.deepcopy(board)

                    b_returnedBoard = al_move(tmpBoa, moves, playerNumber)
                    for n in b_returnedBoard :
                        returnedBoa , allMov = n['state'], n['next_move']
                        tmpBoa = copy.deepcopy(returnedBoa)

                    if allMov is not None and len(allMov) > 0:
                        beta = min(beta, AlphaBeta(depth, tmpBoa, playerNumber, allMov, False, alpha, beta))
                    else:
                        playerNume = -playerNumber
                        movesListtmpe = FarononaRules.get_player_actions(tmpBoa,playerNume)
                        beta = min(beta, AlphaBeta(depth - 1, tmpBoa, playerNume, movesListtmpe, True, alpha, beta))
                    if alpha >= beta:
                        return alpha
                return beta

        

        def core (player, state):
            possible_move = FarononaRules.get_player_actions(state,player)
            if len (possible_move) == 1 :
                return possible_move[0]
            if self.vale == -2 :
            
                test_state = copy.deepcopy(state)
                ans  = is_win(test_state , player, possible_move)
                if ans:
                    actio = AI_AlphaBeta(depth= 2, startState=state ,player = self.position )
                    return actio
                else:
                    b_ = best_move (test_state , player, possible_move)
                    return b_
            else:
                
                test_state = copy.deepcopy(state)
                ans = is_win(test_state , player, possible_move) 
                if ans:
                    acti = AI_AlphaBeta(depth= 2, startState=state ,player = self.position )
                    return acti
                else:
                    b_ = best_move (test_state , player, possible_move)
                    return b_     

        def is_win (stated , player, moves):

            for n in moves:
                att = n.get_action_as_dict()['action']['at']
                too = n.get_action_as_dict()['action']['to']
                if (FarononaRules.is_win_approach_move(att, too, stated, player) is not None and len(FarononaRules.is_win_approach_move(att, too, stated, player)) != 0):
                    return True
                if (FarononaRules.is_win_remote_move(att, too, stated, player) is not None and len(FarononaRules.is_win_remote_move(att, too, stated, player)) != 0):
                    return True
            return False

        def corner (statedd , player): #reste un aautre cas de corner

            board = statedd.get_board()
            adver = -player
            act = None
            if board.is_empty_cell((1,1)):
                if ((board.get_cell_color((0,0)) == Color(player)) and (board.get_cell_color((1,0)) == Color(player))):
                    if (board.get_cell_color((2,0)) == Color(adver)):
                        a = (1,0)
                        t = (1,1)
                        act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=a, to=t)
                        
                elif ((board.get_cell_color((0,0)) == Color(player)) and (board.get_cell_color((0,1)) == Color(player))):
                    if (board.get_cell_color((0,2)) == Color(adver)):
                        a = (0,1)
                        t = (1,1)
                        act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=a, to=t)
                

            if board.is_empty_cell((3,1)):
                if ((board.get_cell_color((3,0)) == Color(player)) and (board.get_cell_color((4,0)) == Color(player))):
                    if (board.get_cell_color((2,0)) == Color(adver)):
                        a = (3,0)
                        t = (3,1)
                        act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=a, to=t)
                        
                elif ((board.get_cell_color((4,0)) == Color(player)) and (board.get_cell_color((4,1)) == Color(player))):
                    if (board.get_cell_color((4,2)) == Color(adver)):
                        a = (4,1)
                        t = (3,1)
                        act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=a, to=t)

            if board.is_empty_cell((3,7)):
                if ((board.get_cell_color((3,8)) == Color(player)) and (board.get_cell_color((4,8)) == Color(player))):
                    if (board.get_cell_color((2,8)) == Color(adver)):
                        a = (3,8)
                        t = (3,7)
                        act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=a, to=t)
                        
                elif ((board.get_cell_color((4,8)) == Color(player)) and (board.get_cell_color((4,7)) == Color(player))):
                    if (board.get_cell_color((4,6)) == Color(adver)):
                        a = (4,7)
                        t = (3,7)
                        act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=a, to=t)

            if board.is_empty_cell((1,7)):
                if ((board.get_cell_color((0,8)) == Color(player)) and (board.get_cell_color((1,8)) == Color(player))):
                    if (board.get_cell_color((2,8)) == Color(adver)):
                        a = (1,8)
                        t = (1,7)
                        act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=a, to=t)
                        
                elif ((board.get_cell_color((0,8)) == Color(player)) and (board.get_cell_color((0,7)) == Color(player))):
                    if (board.get_cell_color((0,6)) == Color(adver)):
                        a = (0,7)
                        t = (1,7)
                        act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=a, to=t)
            
            # print(f"############# {act} #####################")

            return act

            # for n in moves:
            #     att = n.get_action_as_dict()['action']['at']
            #     too = n.get_action_as_dict()['action']['to']
            #     if (FarononaRules.is_win_approach_move(att, too, stated, player) is not None and len(FarononaRules.is_win_approach_move(att, too, stated, player)) != 0):
            #         return True
            #     if (FarononaRules.is_win_remote_move(att, too, stated, player) is not None and len(FarononaRules.is_win_remote_move(att, too, stated, player)) != 0):
            #         return True
            # return False

        def save_me (next_stte, player, le_move ):

            bd = next_stte.get_board()
            ac = None
            adv = - player

            for j in range (0,5):
                # first colonn
                if (bd.get_cell_color((j,0)) == Color(player)):
                    if (j-1 >= 0) and (j+1 <= 4):
                        if (((j-1, 2) in le_move) and ((j+1,2) in le_move)):
                            if (j == 3 or j == 2 ):
                                aa = (j,0)
                                tt = (j+1,0)
                                if bd.is_empty_cell(tt):
                                    ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                            if (j == 1):
                                aa = (j,0)
                                tt = (j-1,0)
                                if bd.is_empty_cell(tt):
                                    ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                                    
                    elif (j-1 < 0):
                        if (((j+1, 2) in le_move) and (bd.get_cell_color((j+3,0)) != Color(adv))):
                            aa = (j,0)
                            tt = (j+1,0)
                            if bd.is_empty_cell(tt):
                                ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                                
                    elif (j+1 > 4):
                        if (((j-1, 2) in le_move) and (bd.get_cell_color((j-3,0)) != Color(adv))):
                            aa = (j,0)
                            tt = (j-1,0)
                            if bd.is_empty_cell(tt):
                                ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to= tt)
                                

                # last colonn
                if (bd.get_cell_color((j,8)) == Color(player)):
                    if (j-1 >= 0) and (j+1 <= 4):
                        if (((j-1, 6) in le_move) and ((j+1,6) in le_move)):
                            if (j == 3 or j == 2 ):
                                aa = (j,8)
                                tt = (j+1,8)
                                if bd.is_empty_cell(tt):
                                    ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                                    
                            if (j == 1):
                                aa = (j,8)
                                tt = (j-1,8)
                                if bd.is_empty_cell(tt):
                                    ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                                    
                            # elif (j == 2):
                            #         aa = (j,8)
                            #         tt = (j+1,8)
                            #         ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                            #         
                    elif (j-1<0):
                        if (((j+1, 6) in le_move) and (bd.get_cell_color((j+3,8)) != Color(adv))):
                            aa = (j,8)
                            tt = (j+1,8)
                            if bd.is_empty_cell(tt):
                                ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                                
                    elif (j+1 > 4):
                        if (((j-1, 6) in le_move) and (bd.get_cell_color((j-3,8)) != Color(adv))):
                            aa = (j,8)
                            tt = (j-1,8)
                            if bd.is_empty_cell(tt):
                                ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to= tt)
                                
        
            for i in range (0,9):
                # first row
                if (bd.get_cell_color((0,i)) == Color(player)):
                    # if (i-1 >= 0) and (i+1 <= 8):
                    #     if (((2, i-1) in le_move) and ((2, i+1) in le_move)): 
                    #         if (i % 2 == 0):
                    #             aa = (j,0)
                    #             tt = (j+1,0)
                    #             if bd.is_empty_cell(tt):
                    #                 ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                    #                 
                    #         if (j == 1):
                    #             aa = (j,0)
                    #             tt = (j-1,0)
                    #             if bd.is_empty_cell(tt):
                    #                 ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                    #                 
                    if (i == 0):
                        if (((2, 1) in le_move) and (bd.get_cell_color((0, 3)) != Color(adv))):
                            aa = (0,0)
                            tt = (0, 1)
                            if bd.is_empty_cell(tt):
                                ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                                
                    elif (i == 8):
                        if (((2, 7) in le_move) and (bd.get_cell_color((0, 5)) != Color(adv))):
                            aa = (0, 8)
                            tt = (0, 7)
                            if bd.is_empty_cell(tt):
                                ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to= tt)
                                

                # last row
                if (bd.get_cell_color((4,i)) == Color(player)):
                    # if (j-1 >= 0) and (j+1 <= 4):
                    #     if (((j-1, 6) in le_move) and ((j+1,6) in le_move)):
                    #         if (j == 3 or j == 2 ):
                    #             aa = (j,8)
                    #             tt = (j+1,8)
                    #             if bd.is_empty_cell(tt):
                    #                 ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                    #                 
                    #         if (j == 1):
                    #             aa = (j,8)
                    #             tt = (j-1,8)
                    #             if bd.is_empty_cell(tt):
                    #                 ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                    #                 
                            # elif (j == 2):
                            #         aa = (j,8)
                            #         tt = (j+1,8)
                            #         ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                            #         
                    if (i == 0):
                        if (((2, 1) in le_move) and (bd.get_cell_color((4, 3)) != Color(adv))):
                            aa = (4,0)
                            tt = (4, 1)
                            if bd.is_empty_cell(tt):
                                ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to=tt)
                                
                    elif (i == 8):
                        if (((2, 7) in le_move) and (bd.get_cell_color((4, 5)) != Color(adv))):
                            aa = (4,8)
                            tt = (4, 7)
                            if bd.is_empty_cell(tt):
                                ac = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=aa, to= tt)
                                
            return ac


        def best_move (stated , player, moves): # à optimiser ou créer une autre fonction de checking 
            x = copy.deepcopy(moves)
            delet = []
            

            f = corner (stated , player)
            if f is not None:
                # print( "###### corner ####")
                return f
            
            for m in x:
                initial_value = []
                final_value = []
                statess = copy.deepcopy(stated)
                # att = m.get_action_as_dict()['action']['at']
                too = m.get_action_as_dict()['action']['to']
                next_state, _a = FarononaRules.make_move(statess,m,player)
                opp_val = -player
                l_move = FarononaRules.get_player_actions(next_state, opp_val)
                

                # save from futur atak of adverse
               
                save_mo = save_me (next_state, player, l_move )
                if save_mo is not None:
                    print( "###### save me ####")
                    return save_mo
                # nodeVal = CalculatePlayerLead(next_state, player)
                

                for t in l_move:
                    ats = t.get_action_as_dict()['action']['at']
                    tos = t.get_action_as_dict()['action']['to']
                    if (FarononaRules.is_win_approach_move(ats, tos, next_state, opp_val) is not None and len(FarononaRules.is_win_approach_move(ats, tos, next_state, opp_val)) != 0):
                        bouf_app = FarononaRules.is_win_approach_move(ats, tos, next_state, opp_val)

                        # nex_state, _a = FarononaRules.make_move(next_state,t,opp_val)
                        # info_me = nex_state.get_player_info(player)
                        # playerCount = int(info_me["on_board"])
                        # initial_value.append(playerCount)

                        if too in bouf_app:
                            if m not in delet:
                                
                                delet.append(m)
                                break
            
                    if (FarononaRules.is_win_remote_move(ats, tos, next_state, opp_val) is not None and len(FarononaRules.is_win_remote_move(ats, tos, next_state, opp_val)) != 0):
                        bouf_remo = FarononaRules.is_win_remote_move(ats, tos, next_state, opp_val)
                        
                        if too in bouf_remo:
                            if m not in delet:
                                delet.append(m)
                                break
                
                
            z = [i for i in x if i not in delet] # verifier si ya pas de mouvement pouvant tuer nos coéquipiers
            

            if len(z) != 0:
                if len (z) == 1 :
                    return z[0]

                else:
                    # print("#####...........###############")
                   return z[random.randint(0,len(z)-1)]
            else:
                if f is not None:
                    return f
                return False, moves[random.randint(0,len(moves)-1)]
                # # print("#####..... SUICIDE......###############")
                # acti = AI_AlphaBeta(depth= 3, startState=state ,player = self.position , chass= moves)
                # return acti
                # return moves[random.randint(0,len(moves)-1)]        







        def after_demarage(state, player):

            opp_val = -player
            latest_move = state.get_latest_move()



            at , to = latest_move['action']['at'], latest_move['action']['to']

            if ((((self.vale == 4) and (state.get_latest_player()== opp_val) ) and ((at == (2,6) and (to == (2,5))))) or (self.after_demar["a"] == "a")):
                a_act = cas_a (1)
                self.after_demar["b1"] = "a"


            elif ((((self.vale == 4) and (state.get_latest_player()== opp_val) ) and ((at == (3,5) and (to == (2,5))))) or (self.after_demar["b1"] == "b1")):
                a_act = cas_a (1)
                self.after_demar["a"] = "b1"



            elif ((((self.vale == 4) and (state.get_latest_player()== opp_val) ) and ((at == (2,4) and (to == (3,3))))) or (self.after_demar["b21"] == "b21")):
                a_act = cas_b (1)



            elif ((((self.vale == 4) and (state.get_latest_player()== opp_val) ) and ((at == (2,4) and (to == (3,4))))) or (self.after_demar["b22"] == "b22")):
                a_act = cas_b (2)



            elif ((((self.vale == 4) and (state.get_latest_player()== opp_val) ) and ((at == (3,2) and (to == (2,2))))) or (self.after_demar["c"] == "c")):
                a_act = cas_b (3)


            elif ((((self.vale == 4) and (state.get_latest_player()== opp_val) ) and ((at == (3,1) and (to == (2,2))))) or (self.after_demar["d"] == "d")):
                a_act = cas_a (2)
                self.after_demar["e1"] = "d"
                self.after_demar["e2"] = "d"



            elif ((((self.vale == 4) and (state.get_latest_player()== opp_val) ) and ((at == (2,1) and (to == (2,2))))) or (self.after_demar["e1"] == "e1")):
                a_act = cas_a (2)
                self.after_demar["d"] = "e1"
                self.after_demar["e2"] = "e1"



            elif ((((self.vale == 4) and (state.get_latest_player()== opp_val) ) and ((at == (2,1) and (to == (1,1))))) or (self.after_demar["e2"] == "e2")):
                a_act = cas_a (2)
                self.after_demar["d"] = "e2"
                self.after_demar["e1"] = "e2"



            
            else:
                a_act = core(player, state)

            return a_act


        def actions(player, state):

            self.vale += 1 
            
            if ((self.vale == 1) and (state.get_latest_player () is not None) ):

                self.vale = -2
                return demarage_def (state, player)
            elif self.vale == -1 :
                self.vale = -2
                return core (player, state)
            elif self.vale <= 1 :
                return demarage(state, player)
            elif self.vale > 1 :
                self.vale = -2
                return core (player, state)
            
                   
        action = actions(self.position,state)
        return action 