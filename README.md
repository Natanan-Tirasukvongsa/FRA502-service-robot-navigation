# FRA502-service-robot : Phase III: Final presentation
This robot is moving base (by differential drive) 
Name : Natanan Tirasukvongsa
Student ID : 62340500020

**credits:**
1. https://kiranpalla.com/autonomous-navigation-ros-differential-drive-robot-simulation/describing-ros-robot-with-urdf/
2. https://github.com/devanshdhrafani/diff_drive_bot?fbclid=IwAR2t3EY3aUO5wAb3eOJGuSDGXqBoWrExbm618RtJ0-9Htg4wOJ05qkK33cg
3. https://github.com/Avi241/ancro_description

**video demonstration:** https://drive.google.com/drive/folders/1J6MmJnSN6SAPsfUbSrsweeX5UOToTUsP
*note*
1. video sound is very low  

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
1. you can use __2D Nav Goal__ to set goal

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
if it can listen clearly, output will be like this
~~~
Sphinx thinks you said living room
~~~
if it cannot listen clearly, output will be like this
~~~
speech_recognition.UnknowValueError
~~~
*note*
1. there are 4 room such as living room, kitchen, toilet and bedroom
2. you must pronouce clearly

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

### speech
1. ไม่สามารถโหลด pystudio ได้ **__(แก้ไขไม่ได้)__**
2. มีปัญหาในการออกเสียงตัวเลข เช่น input room 3 แต่ output ออกมาเป็น room three แก้ไขโดยการเปลี่ยนเป็นคำอื่นแทน **__(แก้ไขแล้ว)__**

### navigation
1. ไฟล์ global_costmap_params.yaml ในส่วนของ global_frame ไม่สามารถใช้ /map ได้ โดยแก้ปัญหาโดยการใช้ map แทน **__(แก้ไขแล้ว)__**
2. หุ่นยนต์ที่แสดงบน navigaion.rviz มีการวาปไปมา และในการทดสอบบางครั้งมีการชนกำแพงหรือสิ่งกีดขวาง (ยังแก้ปัญหานี้ไม่ได้) **__(แก้ไขไม่ได้)__**

### urdf 
1. ในช่วงแรกมีการใส่ค่า parameter ที่ไม่เหมาะสม เช่น ใส่มวลบางส่วนมากหรือน้อยเกินไป, ไม่ได้ใส่ค่าแรงเสียดทาน ดังนั้นจึงมีการเปลี่ยนแปลงค่า parameter ให้เหมาะสมมากขึ้น **__(แก้ไขแล้ว)__**
