import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion, Twist
from std_msgs.msg import String

class GoToPose():
    def __init__(self):

        self.goal_sent = False

        # initialize node
        rospy.init_node('asr_control', anonymous=False)
#        rospy.init_node("asr_control")

        # What to do if shut down (e.g. Ctrl-C or failure)
        rospy.on_shutdown(self.shutdown)

        # Tell the action client that we want to spin a thread by default
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("Wait for the action server to come up")

        # Allow up to 5 seconds for the action server to come up
        self.move_base.wait_for_server(rospy.Duration(5))

        # Initializing publisher with buffer size of 10 messages
        self.pub_ = rospy.Publisher("mobile_base/commands/velocity", Twist, queue_size=10)

        # Subscribe to kws output
        rospy.Subscriber("kws_data", String, self.parse_asr_result)
        rospy.spin()

    def goto(self, pos, quat):

        # Send a goal
        self.goal_sent = True
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000),
                                        Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))

        # Start moving
        self.move_base.send_goal(goal)

        # Allow TurtleBot up to 60 seconds to complete task
        success = self.move_base.wait_for_result(rospy.Duration(60)) 

        state = self.move_base.get_state()
        result = False

        if success and state == GoalStatus.SUCCEEDED:
            # We made it!
            result = True
        else:
            self.move_base.cancel_goal()

        self.goal_sent = False
        return result

    def parse_asr_result(self, detected_words):
        """Function to perform action on detected word"""
        quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.000, 'r4' : 1.000}
        if detected_words.data.find("go to room 1") > -1 or detected_words.data.find("geh in Zimmer 1") > -1:
            position = {'x': 15.5, 'y' : 31.1}
        elif detected_words.data.find("go to room 2") > -1 or detected_words.data.find("geh in Zimmer 2") > -1:
            position = {'x': 11.1, 'y' : 27.4}
        elif detected_words.data.find("go to room 3") > -1 or detected_words.data.find("geh in Zimmer 3") > -1:
            position = {'x': 6, 'y' : 23}
        elif detected_words.data.find("go to room 4") > -1 or detected_words.data.find("geh in Zimmer 4") > -1:
            position = {'x': 16.4, 'y' : 24.4}
        elif detected_words.data.find("go to room 5") > -1 or detected_words.data.find("geh in Zimmer 5") > -1:
            position = {'x': 14.3, 'y' : 21.6}
        elif detected_words.data.find("go to room 6") > -1 or detected_words.data.find("geh in Zimmer 6") > -1:
            position = {'x': 5.6, 'y' : 14.2}
        elif detected_words.data.find("go to room 7") > -1 or detected_words.data.find("geh in Zimmer 7") > -1:
            position = {'x': 24.3, 'y' : 13.2}
            success = goto(position, quaternion)
        elif detected_words.data.find("go to room 8") > -1 or detected_words.data.find("geh in Zimmer 8") > -1:
            position = {'x': 29.6, 'y' : 3}
        elif detected_words.data.find("go to room 9") > -1 or detected_words.data.find("geh in Zimmer 9") > -1:
            position = {'x': 38.4, 'y' : 19.8}
        elif detected_words.data.find("go to room 10") > -1 or detected_words.data.find("geh in Zimmer 10") > -1:
            position = {'x': 44.2, 'y' : 12.5}
        elif detected_words.data.find("go to room 11") > -1 or detected_words.data.find("geh in Zimmer 11") > -1:
            position = {'x': 47, 'y' : 8.3}
        elif detected_words.data.find("go to room 12") > -1 or detected_words.data.find("geh in Zimmer 12") > -1:
            position = {'x': 42.6, 'y' : 6.2}
        elif detected_words.data.find("go to boxroom") > -1 or detected_words.data.find("geh in die Abstellkammer") > -1:
            position = {'x': 32.7, 'y' : 6}    

#        elif detected_words.data.find("happy") > -1 or detected_words.data.find("glücklich") > -1:

#        elif detected_words.data.find("sad") > -1 or detected_words.data.find("traurig") > -1:

#        elif detected_words.data.find("surprised") > -1 or detected_words.data.find("überrascht") > -1:

#        elif detected_words.data.find("angry") > -1 or detected_words.data.find("wütend") > -1:

#        elif detected_words.data.find("excited") > -1 or detected_words.data.find("aufgeregt") > -1:

#        elif detected_words.data.find("expressionless") > -1 or detected_words.data.find("ausdruckslos") > -1:

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.loginfo("Stop")
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        navigation = GoToPose()
        success = navigation.goto(position, quaternion)
        # Sleep to give the last log messages time to be sent
        rospy.sleep(1)

    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")