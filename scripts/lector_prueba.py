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
		if orden[0]=="F":
			rospy.loginfo("fin")
			print("fin")

			break

		if orden[0:2]=="KH":
			#kuka.home()
			rospy.sleep(0.5)
			rospy.loginfo("Kuka Home")
			rospy.sleep(1.0)

		if orden[0:2]=="KV":
			#kuka.set_vel(int(orden[3:5]))
			rospy.loginfo("vel:"+ orden[3:5])
			rospy.sleep(0.5)

		if orden[0]=="#":
			print(orden)
			pass

		if orden[0:2]=="GO":
			gripper.open()
			rospy.loginfo("go")
			rospy.sleep(2.0)

		if orden[0:2]=="GC":
			gripper.close()
			rospy.loginfo("gc")
			rospy.sleep(2.0)

		if orden[0:2]=="RS":
			#rospy.sleep(float(orden[3:(len(orden))]))
			print("sleep"+ orden[3:(len(orden))])

		if orden[0]=="[":
			punto=map(float,orden[1:len(orden)-2].split( ','))
			rospy.loginfo("kuka.ptp("+str(punto)+")")
			rospy.sleep(0.5)
		else:
			pass

	print("rutina finalizada")
	Rutina.close()
	gripper.shutdown()

if __name__ == '__main__': 
    try:
        main()
    except rospy.ROSInterruptException:
        pass