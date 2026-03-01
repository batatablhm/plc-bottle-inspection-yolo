from ultralytics import YOLO
import cv2
import cvzone
import math
import snap7

# PLC connection settings
plc_ip = '192.168.0.1'
plc_rack = 0
plc_slot = 1

# Connect to the PLC
plc = snap7.client.Client()
plc.connect(plc_ip, plc_rack, plc_slot)
state = plc.get_cpu_state()
print(f'CPU State: {state}')

# Function to write a boolean to the PLC
def WriteBooltoDB(db_number, byte, size, bit, value):
    reading = plc.read_area(snap7.types.Areas.DB, db_number, byte, size)
    snap7.util.set_bool(reading, 0, bit, value)
    plc.write_area(snap7.types.Areas.DB, db_number, byte, reading)

def WriteBooltoMemory( byte, size, bit,value):
    reading = plc.read_area(snap7.types.Areas.MK, 0, byte, size)
    snap7.util.set_bool(reading, 0, bit,value)
    plc.write_area(snap7.types.Areas.MK,0,byte,reading)

# Open the default camera
cap = cv2.VideoCapture(1)

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

# Load the YOLO models
model = YOLO('best (1).pt')
model2 = YOLO('dslabel.pt')

# Class names for detection
classNames = ["cap", "nocap"]
classNames1 = ["label"]
myColor = (0, 0, 255)

# Main loop
while True:
    # Read a frame from the camera
    success, img = cap.read()

    # Check if the frame was read successfully
    if not success:
        print("Error: Could not read frame")
        break

    # Perform object detection on the frame using YOLO
    results = model(img, stream=True)
    cap_detected = False

    # Process detection results
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h), colorR=myColor)
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (x1, y1 - 10), scale=1, thickness=1)
            if cls == 0:  # Cap detected
                cap_detected = True

    # Check for cap detection before proceeding
    if cap_detected:
        print("Good cap")
        results1 = model2(img, stream=True)
        label_detected = False

        # Process label detection results
        for r in results1:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                w, h = x2 - x1, y2 - y1
                cvzone.cornerRect(img, (x1, y1, w, h), colorR=myColor)
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                cvzone.putTextRect(img, f'{classNames1[cls]} {conf}', (x1, y1 - 10), scale=1, thickness=1)
                label_detected = True

        # Output results
        if label_detected:
            print("Good label")
            WriteBooltoMemory(0, 1, 0, False)
            print("Good bottle")
        else:
            print("No label was detected, activate ejection")
            WriteBooltoMemory(0, 1, 0, True)
            print("Bad bottle, activate ejection")
    else:
        print("No cap was detected, activate ejection")
        WriteBooltoMemory(0, 1, 0, True)
        print("Bad bottle, activate ejection")

    # Display the image
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()