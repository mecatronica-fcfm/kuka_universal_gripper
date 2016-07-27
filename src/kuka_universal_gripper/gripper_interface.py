#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
from threading import Thread
from kuka_universal_gripper.msg import state_msg


class Gripper(object):
    def __init__(self, topic = '/gripper_cmd'):
        self.pub = rospy.Publisher('/gripper_cmd', Bool, queue_size=10)
        self.msg = Bool()
        # Publish msg on thread
        self.state_update_rate = 10
        self.is_running = True
        self.pub_thread = None

        self.sub = rospy.Subscriber('/gripper_state',state_msg,self.callback)
        self.state = False
        self.time = 0


    def start(self):
        self.pub_thread = Thread(target=self.update_state)
        self.pub_thread.start()
        
    def set(self, status = False):
        self.msg.data = status
        
    def close(self):
        self.set(True)

    def open(self):
        self.set(False)

    def update_state(self):
        rate = rospy.Rate(self.state_update_rate) 
        while not rospy.is_shutdown() and self.is_running:  
            self.pub.publish(self.msg)
            rate.sleep() 
    
    def shutdown(self):
        self.is_running=False

    def callback(self,data):
        self.state = data.state
        self.time = data.time
        rospy.logdebug("state: "+ str(data.state) + " | time: "+ str(data.time))

def main():  
    rospy.init_node('gripper_commander', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    gripper= Gripper()
    gripper.start()

    while not rospy.is_shutdown():
        gripper.close()        
        rospy.sleep(1.0)
        gripper.open()
        rospy.sleep(1.0)
    gripper.shutdown()

if __name__ == '__main__': 
    try:
        main()
    except rospy.ROSInterruptException:
        pass