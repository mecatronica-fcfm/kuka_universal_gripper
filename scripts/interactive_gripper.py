#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

"""
Interactive markers for control gripper
"""


import rospy
from kuka_interface.marker import MarkerServer, OptionMarker, OptionMenu
from kuka_interface.interactive import KukaMarkerBaseController

# Gripper
from kuka_universal_gripper.gripper_interface import Gripper



class KukaGripperBaseController(KukaMarkerBaseController):
    def __init__(self):
        super(KukaGripperBaseController, self).__init__()
        self.gripper = Gripper()
        self.gripper.start()

        
    def _add_menu(self):
        # Get menu marker
        ptp_entry = OptionMenu()
        ptp_entry.marker_name = 'ik_marker'
        ptp_entry.entry_name = 'PTP'
        ptp_entry.callback = self.ptp

        self.marker_server.add_menu_entry(ptp_entry)

        # Close gripper
        close_entry = OptionMenu()
        close_entry.marker_name = 'ik_marker'
        close_entry.entry_name = 'Close gripper'
        close_entry.callback = self.gripper_close

        self.marker_server.add_menu_entry(close_entry)

        # Open gripper
        open_entry = OptionMenu()
        open_entry.marker_name = 'ik_marker'
        open_entry.entry_name = 'Open gripper'
        open_entry.callback = self.gripper_open

        self.marker_server.add_menu_entry(open_entry)

    def gripper_close(self, feedback):
        self.gripper.close()

    def gripper_open(self, feedback):
        self.gripper.open()

def main():
    rospy.init_node('marker_test')
    rospy.loginfo('Init marker_test')
    kuka_marker = KukaGripperBaseController()
    rospy.spin()

if __name__ == "__main__":
    main()
