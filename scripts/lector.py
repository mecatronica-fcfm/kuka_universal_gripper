#!/usr/bin/env python
import rospy
from kuka_driver.kuka_commander import KukaCommander
from gripper_cmd import Gripper

def main():
	
	kuka = KukaCommander()  
	kuka.set_vel(60)
	kuka.home()

	rate = rospy.Rate(1) # 1hz
	gripper= Gripper()
	gripper.start()

	NombreRutina=raw_input("Ingrese nombre de la rutina a seguir: ")

	print(" Realizando Rutina: "+ NombreRutina)
	
	Rutina=open("NombreRutina","r")

	for orden in Rutina:
		if orden[0:2]=="fin":
			break

		if orden=="KH":
			kuka.home()
			rospy.sleep(0.5)

		if orden[0:1]=="KV":
			kuka.set_vel(int(orden[3:4]))

		if orden[0]=="#":
			pass

		if orden=="GO":
			gripper.open()

		if orden=="GC":
			gripper.close()

		if orden[0:1]=="RS":
			rospy.sleep(int(orden[3:4]))

		if orden[0]=="[":
			punto=map(float,orden[1:len(str)-1].split( ','))
			kuka.ptp(punto)
			rospy.sleep(0.5)
		else:
			pass

	Rutina.close()
	gripper.shutdown()

if __name__ == '__main__': 
    try:
        main()
    except rospy.ROSInterruptException:
        pass