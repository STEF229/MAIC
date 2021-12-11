
from core import player , Color
from faronona.faronona_player import FarononaPlayer
from faronona.faronona_rules import FarononaRules
from faronona.faronona_action import FarononaAction
from faronona.faronona_action import FarononaActionType
import random, copy

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




# def alpha_beta(state, player, alpha , beta, depht = 3):

#     #verifier si game over ou profondeur atteint
#     opposant= {"1":-1, "-1":1}
#     opp_val = opposant[str(player)]
#     info_adv = state.get_player_info(opp_val)
#     info_adv = int(info_adv["on_board"])
#     info_me = state.get_player_info(opp_val)
#     info_me = int(info_me["on_board"])
#     action_to_do = 0

#     if ((info_me == 0) or (info_adv == 0) or ( depht <= 0)):
#         print("RANDOMMMMMMMMMMMM")
#         action = FarononaRules.random_play(state, self.position)
#         #Extract departure and arrival of the piece
#         actionDict = action.get_action_as_dict()
#         at = actionDict['action']['at']
#         to = actionDict['action']['to']
#         #check if it is a win move both for approach and remote
#         if (FarononaRules.is_win_approach_move(at, to, state, self.position) is not None) and (FarononaRules.is_win_remote_move(at, to, state, self.position) is not None) and len(FarononaRules.is_win_approach_move(at, to, state, self.position)) != 0 and len(FarononaRules.is_win_remote_move(at, to, state, self.position)) != 0:
#             # between win approach and win remoate, check which can let me gain the more adverse pieces
#             if len(FarononaRules.is_win_approach_move(at, to, state, self.position)) < len(FarononaRules.is_win_remote_move(at, to, state, self.position)):
#                 action = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)
#             else: 
#                 action = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
#         return action 
#         # return 

#     possible_move = FarononaRules.get_player_actions(state,player)
#     for move in possible_move:
#         next_state = FarononaRules.act(state,move,player)
#         score = -alpha_beta(next_state,player, -beta, -alpha, depht-1)
#         if (score >= alpha):
#             alpha = score
#             action_to_do = move
#             if (alpha >= beta):
#                 break

