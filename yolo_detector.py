from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")


tracking_points = []

def draw_boxes(frame, boxes):
    """Draw detected bounding boxes on image frame"""

    # Create annotator object
    annotator = Annotator(frame)
    for box in boxes:
        class_id = box.cls
        class_name = model.names[int(class_id)]
        coordinator = box.xyxy[0]
        confidence = box.conf

        if class_name == "cat":
    # Draw bounding box
            annotator.box_label(
                box=coordinator, label=class_name, color=(255,0,0)
    )
            # อันนี้คำนวนจุดตรงกลางกล่อง
            x1, y1, x2, y2 = coordinator.cpu().numpy()
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)
            
            # ใส่จุดตรงกลางลงในlist
            tracking_points.append((center_x, center_y))
            
            # จำกัดจำนวนจุดในlist เดี๋ยวจะเยอะเกิน
            if len(tracking_points) > 50:
                tracking_points.pop(0)

            # วากเส้น
            if len(tracking_points) > 1:
                for i in range(1, len(tracking_points)):
                    cv2.line(frame, tracking_points[i-1], tracking_points[i], (0, 255, 255), 2)
            
            # วาดจุดตรงกลางกล่อง
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

    return annotator.result()


def detect_object(frame):
    """Detect object from image frame"""
    
    # Detect object from image frame
    results = model.predict(frame)

    for result in results:
        frame = draw_boxes(frame, result.boxes)

    name = "duangtawan singsa Clicknext-Internship-2024"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255) 
    thickness = 2
    position = (500, 30)  

    cv2.putText(frame, name, position, font, font_scale, color, thickness)

    return frame


if __name__ == "__main__":
    video_path = "CatZoomies.mp4"
    cap = cv2.VideoCapture(video_path)

    # Define the codec and create VideoWriter object
    # video_writer = cv2.VideoWriter(
    #     video_path + "_demo.avi", cv2.VideoWriter_fourcc(*"MJPG"), 120, (1280, 720)
    # )

    while cap.isOpened():
        # Read image frame
        ret, frame = cap.read()

        if ret:
            # Detect motorcycle from image frame
            frame_result = detect_object(frame)

            # Write result to video
            # video_writer.write(frame_result)

            # Show result
            cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
            cv2.imshow("Video", frame_result)
            cv2.waitKey(1)

        else:
            break

    # Release the VideoCapture object and close the window
    # video_writer.release()
    cap.release()
    cv2.destroyAllWindows()
    
