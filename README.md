# FRA502-service-robot-navigation
This robot is moving base (by differential drive) &amp; 

All files used in this project

Use for | Package | Folder | File
------|----|----|-------
show default rviz | dd_sim | launch | config.rviz
launch robot on RVIZ | dd_sim | launch | dd_rviz.launch
launch robot on Gazebo & RVIZ | dd_sim | launch | dd_gazebo.launch
show hokuyo lidar | dd_sim | meshes | hokuyo.dae
show all obstacle in gazebo world | dd_sim | models | box_blue, box_green, box_orgage, box_red, cylinder_blue, cylinder_red
spawn world | dd_sim | world | dd_navi.world
show robot xacro model | dd_sim | urdf | dd_navi.xacro
camera plugin | dd_sim | urdf | camera.gazebo
lidar plugin | dd_sim | urdf | hokuyo.gazebo
differenial drive plugin | dd_sim | urdf | dd_gazebo_plugins.xacro
CMakeLists | dd_sim |  - | CMakeLists.txt
package | dd_sim| - | package.xml
launch control robot movement | dd_sim | launch| dd_control_teleop.launch
show gmapping rviz | dd_sim | rviz | gmapping.rviz
launch gmapping | dd_sim | launch | gmapping.launch
save created map | dd_sim | map | test2_map.pgm , test2_map.yaml
show navigation rviz | dd_sim | rviz | navigation.rviz
launch navigation | dd_sim | launch | amcl_move_base.launch
all parameter for navigation | dd_sim | param | costmap_common_params.yaml, dwa_local_planner_params, global_costmap_params.yaml, local_costmap_params.yaml, move_base_params.yaml
voice commanf program | dd_sim | script | dd_voice.py


## Simulation Phase I
**Step 1**, open first terminal and launch RVIZ by following this 
~~~~~~
$ roslaunch dd_sim dd_rviz.launch
~~~~~~
launch Gazebo 
~~~
$ roslaunch dd_sim dd_gazebo.launch
~~~

**Step 2**,open second terminal to show rostopic list
~~~
$ rostopic list
~~~
results will show 
~~~
/dd/camera1/image_raw
/dd/laser/scan
~~~

**Step 3**, open camera in the second terminal
~~~
$ rosrun image_view image_view image:=/dd/camera1/image_raw
~~~
if it works, output will be like this
~~~
[ INFO] [1634705652.284265008]: Initializing nodelet with 4 worker threads.

[ INFO] [1634705652.431830628]: Using transport "raw"
~~~
**if got a problem**
 1. close all terminals and open them again
 2. add more system base memory (in this case, virtualbox system base memory 13000 MB)

**Step 4**, open third terminal to launch this package for controlling robor arm
~~~
$ roslaunch dd_arm_control dd_control.launch
~~~

**Step 5**, open fourth terminal to see rostopic list 
~~~
$ rostopic list
~~~
the results will show 
~~~
/dd/joint1_position_controller/command
/dd/joint2_position_controller/command
~~~
**if it does not show the results , try this following**
~~~
$ rosservice call /dd/controller_manager/load_controller "name: 'joint1_position_controller'"
$ rosservice call /dd/controller_manager/load_controller "name: 'joint1_position_controller'"
~~~
the result should be like this
~~~
ok: True
~~~

**Step 6**,add input to control robot arm
~~~
$ rostopic pub /dd/joint1_position_controller/command std_msgs/Float64 "data: 1.57"
$ rostopic pub /dd/joint2_position_controller/command std_msgs/Float64 "data: -0.7"
~~~
if it works , the result will show
~~~
publishing and latching message. Press ctrl-C to terminate
~~~
*note*
 1. input is in radian unit
 2. each joint limit is between -3.14 to 3.14 radian
 3. input is also float

**Step 7**, open fifth terminal, to control robot movement 
~~~
$ roslaunch dd_simple_control dd_control_teleop.launch
~~~
following press the letter keys on the screen
