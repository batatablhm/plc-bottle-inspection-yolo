from ultralytics import YOLO
import cv2
import cvzone
import math

model = YOLO('dslabel.pt')
classNames = ['label']
cap = cv2.VideoCapture(0)

while True :
    success , img =cap.read()
    results = model(img,stream=True)
    for r in results :
        #for bounding box
        boxes=r.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            x1, y1, x2, y2 =int(x1), int(y1), int(x2), int(y2)
            w,h = x2-x1,y2-y1
            cvzone.cornerRect(img,(x1,y1,w,h))
            #confidence
            conf=math.ceil((box.conf[0]*100))/100
            #classname
            cls = int(box.cls[0])

            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
    cv2.imshow("Image",img)
    cv2.waitKey(2)



