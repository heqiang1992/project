#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
import time

#废弃

class macro(object):
    def __init__(self):
        print("screen ratio:%s%s" % pyautogui.size())

        def mouse_action(self, **param):

            if param.has_key("click") and param.has_key("coor"):
                pyautogui.moveTo(param["coor"][0], param["coor"][1], duration=1)
            elif param.has_key("click") and param.has_key("coor"):
                pyautogui.click(param["coor"][0], param["coor"][1])
            elif param.has_key("click") and not param.has_key("coor"):
                pyautogui.click()

        def key_board(self, **param):
            # param typelist,
            # param durationlist,
            # param hot,True or False
            # pyautogui.typewrite("hello word!")
            # pyautogui.hotkey('v','a','x') pyautogui.press()

            if param.has_key("hot") and param["hot"] == True:
                num = len(param["typelist"])
                if num == 2:
                    pyautogui.hotkey(param["typelist"][0], param["typelist"][1])
                elif num == 3:
                    pyautogui.hotkey(param["typelist"][0], param["typelist"][1], param["typelist"][2])
                else:
                    raise Exception("hotkey just support most 3keys.")
            else:
                if len(param["durationlist"]) == len(param["typelist"]):
                    for index, sec in enumerate(param["durationlist"]):
                        if sec != 0: time.sleep(float(sec))
                        pyautogui.typewrite(param["typelist"][index])
                else:
                    raise Exception("KEY AND INTERVAL DONT MATCH.")


if __name__ == "__main__":
    pass
