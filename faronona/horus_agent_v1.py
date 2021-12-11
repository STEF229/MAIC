
from core import rules , Color
from faronona.faronona_player import FarononaPlayer
from faronona.faronona_rules import FarononaRules
from faronona.faronona_action import FarononaAction
from faronona.faronona_action import FarononaActionType
import random , copy, json

#  python main.py -ai0 ./faronona/horus_agent.py -ai1 ./faronona/random_agent.py -s 1 -t 5


class AI(FarononaPlayer):

    name = "Horus: Dieu faucon"
    vale = 0 
    after_demar = {"a": 1, "b1": 1 , "b21": 1,"b22": 1, "c":1, "d":1 , "e1": 1 , "e2": 1 }

    def __init__(self, color):
        super(AI, self).__init__(self.name, color)
        self.position = color.value

    def play(self, state, remain_time):

        def demarage(state, player):
            opposant= {"1":-1, "-1":1}
            opp_val = opposant[str(player)]
            if ((self.vale == 1) and (state.get_latest_player() is None) ):
                at, to = (1,4), (2,4)
                a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)

            if ((self.vale == 2) and (state.get_latest_player()== opp_val) ):
                at, to = (2,5), (2,4)
                a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                next_state, _a = FarononaRules.make_move(state,a_act,player)


            if ((self.vale == 3) and (state.get_latest_player()== player) ):
                at, to = (2,4), (1,4)
                a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)

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


        def core (player, state):
            if self.vale == -2 :
                possible_move = FarononaRules.get_player_actions(state,player)
                if len (possible_move) == 1 :
                    return possible_move[0]
                else:
                    movemt = []
                    test_state = copy.deepcopy(state)
                    ans, b_ = best_move (test_state , player, possible_move)
                    if ans:
                        if player == -1 :
                            xss = []
                            az = []
                            count = 0
                            for move in possible_move:
                                count += 1

                                x = None
                                if FarononaRules.is_legal_move(state, move , player):
                                    results = all_move(test_state,move, player, adver_die = 0)
                                    if len (results) != 0:
                                        c = []
                                        for result in results:
                                            next_state = result["state"]
                                            test = json.loads(next_state.get_json_state())["board"]
                                            x = json.loads(state.get_json_state())["board"]
                                            if x == test:
                                                next_state, a_ = FarononaRules.make_move(next_state,move,player)

                                            if a1(next_state,-player) is not None:
                                                c.append(a1(next_state,-player))

                                            
                                        if len (c) != 0 :
                                            x = max(c)
                                    xss.append(x)
                                    az.append(move)
                            val = xss.count(max(xss))
                            if val == 1:
                                return  az[xss.index(max(xss))]
                            else:

                                x = [m for m in az if m.get_action_as_dict()['action']['to'] in [(1, 1), (1, 3), (3, 1), (3, 3),(1,5),(3,5),(1,7),(3,7),(2,4)]]

                                if len(x) != 0:
                                    return x[random.randint(0,len(x)-1)]
                                else:
                                    return az[xss.index(max(xss))]
                            
                        
                        if player == 1 :
                            xss = []
                            az = []
                            count = 0
                            for move in possible_move:
                                count += 1

                                x = None
                                if FarononaRules.is_legal_move(state, move , player):
                                    results = all_move(test_state,move, player, adver_die = 0)
                                    if len (results) != 0:
                                        c = []
                                        for result in results:
                                            next_state = result["state"]
                                            test = json.loads(next_state.get_json_state())["board"]
                                            x = json.loads(state.get_json_state())["board"]
                                            if x == test:
                                                next_state, a_ = FarononaRules.make_move(next_state,move,player)

                                            if a1(next_state,-player) is not None:
                                                c.append(a1(next_state,-player))
                                            
                                        if len (c) != 0 :
                                            x = max(c)
                                    xss.append(x)
                                    az.append(move)

                            return  az[xss.index(max(xss))]
                    else:
                        return b_
            else:
                alpha = float('-inf')
                beta = float('inf')

                possible_move = FarononaRules.get_player_actions(state,player)
                if len (possible_move) == 1 :
                    return possible_move[0]
                else:
                    movemt = []
                    test_state = copy.deepcopy(state)
                    ans, b_ = best_move (test_state , player, possible_move)
                    if ans:
                        if player == -1 :
                            xss = []
                            az = []
                            count = 0
                            for move in possible_move:
                                count += 1

                                x = None
                                if FarononaRules.is_legal_move(state, move , player):
                                    results = all_move(test_state,move, player, adver_die = 0)
                                    if len (results) != 0:
                                        c = []
                                        for result in results:
                                            next_state = result["state"]
                                            test = json.loads(next_state.get_json_state())["board"]
                                            x = json.loads(state.get_json_state())["board"]
                                            if x == test:
                                                next_state, a_ = FarononaRules.make_move(next_state,move,player)

                                            if a4(next_state,-player,alpha, beta) is not None:
                                                c.append(a4(next_state,-player,alpha, beta))

                                            
                                        if len (c) != 0 :
                                            x = max(c)
                                    xss.append(x)
                                    az.append(move)
                            val = xss.count(max(xss))
                            if val == 1:
                                return  az[xss.index(max(xss))]
                            else:

                                x = [m for m in az if m.get_action_as_dict()['action']['to'] in [(1, 1), (1, 3), (3, 1), (3, 3),(1,5),(3,5),(1,7),(3,7),(2,4)]]

                                if len(x) != 0:
                                    return x[random.randint(0,len(x)-1)]
                                else:
                                    return az[xss.index(max(xss))]
                            
                        
                        if player == 1 :
                            xss = []
                            az = []
                            count = 0
                            for move in possible_move:
                                count += 1

                                x = None
                                if FarononaRules.is_legal_move(state, move , player):
                                    results = all_move(test_state,move, player, adver_die = 0)
                                    if len (results) != 0:
                                        c = []
                                        for result in results:
                                            next_state = result["state"]
                                            test = json.loads(next_state.get_json_state())["board"]
                                            x = json.loads(state.get_json_state())["board"]
                                            if x == test:
                                                next_state, a_ = FarononaRules.make_move(next_state,move,player)

                                            if a4(next_state,-player,alpha, beta) is not None:
                                                c.append(a4(next_state,-player,alpha, beta))
                                            
                                        if len (c) != 0 :
                                            x = max(c)
                                    xss.append(x)
                                    az.append(move)

                            return  az[xss.index(max(xss))]
                    else:
                        return b_     

        def evaluate(stats,player):
            
            
            opp_val = -player
            info_adv = stats.get_player_info(opp_val)
            adver_token_restant = int(info_adv["on_board"])
            info_me = stats.get_player_info(player)
            me_token_restant = int(info_me["on_board"])

            # print("########### EVA ###########")
            # special grid coordinates that have position advantage
            
            for x in [(1, 1), (1, 3), (3, 1), (3, 3),(1,5),(3,5),(1,7),(3,7)]:
                if stats.get_board().get_cell_color(x) == Color(player):
                    me_token_restant += 0.5
                if stats.get_board().get_cell_color(x) == Color(opp_val):
                    adver_token_restant += 1
           
            # if stats.get_board().get_cell_color((2,4)) == Color(player):
            #     me_token_restant += 5
            # if stats.get_board().get_cell_color((2,4)) == Color(opp_val):
            #     me_token_restant += 5

            z = me_token_restant-adver_token_restant
            return z


        def best_move (stated , player, moves):
            for m in moves:
                if (FarononaRules.is_win_approach_move(m.get_action_as_dict()['action']['at'], m.get_action_as_dict()['action']['to'], stated, player) is not None and len(FarononaRules.is_win_approach_move(m.get_action_as_dict()['action']['at'], m.get_action_as_dict()['action']['to'], stated, player)) != 0):
                    return True, None
                if (FarononaRules.is_win_remote_move(m.get_action_as_dict()['action']['at'], m.get_action_as_dict()['action']['to'], stated, player) is not None and len(FarononaRules.is_win_remote_move(m.get_action_as_dict()['action']['at'], m.get_action_as_dict()['action']['to'], stated, player)) != 0):
                    return True, None
            x = [n for n in moves if n.get_action_as_dict()['action']['to'] in [(1, 1), (1, 3), (3, 1), (3, 3),(1,5),(3,5),(1,7),(3,7),(2,4)]]
            for mov in x :
                    next_state, _a = FarononaRules.make_move(stated,mov,player)
                    le_move = FarononaRules.get_player_actions(next_state, -player)
                    for t in le_move:
                        if (FarononaRules.is_win_approach_move(t.get_action_as_dict()['action']['at'], t.get_action_as_dict()['action']['to'], next_state, player) is not None and len(FarononaRules.is_win_approach_move(t.get_action_as_dict()['action']['at'], t.get_action_as_dict()['action']['to'], next_state, player)) != 0):
                            try:
                                x.remove(mov)
                            except:
                                pass
                        if (FarononaRules.is_win_remote_move(t.get_action_as_dict()['action']['at'], t.get_action_as_dict()['action']['to'], next_state, player) is not None and len(FarononaRules.is_win_remote_move(t.get_action_as_dict()['action']['at'], t.get_action_as_dict()['action']['to'], next_state, player)) != 0):
                            try:
                                x.remove(mov)
                            except:
                                pass
            if len(x) != 0:
                return False, x[random.randint(0,len(x)-1)]
            else:
                return False, moves[random.randint(0,len(moves)-1)]        

            
        
        def a4 (states , player,alpha, beta):
            possible_move = FarononaRules.get_player_actions(states,player)
            test_states = copy.deepcopy(states)
            if player == 1 :
                xss = []
                cur__alpha = float("inf")
                for move in possible_move:
                    x = None
                    if FarononaRules.is_legal_move(states, move , player):
                        results = all_move(test_states,move, player, adver_die = 0)
                        if len (results) != 0:
                            c = []
                            for result in results:
                                next_state = result["state"]
                                test = json.loads(next_state.get_json_state())["board"]
                                x = json.loads(states.get_json_state())["board"]
                                if x == test:
                                    next_state, a_ = FarononaRules.make_move(next_state,move,player)

                                if a1(next_state,-player) is not None:
                                    c.append(a1(next_state,-player))
                                    
                            if len (c) != 0 :
                                x = min(c)
                        if x is not None:
                            xss.append(x)
                if len (xss) != 0 :
                    return min(xss)
                else :
                    return None

            if player == -1 :
                xss = []
                cur__alpha = float("inf")
                for move in possible_move:
                    x = None
                    if FarononaRules.is_legal_move(states, move , player):
                        results = all_move(test_states,move, player, adver_die = 0)
                        if len (results) != 0:
                            c = []
                            for result in results:
                                next_state = result["state"]
                                test = json.loads(next_state.get_json_state())["board"]
                                x = json.loads(states.get_json_state())["board"]
                                if x == test:
                                    next_state, a_ = FarononaRules.make_move(next_state,move,player)

                                if a1(next_state,-player) is not None:
                                    c.append(a1(next_state,-player))
                                    

                            if len (c) != 0 :
                                x = min(c)
                        if x is not None:
                            xss.append(x)
                if len (xss) != 0 :
                    return min(xss)
                else :
                    return None

        def a1 (state_a1 , player):

            possible_move = FarononaRules.get_player_actions(state_a1,player)
            test_state_a1 = copy.deepcopy(state_a1)
            if player == -1 :
                xs = []
                for move in possible_move:
                    if FarononaRules.is_legal_move(state_a1, move , player):
                        results = all_move(test_state_a1 ,move, player, adver_die = 0)
                        if len (results) != 0:
                            c = []
                            for y in results:
                                next_state = y["state"]
                                test = json.loads(next_state.get_json_state())["board"]
                                x = json.loads(state_a1.get_json_state())["board"]
                                if x == test:
                                    next_state, a_ = FarononaRules.make_move(next_state,move,player)

                                c.append(evaluate(next_state ,player))

                            if len (c) != 0 :
                                xx = max(c)
                        if xx is not None:
                            xs.append(xx)
                if len (xs) != 0 :
                    return max(xs)
                else :
                    return None
            if player == 1 :
                xs = []
                for move in possible_move:
                    if FarononaRules.is_legal_move(state_a1, move , player):
                        results = all_move(test_state_a1 ,move, player, adver_die = 0)
                        if len (results) != 0:
                            c = []
                            for y in results:
                                next_state = y["state"]
                                test = json.loads(next_state.get_json_state())["board"]
                                x = json.loads(state_a1.get_json_state())["board"]
                                if x == test:
                                    next_state, a_ = FarononaRules.make_move(next_state,move,player)

                                c.append(evaluate(next_state ,player))

                            if len (c) != 0 :
                                xx = max(c)
                        if xx is not None:
                            xs.append(xx)
                if len (xs) != 0 :
                    return max(xs)
                else :
                    return None

        def all_move(stat,move, player, adver_die):

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
                adver_die += a
                possible_m = FarononaRules.get_effective_cell_moves(next_state,to)
                board = stat.get_board()
                fa = FarononaRules.get_player_actions(next_state,player)
                
                
                
                if len(fa)== 0:
                    next_state.winmove = None 
                    next_state.set_next_player(player * -1) 
                    next_player = opp_val
                else:
                    next_player = next_state.get_next_player()

               
                if next_player == player:
                    next_moves = FarononaRules.get_player_actions(next_state, next_player)

                    results_a = []
                    for action in next_moves :
                        attendu  = all_move(next_state,action, player, adver_die)
                        for attend in attendu: 
                            results_a.append(attend)

                
                else:

                    results_a = [{"state": next_state, "adver_die": adver_die }]
           

            if (FarononaRules.is_win_remote_move(at, to, stat, player) is not None) and (len(FarononaRules.is_win_remote_move(at, to, stat, player)) != 0):
                b = len(FarononaRules.is_win_remote_move(at, to, stat,player))
                next_state, _a = FarononaRules.make_move(stat,move,player)
                adver_die += b

                fb = FarononaRules.get_player_actions(next_state,player)

                if len(fb)== 0:

                    next_state.winmove = None 
                    next_state.set_next_player(player * -1) 

                    next_player = opp_val
                else:
                    next_player = next_state.get_next_player()


                if next_player == player:
                    next_moves = FarononaRules.get_player_actions(next_state, next_player)
                    results_b = []
                    for action in next_moves :
                        attendu  = all_move(next_state,action, player, adver_die)
                        for atten in attendu: 
                            results_b.append(atten)       
                 
                else:
                    results_b = [{"state": next_state, "adver_die": adver_die }]


            if a == 0 and b == 0:
                results_o = [{"state": stat, "adver_die": adver_die }] 
            
            results = results_a + results_b + results_o
            return results







        def after_demarage(state, player):

            opposant= {"1":-1, "-1":1}
            opp_val = opposant[str(player)]
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
                return core (player, state)
            elif self.vale == -1 :
                self.vale = -2
                return core (player, state)
            elif self.vale <= 3 :
                return demarage(state, player)
            elif self.vale > 3 :
                return after_demarage(state, player)
            
                   
        action = actions(self.position,state)
        return action 