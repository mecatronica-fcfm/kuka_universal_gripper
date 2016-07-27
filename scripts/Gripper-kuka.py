#!/usr/bin/env python
import rospy
from kuka_driver.kuka_commander import KukaCommander
from gripper_cmd import Gripper

if __name__=='__main__':

  #iniciando nodos
  rospy.init_node('kuka_commander')
  rospy.init_node('gripper_commander', anonymous=True)

  kuka = KukaCommander()  
  kuka.set_vel(60)
  kuka.home()

  rate = rospy.Rate(1) # 1hz
  gripper= Gripper()
  gripper.start()


  #llegar al objeto 
  # kuka.ptp toma 6 angulos
  rospy.sleep(0.5)
  kuka.ptp([])
  rospy.sleep(0.5)
  kuka.ptp([]) 
  rospy.sleep(0.5)

  #tomar objeto
  gripper.close()
  rospy.sleep() # tiempo de espera para que lo tome 

  #manipulación del objeto 
  kuka.ptp([])
  rospy.sleep()
  (...)

  #soltar objeto 
  gripper.open()

  rospy.sleep([])

  gripper.shutdown()
  kuka.home()