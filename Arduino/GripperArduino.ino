#include <ros.h>
#include <std_msgs/Bool.h>
#include <kuka_universal_gripper/state_msg.h>

const int relepin=14;
long delta=200;
long last_time=0;

void gripper_cb( const std_msgs::Bool& cmd){ 
  if(cmd.data)
  {
    digitalWrite(relepin, HIGH);
  }
  else
  {
    digitalWrite(relepin, LOW);
  }
}

ros::NodeHandle  nh;
ros::Subscriber<std_msgs::Bool> sub("gripper_cmd" , gripper_cb);

kuka_universal_gripper::state_msg state_msg;
ros::Publisher gripper_state("gripper_state", &state_msg);

void setup()

{
    pinMode(relepin, OUTPUT); 
    nh.initNode();
    nh.subscribe(sub);
    nh.advertise(gripper_state);
    last_time=millis(); 
}

void loop()
{

   if (millis()-last_time > delta) {
     last_time=millis();
     state_msg.state=(bool)digitalRead(relepin);
     state_msg.time = last_time;
     gripper_state.publish(&state_msg);
   }
   nh.spinOnce();
 
}

