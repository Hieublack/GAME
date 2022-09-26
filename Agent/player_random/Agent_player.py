import numpy as np

import os
import sys
from base.Century.env import amount_action, amount_player, get_list_action_old, normal_main
from main import game_name
sys.path.append(os.path.abspath(f"base/{game_name}"))
from env import *

# def test(p_state, temp_file, per_file):
#     arr_action = get_list_action(p_state)
#     act_idx = np.random.randint(0, len(arr_action))
#     return arr_action[act_idx], temp_file, per_file


def test(player_state, file_temp, file_per):

    list_action = get_list_action(player_state)
    c = np.where(list_action == 1)[0]
    b = get_list_action_old(player_state)

    action = int(np.random.choice(b))
    # print(c,b,action)
    if len(np.setdiff1d(b,c)) != 0 and len(np.setdiff1d(c,b)) != 0:
        raise Exception('toang action')
    # print(list_action)
    if check_victory(player_state) == -1:
        # print('chưa hết game')
        pass
    else:
        if check_victory(player_state) == 1:
            # print('win')
            pass
        else:
            # print('lose')
            pass
    
    return action, file_temp, file_per

def train(x):
    list_player = [test]*amount_player()
    result, dt1 = normal_main(list_player, 1000, [0])
    print(result)
    print('DONE')
    