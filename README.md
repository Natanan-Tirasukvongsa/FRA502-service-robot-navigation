# FRA502-service-robot : Phase III: Final presentation

## Info:

Name : Natanan Tirasukvongsa

Student ID : 62340500020

## Dear professor
Dear Professor Thavida Maneewarn, Thank you so much for helping me and teaching me.
I will apply your lessons in the future and develop myself to be better all the time.

## credits:
1. urdf,rviz,gazebo and teleop_twist_key : [links](https://kiranpalla.com/autonomous-navigation-ros-differential-drive-robot-simulation/describing-ros-robot-with-urdf/)
2. gmapping and navigation : [links](https://github.com/devanshdhrafani/diff_drive_bot?fbclid=IwAR2t3EY3aUO5wAb3eOJGuSDGXqBoWrExbm618RtJ0-9Htg4wOJ05qkK33cg)
3. speech navigation : [links](https://github.com/Avi241/ancro_description)
4. robot manipulator : [links](https://www.youtube.com/watch?v=Ale55LcdZeE&list=PLK0b4e05LnzYpDnNeWJcQLju7JfJFX-lk&index=1)

## video demonstration: 
1. final video : [links](https://drive.google.com/drive/folders/1J6MmJnSN6SAPsfUbSrsweeX5UOToTUsP)
2. previous video : [links](https://drive.google.com/drive/folders/1LmPplB1sx3LDUO-EncINvqemZJnvC7kX)

*note*
1. video sound is very low , so I add voice record in side google drive
2. final video is speech navigation
3. previous video is pick and place (before edit proposal)
4. this is github of previous video :[links]( https://github.com/Natanan-Tirasukvongsa/FRA502-Service-Robot)

## What did I use
1. ubuntu 20.04 lts (noetic)
2. virtual box
3. visual studio
4. differential drive (2 back wheels)
5. ball wheel (support wheel)
6. hokuyo lidar (laserscan)
7. camera

## All files used in this project

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
voice command program | dd_sim | script | dd_voice.py

## run robot 
### launch rviz ,gazebo and open camera
**Step 1**, open first terminal and launch RVIZ by following this 
~~~~~~
$ roslaunch dd_sim dd_rviz.launch
~~~~~~
launch Gazebo 
~~~
$ roslaunch dd_sim dd_gazebo.launch
~~~

**Step 2**, open second terminal to show rostopic list
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
 3. on the other hand you can open camera in rviz, no need to open in terminal 

### create map
**Step 1**, open first terminal to launch gazebo
~~~
$ roslaunch dd_sim dd_gazebo.launch
~~~

**Step 2**, open second terminal to launch gmapping 
~~~
$ roslaunch dd_sim gmapping.launch
~~~

**Step 3**, open third terminal to control robot movement 
~~~
$ roslaunch dd_simple_control dd_control_teleop.launch
~~~
you will see the map on rviz, move the robot by following press the letter keys on the screen
move your robot until you are satisfied (created map is complete)

**Step 4**, open fourth terminal to save your map 
~~~
$ rosrun map_server map_saver -f ~/test2_map
~~~
*note*
1. test2_map is file name
2. copy the map file to dd_sim/map/
3. change directory in test2_map.yaml to  /home/(your ubuntu)/catkin_ws/src/dd_sim/map/test2_map.pgm

### autonomous navigation
**Step 1**, open first terminal to launch gazebo
~~~
$ roslaunch dd_sim dd_gazebo.launch
~~~

**Step 2**, open second terminal to launch amcl, movebase and rviz
~~~
$ roslaunch dd_sim amcl_move_base.launch
~~~
*note*
1. you can use __2D Pose Estimate__ to set initial
2. you can use __2D Nav Goal__ to set goal

**Step 3**, open third terminal to see position and orientation (x, y, z, w)
~~~
$ rostopic echo /move_base_simple/goal
~~~
*note*
1. you can note robot pose for using in voice command 

### voice command
**Step 1**, open first terminal to launch gazebo
~~~
$ roslaunch dd_sim dd_gazebo.launch
~~~

**Step 2**, open second terminal to launch amcl, movebase and rviz
~~~
$ roslaunch dd_sim amcl_move_base.launch
~~~

**Step 3**, open third terminal to launch program 
~~~
$ rosrun dd_sim dd_voice.py
~~~
if it works, output will be like this
~~~
Where Should I go ?
~~~
after that say the room name (living room, kitchen, toilet or bedroom)
if it can listen clearly, output will be like this
~~~
Sphinx thinks you said living room
~~~
if it cannot listen clearly, output will be like this
~~~
speech_recognition.UnknowValueError
~~~
*note*
1. there are 4 rooms such as living room, kitchen, toilet and bedroom
2. you must pronouce clearly
3. if cannot run this file, you can run thisfile in visual studio (or other IDE). another way in third terminal, try : 
~~~
$ roscd dd_sim/script/
$ chmod +x dd_voice.py
$ rosrun dd_sim dd_voice.py
~~~

## problems
### virtual box
1. gazebo และ camera ในช่วงแรก ๆ มีการแสดงหน้าจอเป็นสีดำ ไม่แน่ใจว่าการเพิ่ม virtualbox system base memory สามารถช่วยได้หรือไม่ แต่ว่าหลังจากเพิ่ม ปัญหานี้ก็หาย **__(แก้ไขแล้ว)__**
2. ถ้า virtual box ไม่มีการเปิดใช้ตัวเร่งความเร็ว 3D ที่หน้าจอแสดงผล ตอนที่ใช้ gazebo เช่นเวลาใส่สีจะไม่ขึ้น option window มาให้ หรือตอนที่ save งานก็จะไม่ขึ้นหน้าต่าง save มาให้ **__(แก้ไขแล้ว)__**
3. ถ้ามีการเปิดใช้ตัวเร่งความเร็ว 3D จะไม่สามารถประมวลผลหนักๆ ได้ เช่นเปิด gazebo พร้อมกับ navigation ถ้าเปิดพร้อมกัน virtual box จะปิดการทำงานเอง **__(แก้ไขแล้ว)__**
4. virual box มีการใช้งานไม่ได้ในช่วงหนึ่ง (เหมือนลบตัวเองต้องโหลดใหม่) **__(แก้ไขแล้ว)__**
5. การตั้งค่าเริ่มต้นไม่ได้เปิด enable audio input ที่ audio ทำให้ไม่มีเสียงเข้าไปสั่งงานหุ่นยนต์ได้ ดังนั้นจึงเปิดการใช้งาน  enable audio input ที่ setting ของ virtual box  **__(แก้ไขแล้ว)__**

### gazebo
1. ตอนสร้าง บ้านใน gazebo ไม่สามารถลาก หน้าต่างหรือประตู ข้ามกำแพงที่ซ้อนกันได้ ต้องสร้างกำแพงเสร็จแล้วใส่ หน้าต่างหรือประตูเข้าไปทันที ไม่งั้น โปรแกรม gazebo จะปิดตัวเอง **__(แก้ไขแล้ว)__**
2. ในบางครั้ง gazebo ปิดตัวมันเองโดยไม่ทราบสาเหตุ **__(ไม่ทราบแนวทางแก้ไข)__**
3. เมื่อ launch gazebo ในส่วนของ node robot_state_publisher ไม่สามารถใช้ type = state_publisher แต่แก้ไขเป็น type = robot_state_publisher **__(แก้ไขแล้ว)__**
~~~
<node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" output="screen"/>
~~~

### speech
1. ไม่สามารถโหลด pystudio และ pip3 install SpeechRecognition ได้ **__(แก้ไขไม่ได้)__**
2. มีปัญหาในการออกเสียงตัวเลข เช่น input room 3 แต่ output ออกมาเป็น room three แก้ไขโดยการเปลี่ยนเป็นคำอื่นแทน **__(แก้ไขแล้ว)__**
3. ถ้าหาก run ไฟล์ dd_voice.py ใน terminal จะติดปัญหาไม่สามารถรันได้ แต่แก้ไขโดยการทำเหมือนขั้นตอนของ note ในหัวข้อ command หรือ run ใน visualstudio โดยตรง **__(แก้ไขแล้ว)__**
4. ไม่สามารถตั้งชื่อห้องเป็น room1 ได้ แต่สามารถแก้ไขเป็น room 1ได้ **__(แก้ไขแล้ว)__**

### navigation
1. ไฟล์ global_costmap_params.yaml ในส่วนของ global_frame ไม่สามารถใช้ /map ได้ โดยแก้ปัญหาโดยการใช้ map แทน **__(แก้ไขแล้ว)__**
2. หุ่นยนต์ที่แสดงบน navigaion.rviz มีการวาปไปมา และในการทดสอบบางครั้งมีการชนกำแพงหรือสิ่งกีดขวาง **__(แก้ไขไม่ได้)__**
3. ในส่วนการทำ navigation ช่วงแรกมีการติดตั้ง laser scan ที่ต่ำไปและสามารถตรวจจับได้เพียง 180 องศา ทำให้เมื่อหุ่นยนต์ถอยหลังมีการชนสิ่งกีดขวาง จึงแก้ไขปรับให้ตำแหน่งสูงขึ้นและเปลี่ยนมุมองศาเป็น 360 องศา **__(แก้ไขแล้ว)__**

### urdf 
1. ในช่วงแรกมีการใส่ค่า parameter ที่ไม่เหมาะสม เช่น ใส่มวลบางส่วนมากหรือน้อยเกินไป, ไม่ได้ใส่ค่าแรงเสียดทาน ดังนั้นจึงมีการเปลี่ยนแปลงค่า parameter ให้เหมาะสมมากขึ้น **__(แก้ไขแล้ว)__**

### package
1. ถ้าหากสร้าง package ขึ้นมาแล้วไม่มี package นั้นแต่แรก สามารถใส่ package นั้นเข้าไปยัง package.xml และ CMackList.txt **__(แก้ไขแล้ว)__**

### arm control
1. ถ้าหากใส่ค่า pid ของแต่ละข้อต่อหุ่นยนต์มากเกินไปจะทำให้หุ่นยนต์ทั้งหมดสั่น ดังนั้นจึงเริ่มต้นจากการใส่ค่าน้อย ๆ ก่อน **__(แก้ไขแล้ว)__**
2. ในการบังคับแขนหุ่นยนต์ไปในองศาต่าง ๆ ในบางครั้งไม่ขึ้น topic ดังนั้นจึงแก้ไขตามลิงก์นี้ [links](http://wiki.ros.org/ros_control/Tutorials/Loading%20and%20starting%20controllers%20through%20service%20calls) **__(แก้ไขแล้ว)__**
~~~
$ rosservice call /dd/controller_manager/load_controller "name: 'joint1_position_controller'"
$ rosservice call /dd/controller_manager/load_controller "name: 'joint1_position_controller'"
~~~
4. ตอนที่เพิ่ม package ของ controller_manager, joint_state_controller, robot_state_publisher ไม่สามารถใช้ <build_depend/> และ <run_depend/> แต่ใช้ลักษณะแบบนี้แทน **__(แก้ไขแล้ว)__**
~~~
<build_export_depend>controller_manager</build_export_depend>
<build_export_depend>joint_state_controller</build_export_depend>
<build_export_depend>robot_state_publisher</build_export_depend>

<exec_depend>controller_manager</exec_depend>
<exec_depend>joint_state_controller</exec_depend>
<exec_depend>robot_state_publisher</exec_depend>
~~~
