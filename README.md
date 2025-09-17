## Technical test for internship program 2024

Please follow below instruction to complete the tests
1. Correct all errors in the yolo_detector.py script and ensure its successful execution.
2. Generate a requirements.txt file that includes the necessary packages.
3. Use **CatZoomies.mp4** video as an input and detect only cat. (Ignore another class)
4. Add your **name + Clicknext-Internship-2024** the top-right corner.
5. Remove video writer function to increase fps
6. Modify the color of the bounding box for the detected cat to blue color.
7. Draw a tracking line for the detected cat.
8. Push the code to your Github account with public access and provide the link in the answer box.

<p align="left">
  <img src="demo.gif" width="640"/>
</p>


สิ่งที่แก้ไขแล้ว:
1. Fixed Code Errors
    แก้ import cv2 
    แก้ cap.read_frame() > cap.read()
    แก้ model.prediction() > model.predict()
    แก้ annotator.box_label() ให้อยู่ใน loop tab เข้าไป
    แก้ yolov8a.pt > yolov8n.pt 

2. Requirements.txt
    สร้างไฟล์แล้ว มี ultralytics และ opencv-python

3. Detect Only Cat
    เพิ่ม if class_name == "cat": filter

4. Add Name Top-Right Corner
    มี code สำหรับใส่ชื่อแล้ว 

5. Remove Video Writer
    comment video writer code ออกแล้ว

6. Blue Bounding Box
    เปลี่ยนสีเป็นสีน้ำเงิน color=(255,0,0) (BGR format)

7. Tracking Line
    เพิ่ม tracking_points list
    เพิ่ม code สำหรับวาดเส้น tracking

8. แก้ waitingKey เป็น 1 