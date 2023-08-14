#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=False)
    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        if pub.get_num_connections() > 0:  # check if any subscribers are connected
            message_str = "Hi this is 93.5"
            rospy.loginfo(message_str)
            pub.publish(message_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
