
from core import player , Color
from faronona.faronona_player import FarononaPlayer
from faronona.faronona_rules import FarononaRules
from faronona.faronona_action import FarononaAction
from faronona.faronona_action import FarononaActionType
import random, copy, json

#  python main.py -ai0 ./faronona/random_agent.py -ai1 ./faronona/horus_agent.py -s 1 -t 1
#  python main.py -ai0 ./faronona/horus_agent.py -ai1 ./faronona/random_agent.py -s 1 -t 1
#  python main.py -ai0 ./faronona/alpha.py -ai1 ./faronona/random_agent.py -s 1 -t 1

class AI(FarononaPlayer):

    name = "alpha_beta"
    vale = 0

    def __init__(self, color):
        super(AI, self).__init__(self.name, color)
        self.position = color.value

    def play(self, state, remain_time):

        def all_move(stat,move, player, adver_die):

            mov = move.get_action_as_dict()
            at = mov['action']['at']
            to = mov['action']['to']
            a = 0
            b = 0
            results_o, results_a, results_b = [],[], []
            opp_val = -player
            print("########### all_move #############", at, to )
            # print("########### all_move #############")
            results = []
            if (FarononaRules.is_win_approach_move(at, to, stat, player) is not None) and (len(FarononaRules.is_win_approach_move(at, to, stat, player)) != 0):
                
            # between win approach and win remoate, check which can let me gain the more adverse pieces
                a = len(FarononaRules.is_win_approach_move(at, to, stat,player))
                next_state, _a = FarononaRules.make_move(stat,move,player)
                adver_die += a
                possible_m = FarononaRules.get_effective_cell_moves(next_state,to)
                board = stat.get_board()
                fa = FarononaRules.get_player_actions(next_state,player)
                
                
                # for m in possible_m :
                #     t = board.is_empty_cell(m)
                #     if t:
                # get_effective_cell_moves
                
                
                # if  self.vale == 1:
                #     next_player = opp_val
                if len(fa)== 0:
                    # print("#######",next_state.winmove)
                    next_state.winmove = None 
                    next_state.set_next_player(player * -1) 
                    # print("#######", next_state.winmove)
                    next_player = opp_val
                else:
                    next_player = next_state.get_next_player()

                # print("########## APPROACH ###########",next_state.get_next_player(), player, opp_val, fa )
                # next_moves = FarononaRules.get_player_actions(next_state, next_player)
                # print("########## next ###########",a,next_moves)
                

                if next_player == player:
                    next_moves = FarononaRules.get_player_actions(next_state, next_player)
                    # print("###### equal ##########", next_moves)
                    results_a = []
                    for action in next_moves :
                        attendu  = all_move(next_state,action, player, adver_die)
                        for attend in attendu: 
                            results_a.append(attend)
                    # print("########## next ###########",a,next_moves)
                
                else:
                    # print("########## not equal ###########",next_state.get_next_player() , player, opp_val, fa )
                    
                    results_a = [{"state": next_state, "adver_die": adver_die }]
            
            
                
            #         a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
            

            # print("############## check remote ######################")
            # print("type at et at", type(at), at)
            # print("type to et to", type(to), to)
            # print("type at", type(at[0]) ,type(at[1]) )
            # print("type to", type(to[0]) , type(to[1]))
            # print("############## check remote ######################")

            if (FarononaRules.is_win_remote_move(at, to, stat, player) is not None) and (len(FarononaRules.is_win_remote_move(at, to, stat, player)) != 0):
                b = len(FarononaRules.is_win_remote_move(at, to, stat,player))
                next_state, _a = FarononaRules.make_move(stat,move,player)
                adver_die += b

                fb = FarononaRules.get_player_actions(next_state,player)

                if len(fb)== 0:
                    # print("#######",next_state.winmove)
                    next_state.winmove = None 
                    next_state.set_next_player(player * -1) 
                    # print("#######", next_state.winmove)
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


        def evaluate(stats,player):
            
            opposant= {"1":-1, "-1":1}
            opp_val = opposant[str(player)]
            info_adv = stats.get_player_info(opp_val)
            adver_token_restant = int(info_adv["on_board"])
            info_me = stats.get_player_info(player)
            me_token_restant = int(info_me["on_board"])

            print("########### EVA ###########")
            # special grid coordinates that have position advantage
            
            for x in [(1, 1), (1, 3), (3, 1), (3, 3),(1,5),(3,5),(1,7),(3,7)]:
                if stats.get_board().get_cell_color(x) == Color(player):
                    me_token_restant += 0.5
                if stats.get_board().get_cell_color(x) == Color(opp_val):
                    adver_token_restant += 0.5
           
            if stats.get_board().get_cell_color((2,4)) == Color(player):
                me_token_restant += 5
            if stats.get_board().get_cell_color((2,4)) == Color(opp_val):
                me_token_restant += 5

            z = me_token_restant-adver_token_restant
            return z

        # def alpha_beta(state, player, alpha , beta, depht ):
            
        #     global move_val
        #     # action_to_do = 0
            
        #     #verifier si game over ou profondeur atteint
        #     print("player", player)
        #     print(state.get_next_player())
        #     possible_move = FarononaRules.get_player_actions(state,player)
        #     if  ( depht == 0):
        #         return evaluate(state,player)
        #     # print("############possible move ############",  possible_move )
        #     print("########### depht ###########",depht)


        #     # if player == -1:
        #     #     for move in possible_move:
        #     #         if FarononaRules.is_legal_move(state, move , player):
        #     #             results = all_move(state,move, player, adver_die = 0)
        #     #             if len(results != 0):
        #     #                 for result in results:
        #     #                     score = alpha_beta()


        #     # print(possible_move)
        #     if player == - 1:
        #         valu = float("-inf")
        #         best_move = 0
        #         for move in possible_move:
        #             print("########### player -1 *************** ###########")
        #             # if FarononaRules.is_legal_move(state, move , player):
        #             results = all_move(state,move, player, adver_die = 0)
        #             # print("########### result depht player move ###########" , results,depht,player, move )
        #             res = []
        #             test = []
        #             for result in results:
        #                 next_state = result["state"]
        #                 score = alpha_beta(next_state, -player, alpha, beta, depht-1)[1]
        #                 res.append(score)
        #                 test.append(next_state)
        #             x = max(res)
        #             if x > valu:
        #                 valu = x
        #                 best_move = test[res.index(x)]
        #             alpha = max(alpha,valu)
        #             if alpha >= beta:
        #                 break
        #         print( "AZERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR    ", best_move)
        #         return best_move, valu
                        

        #     if player == 1:
        #         valu = float("inf")
        #         best_move = 0
        #         for move in possible_move:
        #             print("########### player 1 *************** ###########")
        #             if FarononaRules.is_legal_move(state, move , player):
        #             results = all_move(state,move, player, adver_die = 0)
        #             # print("########### result depht player move ###########" , results,depht,player, move )
        #             res = []
        #             test = []
        #             for result in results:
        #                 next_state = result["state"]
        #                 score = alpha_beta(next_state, -player, alpha, beta, depht-1)[1]
        #                 res.append(score)
        #                 test.append(next_state)
        #             x = min(res)
        #             if x < valu:
        #                 valu = x
        #                 best_move = test[res.index(x)]
        #             beta = min(beta,valu)
        #             if alpha >= beta:
        #                 break
        #         print( "AZERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR    ", best_move)
        #         return best_move, valu    
        #                 #     # adver_die = result["adver_die"]
        #                 #     # next_state, _a = FarononaRules.make_move(state,move,player)
        #                 #     print("******** A B ********", alpha,beta , depht)
        #                 #     score = -alpha_beta(next_state,-player, -beta, -alpha, depht-1)
        #                 #     print("########## score ############",move,score,alpha,beta)
        #                 #     if (score >= alpha):
                                
        #                 #         alpha = score
        #                 #         move_val = move
        #                 #         print("########## score ############",move,score,alpha,beta)
        #                 # if (alpha >= beta):
        #                 #     print("############# fin #########" , alpha, beta, score)
        #                 #     break

                # return alpha
            
        def a5 (state , player,alpha, beta):
            possible_move = FarononaRules.get_player_actions(state,player)
            movemt = []
            test_state = copy.deepcopy(state)
            
            if player == -1 :
                xss = []
                az = []
                count = 0
                for move in possible_move:
                    count += 1
                    print(f"############## count {count}######################", FarononaRules.get_player_actions(state,player))
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

                                print("********** call a4 *******************")
                                if a4(next_state,-player, alpha, beta) is not None:
                                    c.append(a4(next_state,-player, alpha, beta))
                                    print("********** call success *******************")
                                
                            if len (c) != 0 :
                                x = max(c)
                        xss.append(x)
                        az.append(move)
                    print(f"############## count {count} END MOVE ######################", move , xss)
                print(f"############## count {az[xss.index(max(xss))]} {xss} {move} END MOVE ######################")
                return  az[xss.index(max(xss))]

            if player == 1 :
                xss = []
                for move in possible_move:
                    x = None
                    if FarononaRules.is_legal_move(state, move , player):
                        results = all_move(state,move, player, adver_die = 0)
                        if len (results) != 0:
                            c = []
                            for result in results:
                                next_state = result["state"]
                                if a4(next_state,-player, alpha, beta) is not None:
                                    c.append(a4(next_state,-player,alpha, beta))
                            if len (c) != 0 :
                                x = min(c)
                        if x is not None:
                            xss.append(x)
                if len (xss) != 0 :
                    return min(xss)
                else :
                    return None
        
        def a4 (states , player,alpha, beta):
            possible_move = FarononaRules.get_player_actions(states,player)
            test_states = copy.deepcopy(states)
            if player == 1 :
                xss = []
                for move in possible_move:
                    x = None
                    if FarononaRules.is_legal_move(states, move , player):
                        results = all_move(test_states,move, player, adver_die = 0)
                        if len (results) != 0:
                            c = []
                            for result in results:
                                next_state = result["state"]
                                tes = json.loads(next_state.get_json_state())["board"]
                                x = json.loads(states.get_json_state())["board"]
                                if x == tes:
                                    next_state, a_ = FarononaRules.make_move(next_state,move,player)
                                print("********** call a3 *******************")
                                if a1(next_state,-player) is not None:
                                    c.append(a1(next_state,-player))
                                    print("********** call a3  success *******************")
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
                for move in possible_move:
                    x = None
                    if FarononaRules.is_legal_move(state, move , player):
                        results = all_move(state,move, player, adver_die = 0)
                        if len (results) != 0:
                            c = []
                            for result in results:
                                next_state = result["state"]
                                if a3(next_state,-player ,alpha, beta) is not None:
                                    c.append(a3(next_state,-player,alpha, beta))
                            if len (c) != 0 :
                                x = max(c)
                        if x is not None:
                            xss.append(x)
                if len (xss) != 0 :
                    return max(xss)
                else :
                    return None
        
        
        def a3 (state_a3 , player,alpha, beta):
            possible_move = FarononaRules.get_player_actions(state_a3,player)
            test_state_a3 = copy.deepcopy(state_a3)
            if player == -1 :
                xss = []
                for move in possible_move:
                    x = None
                    if FarononaRules.is_legal_move(state_a3, move , player):
                        results = all_move(test_state_a3,move, player, adver_die = 0)
                        if len (results) != 0:
                            c = []
                            for result in results:
                                next_state = result["state"]
                                print("********** call a2 *******************")
                                if a2(next_state,-player, alpha, beta) is not None:
                                    c.append(a2(next_state,-player,alpha, beta))
                                    print("********** call a2 success *******************")
                            if len (c) != 0 :
                                x = max(c)
                        if x is not None:
                            xss.append(x)
                if len (xss) != 0 :
                    return max(xss)
                else :
                    return None

            if player == 1 :
                xss = []
                for move in possible_move:
                    x = None
                    if FarononaRules.is_legal_move(state, move , player):
                        results = all_move(state,move, player, adver_die = 0)
                        if len (results) != 0:
                            c = []
                            for result in results:
                                next_state = result["state"]
                                if a2(next_state,-player, alpha, beta) is not None:
                                    c.append(a2(next_state,-player,alpha, beta))
                            if len (c) != 0 :
                                x = min(c)
                        if x is not None:
                            xss.append(x)
                if len (xss) != 0 :
                    return min(xss)
                else :
                    return None
        
        
        
        def a2 (state_a2 , player,alpha, beta):
            
            possible_move = FarononaRules.get_player_actions(state_a2,player)
            test_state_a2 = copy.deepcopy(state_a2)
            if player == 1 :
                xss = []
                for move in possible_move:
                    x = None
                    if FarononaRules.is_legal_move(state_a2, move , player):
                        results = all_move(test_state_a2,move, player, adver_die = 0)
                        if len (results) != 0:
                            c = []
                            for result in results:
                                next_state = result["state"]
                                print("********** call a1 success *******************")
                                if a1(next_state,-player,alpha, beta) is not None:
                                    c.append(a1(next_state,-player,alpha, beta))
                                    print("********** call a1 success *******************")
                            
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
                for move in possible_move:
                    x = None
                    if FarononaRules.is_legal_move(state, move , player):
                        results = all_move(state,move, player, adver_die = 0)
                        if len (results) != 0:
                            c = []
                            for result in results:
                                next_state = result["state"]
                                if a1(next_state,-player) is not None:
                                    c.append(a1(next_state,-player))
                            if len (c) != 0 :
                                x = max(c)
                        if x is not None:
                            xss.append(x)
                
                if len (xss) != 0 :
                    return max(xss)
                else :
                    return None
        
        
        
        def a1 (state_a1 , player):
            possible_move = FarononaRules.get_player_actions(state_a1,player)
            test_state_a1 = copy.deepcopy(state_a1)
            if player == -1 :
                for move in possible_move:
                    if FarononaRules.is_legal_move(state_a1, move , player):
                        results = all_move(test_state_a1 ,move, player, adver_die = 0)
                        if len (results) != 0:
                            x = max([evaluate(y["state"],player) for y in results ])

                            return x
            if player == -1 :
                for move in possible_move:
                    if FarononaRules.is_legal_move(state, move , player):
                        results = all_move(state,move, player, adver_die = 0)
                        if len (results) != 0:
                            x = min([evaluate(y["state"],player) for y in results ])
                            return x
                    

                    



        self.vale += 1 
        player = self.position
        alpha  = float("-inf")
        beta = float("inf")
        # move_val = 0
        new_state = copy.deepcopy(state)
        # action = alpha_beta(new_state, player, alpha , beta, depht = 6)[0]
        return a5 (new_state,player , alpha, beta)