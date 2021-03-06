#!/usr/bin/env python3
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import speech_recognition as sr
from subprocess import call


r = sr.Recognizer()


def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    with sr.Microphone() as source:
        #call(["espeak","-s140 -ven+18 -z","Where Should I go ?"])
        print("Where Should I go ?")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    #print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    data = r.recognize_google(audio)
    data = data.lower()
    print("Sphinx thinks you said " + data)
    place = ""
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    if 'living room' in data:
        #call(["espeak","-s140 -ven+18 -z","Going to room1"])
        goal.target_pose.pose.position.x = 3.4
        goal.target_pose.pose.position.y = -1.5
        goal.target_pose.pose.orientation.w =  1
        client.send_goal(goal) 
        place="living room"       

    elif 'kitchen' in data:
        #call(["espeak","-s140 -ven+18 -z","Going to room2"])
        goal.target_pose.pose.position.x = 3.34
        goal.target_pose.pose.position.y = 1.07
        goal.target_pose.pose.orientation.w =  1
        client.send_goal(goal)
        place="kitchen"

    elif 'toilet' in data:
        #call(["espeak","-s140 -ven+18 -z","Going to room3"])
        goal.target_pose.pose.position.x = -0.05
        goal.target_pose.pose.position.y = 2.04
        goal.target_pose.pose.orientation.w =  1
        client.send_goal(goal)
        place="toilet"

    elif 'bedroom' in data:
        #call(["espeak","-s140 -ven+18 -z","Going to room4"])
        goal.target_pose.pose.position.x = -2.22
        goal.target_pose.pose.position.y = 1.18
        goal.target_pose.pose.orientation.w = 1
        client.send_goal(goal)
        place="bedroom"

    else:
        print("No Goal")

    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result(),place

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        while not rospy.is_shutdown():
            result,pl = movebase_client()
            if result:
                rospy.loginfo("Goal execution done!")
                text="Reached to" + pl
                #call(["espeak","-s140 -ven+18 -z",text])


    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")