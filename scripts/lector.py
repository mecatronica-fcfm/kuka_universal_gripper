#!/usr/bin/env python
import rospy
from kuka_driver.kuka_commander import KukaCommander
from kuka_universal_gripper.gripper_interface  import Gripper

def main():
	rospy.init_node('asdasd')
	kuka = KukaCommander()  
	kuka.set_vel(40)
	kuka.home()

	rate = rospy.Rate(1) # 1hz
	gripper= Gripper()
	gripper.start()

	NombreRutina=raw_input("Ingrese nombre de la rutina a seguir: ")

	print(" Realizando Rutina: "+ NombreRutina)
	
	Rutina=open(NombreRutina + ".txt","r")

	for orden in Rutina:
		if orden[0:3]=="fin":
			rospy.loginfo("Fin de la Rutina")
			break

		if orden[0:2]=="KH":
			kuka.home()
			rospy.sleep(3.0)

		if orden[0:2]=="KV":
			kuka.set_vel(int(orden[3:5]))
			rospy.loginfo("Velocidad Kuka : " + orden[3:5])
			rospy.sleep(1.0)

		if orden[0]=="#":
			pass

		if orden[0:4]=="open":
			gripper.open()
			rospy.loginfo("Gripper Open")

		if orden[0:5]=="close":
			gripper.close()
			rospy.loginfo("Gripper Close")


		if orden[0:5]=="sleep":
			rospy.loginfo("sleep:"+ str(orden[6:(len(orden))]))
			rospy.sleep(float(orden[6:(len(orden))]))


		if orden[0:3]=="ptp":
			punto=map(float,orden[4:len(orden)-2].split( ','))
			kuka.ptp(punto)
			rospy.loginfo("kuka.ptp("+str(punto)+")")
			rospy.sleep(1.0)
		else:
			pass

	Rutina.close()
	gripper.shutdown()

if __name__ == '__main__': 
    try:
        main()
    except rospy.ROSInterruptException:
        pass