#     return action_to_do
        

    






        def alpha_beta (state , player, alpha , beta):
            move_choose = {}
            is_cutoff = False
            depth_of_game_tree = 0
            total_node_generated = 0

            v = maxim(state, player, alpha, beta, 0)
            print (move_choose)
            return move_choose[v]



            

            AI_movable_token_table = get_movable_token_information(AI_token, main_grid, False)
            if AI_movable_token_table == {}:
                show_game_results('You Human', 'AI')

            start_grid_coord, end_grid_coord = alpha_beta_search(main_grid, -1, 1)

            make_move(AI_token, main_grid, start_grid_coord, end_grid_coord)
            draw_grid(main_grid)

        def all_move(state,move, player, adver_die):

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
                    if (FarononaRules.is_win_approach_move(at, to, state, player) is not None) and (len(FarononaRules.is_win_approach_move(at, to, state, player)) != 0):
                        
                    # between win approach and win remoate, check which can let me gain the more adverse pieces
                        a = len(FarononaRules.is_win_approach_move(at, to, state,player))
                        next_state, _a = FarononaRules.make_move(state,move,player)
                        adver_die += a
                        possible_m = FarononaRules.get_effective_cell_moves(next_state,to)
                        board = state.get_board()
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

                        print("########## APPROACH ###########",next_state.get_next_player(), player, opp_val, fa )
                        # next_moves = FarononaRules.get_player_actions(next_state, next_player)
                        # print("########## next ###########",a,next_moves)
                        

                        if next_player == player:
                            next_moves = FarononaRules.get_player_actions(next_state, next_player)
                            print("###### equal ##########", next_moves)
                            results_a = []
                            for action in next_moves :
                                attendu  = all_move(next_state,action, player, adver_die)
                                for attend in attendu: 
                                    results_a.append(attend)
                            print("########## next ###########",a,next_moves)
                        
                        else:
                            print("########## not equal ###########",next_state.get_next_player() , player, opp_val, fa )
                            results_a = [{"state": next_state, "adver_die": adver_die }]
                    
                    
                        
                    #         a_act = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
                    

                    # print("############## check remote ######################")
                    # print("type at et at", type(at), at)
                    # print("type to et to", type(to), to)
                    # print("type at", type(at[0]) ,type(at[1]) )
                    # print("type to", type(to[0]) , type(to[1]))
                    # print("############## check remote ######################")

                    if (FarononaRules.is_win_remote_move(at, to, state, player) is not None) and (len(FarononaRules.is_win_remote_move(at, to, state, player)) != 0):
                        b = len(FarononaRules.is_win_remote_move(at, to, state,player))
                        next_state, _a = FarononaRules.make_move(state,move,player)
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
                        results_o = [{"state": state, "adver_die": adver_die }] 
                    
                    results = results_a + results_b + results_o
                    return results


        def maxim (state, player, alpha, beta, depth):
            global total_node_generated
            total_node_generated += 1
            global move_choose
            global depth_of_game_tree

            if depth >= depth_of_game_tree:
                depth_of_game_tree = depth

            current_alpha = alpha
            current_beta = beta


            if terminal_test(state , player):
                print ("return since max_value terminated ")
                return utility(state , player)

            possible_move = FarononaRules.get_player_actions(state,player)
            current_v = float('-inf')
            for move in possible_move:
                print ("in max_value body, action is choose from ", move, '\n\n')
                if FarononaRules.is_legal_move(state, move , player):
                    results = all_move(state,move, player, adver_die = 0)
                    # print("########### result depht player move ###########" , results,depht,player, move )
                    for result in results:
                        next_state = result["state"]
                        v = minim(next_state, -player, current_alpha, current_beta, depth+1)
                        if v > current_v:
                            current_v = v
                            if depth == 0:
                                move_choose[current_v] = move

                            if current_v >= beta:
                                print ("return since max_value pruning: ", current_v)
                                return current_v
                            current_alpha = max(alpha, current_v)
            print ("return since all level done in max_value: ", current_v)
            return current_v
        # def alpha_beta_search(AI_state, minimum_utility, maximum_utility):

        #     global AI_current_action
        #     v = max_value(AI_state, minimum_utility, maximum_utility, 0)
        #     print (AI_current_action)
        #     return AI_current_action[v]


        # def max_value(AI_state, alpha, beta, depth):

        #     # global total_node_generated
        #     # total_node_generated += 1
        #     # global AI_current_action
        #     # global depth_of_game_tree
        #     # if depth >= depth_of_game_tree:
        #     #     depth_of_game_tree = depth

        #     # current_alpha = alpha
        #     # current_beta = beta


        #     # # if depth_of_game_tree >= 3:
        #     # #     is_cutoff = True
        #     # #     return evaluate_current_state(AI_state)
        #     # if terminal_test(AI_state):
        #     #     print "return since max_value terminated "
        #     #     return utility(AI_state)

        #     AI_movable_token_table = get_movable_token_information(AI_token, AI_state, False)
        #     current_v = float('-inf')
        #     for start_grid_coord in AI_movable_token_table.keys():
        #         for end_grid_coord in AI_movable_token_table[start_grid_coord].keys():
        #             print "in max_value body, action is choose from ", start_grid_coord, end_grid_coord, '\n\n'

        #             current_AI_state = copy.deepcopy(AI_state)
        #             result_state = make_move(AI_token, current_AI_state, start_grid_coord, end_grid_coord)

        #             v = min_value(result_state, current_alpha, current_beta, depth+1)
        #             if v > current_v:
        #                 current_v = v
        #                 if depth == 0:
        #                     AI_current_action[current_v] = (start_grid_coord, end_grid_coord)

        #                 if current_v >= beta:
        #                     print "return since max_value pruning: ", current_v
        #                     return current_v
        #                 current_alpha = max(alpha, current_v)
        #     print "return since all level done in max_value: ", current_v
        #     return current_v

        def minim (state, player , alpha, beta, depth):
            global total_node_generated, is_cutoff
            total_node_generated += 1
            global move_choose
            global depth_of_game_tree

            if depth >= depth_of_game_tree:
                depth_of_game_tree = depth

            current_alpha = alpha
            current_beta = beta


            if depth >= 6:   # cutoff setting, maximum level AI can search through
            # if depth_of_game_tree >= 500:
                return evaluate(state , player)
            if terminal_test(state , player):
                print ("return since terminated")
                return utility(state , player)

            possible_move = FarononaRules.get_player_actions(state,player)
            current_v = float('inf')
            for move in possible_move:
                print ("in min_value body, action is choose from ", move, '\n\n')
                if FarononaRules.is_legal_move(state, move , player):
                    results = all_move(state,move, player, adver_die = 0)
                    # print("########### result depht player move ###########" , results,depht,player, move )
                    for result in results:
                        next_state = result["state"]
                        v = maxim(next_state, -player, current_alpha, current_beta, depth+1)
                        if v < current_v:
                            current_v = v
                            if current_v <= alpha:
                                print ("return since min_value pruning: ", current_v)
                                return current_v
                            current_beta = min(beta, current_v)

            print ("return since all level done in min_value: ", current_v)
            return current_v

        # def min_value(AI_state, alpha, beta, depth):

        #     global total_node_generated, is_cutoff, difficulty
        #     total_node_generated += 1

        #     global depth_of_game_tree
        #     if depth > depth_of_game_tree:
        #         depth_of_game_tree = depth

        #     current_alpha = alpha
        #     current_beta = beta


        #     if depth >= int(difficulty):   # cutoff setting, maximum level AI can search through
        #     # if depth_of_game_tree >= 500:
        #         is_cutoff = True
        #         return evaluate_current_state(AI_state)
        #     if terminal_test(AI_state):
        #         print "return since terminated"
        #         return utility(AI_state)


        #     AI_movable_token_table = get_movable_token_information(human_token, AI_state, False)

        #     current_v = float('inf')
        #     for start_grid_coord in AI_movable_token_table.keys():
        #         for end_grid_coord in AI_movable_token_table[start_grid_coord].keys():
        #             print "in min_value body, action is choose from ", start_grid_coord, end_grid_coord, '\n\n'

        #             current_human_state = copy.deepcopy(AI_state)
        #             result_state = make_move(human_token, current_human_state, start_grid_coord, end_grid_coord)

        #             v = max_value(result_state, current_alpha, current_beta, depth+1)
        #             if v < current_v:

        #                 current_v = v

        #                 if current_v <= alpha:
        #                     print "return since min_value pruning: ", current_v
        #                     return current_v
        #                 current_beta = min(beta, current_v)

        #     print "return since all level done in min_value: ", current_v
        #     return current_v


        def terminal_test(state , player):

            opposant= {"1":-1, "-1":1}
            opp_val = opposant[str(player)]
            info_adv = state.get_player_info(opp_val)
            adver_token_restant = int(info_adv["on_board"])
            info_me = state.get_player_info(opp_val)
            me_token_restant = int(info_me["on_board"])


            if me_token_restant == 0 or adver_token_restant == 0:
                return True
            else:
                return False


        def utility(state , player):
            print ("when utility is called, AI_state is terminated to results.\n")
            print ("before setting depth of game tree to zero, and store it in a collector\n")

            opposant= {"1":-1, "-1":1}
            opp_val = opposant[str(player)]
            info_adv = state.get_player_info(opp_val)
            adver_token_restant = int(info_adv["on_board"])
            info_me = state.get_player_info(opp_val)
            me_token_restant = int(info_me["on_board"])

            if me_token_restant == 0:
                print ("AI left nothing\n")
                return -1
            elif adver_token_restant == 0:
                print ("human left nothing")
                return 1


        def evaluate(state,player):
                    
            opposant= {"1":-1, "-1":1}
            opp_val = opposant[str(player)]
            info_adv = state.get_player_info(opp_val)
            adver_token_restant = int(info_adv["on_board"])
            info_me = state.get_player_info(opp_val)
            me_token_restant = int(info_me["on_board"])

            print("########### EVA ###########")
            # special grid coordinates that have position advantage
            
            for x in [(1, 1), (1, 3), (3, 1), (3, 3),(1,5),(3,5),(1,7),(3,7)]:
                if state.get_board().get_cell_color(x) == Color(player):
                    me_token_restant += 0.5
                if state.get_board().get_cell_color(x) == Color(opp_val):
                    adver_token_restant += 0.5


            return (me_token_restant-adver_token_restant) * 1.0 / (me_token_restant+adver_token_restant)


        self.vale += 1 
        player = self.position
        alpha = -1
        beta = 1
        # move_val = 0
        new_state = copy.deepcopy(state)
        action = alpha_beta(new_state, player, alpha , beta)
        return action