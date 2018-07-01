
import json
import requests
from pynput import keyboard
from pynput.keyboard import Key

SERVER_URL      = "localhost"
SERVER_PORT     = "10000"

class Client():

    def __init__(self):
        self.init_keyboard()
        self.init_network()
        self.init_game_info()

    def start(self):
        with keyboard.Listener(
            on_press=self.controller
        ) as key_listener:
            key_listener.join()

    def stop(self):
        keyboard.Listener.stop(None)

    """
    communication protocal:
    {
        "gameID": gameid,
        "userID": userid,
        "action": action,
        "gameMetrix": gameMetrix
    }
    **action** :
    space   ->  0
    up      ->  1
    down    ->  2
    left    ->  3
    right   ->  4
    """
    def controller(self, key):
        if key == Key.esc:
            self.stop()

        action = self.key_map.get(key, -1)
        if action >= 0:
            self.send_action(action)

    def send_action(self, action):
        req_data = {
            "gameID": self.game_id,
            "userID": self.user_id,
            "action": action,
            "gameMetrix": self.tetris_metrix
        }
        URL = "http://" + SERVER_URL + ":" + SERVER_PORT
        r = requests.post(URL, data=json.dumps(req_data))

        # TODO
        print(r.text)

    def init_network(self):
        pass

    def init_game_info(self):
        self.game_id = "gameid"
        self.user_id = "userid"

        self.tetris_metrix = []


    def init_keyboard(self):
        self.key_map = {
            Key.space   :   0,
            Key.up      :   1,
            Key.down    :   2,
            Key.left    :   3,
            Key.right   :   4
        }



if __name__ == "__main__":
    pass

