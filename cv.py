import cv2
import random
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(r"sample/haarcascade_eye.xml")

frame_widht=int(cap.get(3))
frame_height=int(cap.get(4))
kod =cv2.VideoWriter_fourcc(*"XVID")
cixdi = cv2.VideoWriter("records/videom.avi",kod,30,
(frame_widht,frame_height))
while True :
    ret,frame =cap.read() 
    sekil = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    if ret:
        uz = cascade.detectMultiScale(sekil,1.1,4)
        cixdi.write(frame)
        for (x,y,w,h) in uz :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        cv2.imshow("kamera",frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else :
        break
cap.release()
cixdi.release()
cv2.destroyAllWindows()