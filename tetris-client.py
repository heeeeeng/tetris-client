
import json
import requests
import time
import queue
import threading
from pynput import keyboard
from pynput.keyboard import Key

SERVER_URL      = "localhost"
SERVER_PORT     = "10000"

class Client():

    def __init__(self):
        self.init_network()
        self.init_game_info()

        self.tasks = []

    def start(self):
        q = queue.Queue()

        gui = ClientGUI(q)
        t_gui = threading.Thread(target=gui.start)
        t_gui.daemon = True
        t_gui.start()

        controller = ClientController(q, self.game_id, self.user_id)
        t_ctrl = threading.Thread(target=controller.start)
        t_ctrl.daemon = True
        t_ctrl.start()

        self.tasks.append(gui)
        self.tasks.append(controller)

        q.get()
        self.stop()
            

    def stop(self):
        for t in self.tasks:
            t.stop()

    def init_network(self):
        pass

    def init_game_info(self):
        self.game_id = "gameid"
        self.user_id = "userid"

        self.tetris_metrix = []

    """
    communication protocal:
    {
        "gameID": gameid,
        "userID": userid,
        "action": action
    }
    **action** :
    space   ->  0
    up      ->  1
    down    ->  2
    left    ->  3
    right   ->  4
    """


class ClientGUI():

    def __init__(self, q):
        self.shoud_stop_q = q

        self.fps = 30
        self._is_running = True

    def start(self):
        
        while self._is_running:
            time.sleep(1 / self.fps)
            self.refresh()
            self.draw()

    def stop(self):
        self._is_running = False

    def refresh(self):
        pass

    def draw(self):
        pass


class ClientController():

    def __init__(self, q, gameid, userid):
        self.shoud_stop_q = q

        self.game_id = gameid
        self.user_id = userid

        self.init_keyboard()

    def start(self):
        with keyboard.Listener(
            on_press=self.controller
        ) as key_listener:
            key_listener.join()

    def stop(self):
        keyboard.Listener.stop(None)

    def controller(self, key):
        if key == Key.esc:
            self.shoud_stop_q.put(True)
            return

        action = self.key_map.get(key, -1)
        if action >= 0:
            self.send_action(action)

    def send_action(self, action):
        req_data = {
            "gameID": self.game_id,
            "userID": self.user_id,
            "action": action
        }
        # URL = "http://" + SERVER_URL + ":" + SERVER_PORT
        # r = requests.post(URL, data=json.dumps(req_data))

        # TODO
        # print(r.text)
        print(req_data)


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

