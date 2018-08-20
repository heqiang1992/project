#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pythoncom
import pyHook
import win32api
from Macro import macro
from threading import Thread
from keysConfig import keysConfig


class e_hook(macro, Thread):
    def __init__(self, keyMap):
        super(macro, self).__init__()
        super(Thread, self).__init__()
        self.keyMap = keyMap

    def __OnMouseEvent(self, event):
        # called when a mouse event are received
        print "name", event.MessageName
        print "message", event.Message
        print "time", event.Time
        print "window", event.Window
        print "windowName", event.WindowName
        print "position", event.position
        print "wheel", event.Wheel
        print "inject", event.injected
        print "--------"

        return True

    def __OnKeyboardEvent(self, event):
        if event.Key in self.keyMap.keys():
            self.key_board(typelist=self.keyMap[event.Key]["typeKey"],
                           durationlist=self.keyMap[event.Key]["interval"])
        print "name", event.MessageName
        print "message", event.Message
        print "time", event.Time
        print "Ascii8", event.Ascii, chr(event.Ascii)
        print "Key", event.eventKey
        print "keyID", event.KeyID
        print "Transition", event.Transition
        print "-------"

        if event.Key == "F12":
            self.stop_L()
        return True

    def run(self):

        # create a hook manager
        hm = pyHook.HookManager()
        # watch for all mouse events
        # hm.KeryDown = self.OnKeyboardEvent
        hm.SubscribeKeyDown(self.__OnKeyboardEvent)
        # set the hook
        hm.HookKeyboard()
        # wait forever
        pythoncom.PumpMessages()
        return True

    def stop_L(self):
        try:
            win32api.PostQuitMessage()
        except Exception as e:
            print(e)
        finally:
            return True


if __name__ == "__main__":
    t = e_hook(keysConfig())
    t.start()
