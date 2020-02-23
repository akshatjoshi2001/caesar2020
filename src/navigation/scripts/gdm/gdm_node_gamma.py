#!/usr/bin/env python

import rospy
import threading, signal, sys
from gdm_server import GDMNode

class Frontend:
    def __init__ (self):
        self.node = GDMNode()
        signal.signal (signal.SIGINT, self.kill)
        self.node.load ([
            'sleep 1000',
            'goal 45 21',
            'sleep 3000',
            'nav 120 90',
        ])
        #self.node.begin()

        self.spin()

    def kill (self, signal=None, frame=None):
        self.node.kill()
        sys.exit(0)

    def spin (self):
        while not rospy.is_shutdown():
            try:
                inp = raw_input().strip()
            except EOFError:
                self.kill()
                return
            self.node.ctrl_server(inp)

Frontend()
