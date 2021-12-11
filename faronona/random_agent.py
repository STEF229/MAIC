
from faronona.faronona_player import FarononaPlayer
from faronona.faronona_rules import FarononaRules
from faronona.faronona_action import FarononaAction
from faronona.faronona_action import FarononaActionType
import random, copy , json

#  python main.py -ai0 ./faronona/random_agent.py -ai1 ./faronona/horus_agent.py -s 1 -t 1
#  python main.py -ai0 ./faronona/horus_agent.py -ai1 ./faronona/random_agent.py -s 1 -t 1

class AI(FarononaPlayer):

    name = "War of Hearts"
    valeu = 0

    def __init__(self, color):
        super(AI, self).__init__(self.name, color)
        self.position = color.value

    def play(self, state, remain_time):
        self.valeu += 1 
            
        if ((self.valeu == 1) and (state.get_latest_player() is None) ):
            at, to = (1,5), (2,4)
            action = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
        else:
            #Retrieve a random action
            # states = copy.deepcopy(state)
            action = FarononaRules.random_play(state, self.position)
            # test, a_ = FarononaRules.make_move(states,action,self.position)
            
            # states = json.loads(states.get_json_state())["board"]
            # # # # states = 
            # # test = json.loads(test.get_json_state())["board"]
            # # # test = test[1]
            # x = json.loads(state.get_json_state())["board"]
            # if states == x :
            #     print (" equal")
            # # elif test == states :
            # #     print("equal after", test , "\n\n", states, "\n\n" )
            # else:
            #     print("not equal", state , "\n\n", states)
            # #Extract departure and arrival of the piece
            actionDict = action.get_action_as_dict()
            at = actionDict['action']['at']
            to = actionDict['action']['to']
            #check if it is a win move both for approach and remote
            if (FarononaRules.is_win_approach_move(at, to, state, self.position) is not None) and (FarononaRules.is_win_remote_move(at, to, state, self.position) is not None) and len(FarononaRules.is_win_approach_move(at, to, state, self.position)) != 0 and len(FarononaRules.is_win_remote_move(at, to, state, self.position)) != 0:
                # between win approach and win remoate, check which can let me gain the more adverse pieces
                if len(FarononaRules.is_win_approach_move(at, to, state, self.position)) < len(FarononaRules.is_win_remote_move(at, to, state, self.position)):
                    action = FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=at, to=to)
                else: 
                    action = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=at, to=to)
        return action 