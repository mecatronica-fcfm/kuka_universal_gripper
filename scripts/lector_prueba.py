#!/usr/bin/env python
import rospy
from kuka_driver.kuka_commander import KukaCommander
from kuka_universal_gripper.gripper_interface import Gripper

def main():
	rospy.init_node('gripper')
	#kuka = KukaCommander()  
	#kuka.set_vel(60)
	#kuka.home()

	rate = rospy.Rate(1) # 1hz
	gripper= Gripper()
	gripper.start()

	NombreRutina=raw_input("Ingrese nombre de la rutina a seguir: ")

	print(" Realizando Rutina: "+ NombreRutina)
	
	Rutina=open(NombreRutina+".txt","r")
	for orden in Rutina:
		if orden[0:3]=="fin":
			print("fin")
			break

		if orden[0:2]=="KH":
			print("kuka.home()")
			rospy.sleep(3.0)

		if orden[0:2]=="KV":
			#kuka.set_vel(int(orden[3:5]))
			rospy.loginfo("Velocidad Kuka : " + orden[3:5])
			rospy.sleep(1.0)

		if orden[0]=="#":
			pass

		if orden[0:4]=="open":
			gripper.open()
			rospy.loginfo("Gripper Open")
			rospy.sleep(3.0)

		if orden[0:5]=="close":
			gripper.close()
			rospy.loginfo("Gripper Close")
			rospy.sleep(1.0)


		if orden[0:5]=="sleep":
			rospy.sleep(float(orden[6:(len(orden))]))
			print("sleep:"+ str(orden[6:(len(orden))]))

		if orden[0:3]=="ptp":
			punto=map(float,orden[5:len(orden)-2].split( ','))
			print("kuka.ptp(punto)"+str(punto))
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