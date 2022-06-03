import cv2
import numpy as np
import dlib
from math import hypot
#import winsound
import datetime, time
import threading
cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")   #cascade yukledim
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
sayac=0
count = 0
count2 = 0
sayac2=0
sayac3=0
sayac4=0
sayac5=0

def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)
FONT_HERSHEY_PLAIN = 1
font = FONT_HERSHEY_PLAIN

def get_blinking_ratio(eye_points, facial_landmarks): 
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_lenght / ver_line_lenght
    return ratio

def f(mythread):
    #winsound.PlaySound("danger_01", winsound.SND_FILENAME)
    k=k+1

def yola(mythread1):
    #winsound.PlaySound("yolaodaklan", winsound.SND_FILENAME)
    l=l+1
    

while True:
    
    
    
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    sayac3=sayac
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
            
            
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]     
            
            eyes = eye_cascade.detectMultiScale(roi_gray)
            
            for (ex,ey,ew,eh) in eyes:
                        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
                          
                        if ex+ey<=0:
                         
                            t2 = threading.Thread(target=yola,args = ("thread-1", ))  #threadi tanımladık ve f fonksiyonunu hedef gösterdik#uyuma  
                            t2.start()
  
    cv2.putText(frame, "kirpma sayisi: ", (450, 35), font, 1, (0, 0, 0))
    cv2.putText(frame, str(sayac5), (570, 35), font, 1, (255, 255, 255))
    faces = detector(gray)
    for face in faces:
        now = time.time()
        future=now+6
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2) #yuzu dikdiortgen icine aldim.
        

        landmarks = predictor(gray, face)

        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
         

      
    
          
        if blinking_ratio > 5.4:
            
            
            #cv2.rectangle(frame, (x, y+145), (x1, y1), (255, 0, 0), cv2.FILLED)
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 0, 225), 2)
            cv2.putText(frame, "KAPANDI", (x, y-10), font, 2, (0, 0, 255), 3)
            
            
                
            if sayac4>0:
                sayac5=sayac5+1
            cv2.putText(frame, str(sayac5), (570, 35), font, 1, (255, 255, 255))
            sayac4=0
            count2=count2+1
        
            print(count2)
        
            if count2==27:  #uyuklama
                sayac2=sayac2+1
            if sayac2==5:
                t2 = threading.Thread(target=yola,args = ("thread-1", ))  #threadi tanımladık ve f fonksiyonunu hedef gösterdik#uyuma  
                t2.start()
                sayac2=0
                
            if count2==26:
                cv2.putText(frame, "UYARI", (470, 60), font, 1.5, (0, 0, 255), 3)
                t2 = threading.Thread(target=yola,args = ("thread-1", ))  #threadi tanımladım ve yola fonksiyonunu hedef gösterdik#uyuma  
                t2.start()
            if count2==62:
                cv2.putText(frame, "UYARI", (470, 60), font, 1.5, (0, 0, 255), 3)
                t2 = threading.Thread(target=yola,args = ("thread-1", ))  #threadi tanımladım ve yola fonksiyonunu hedef gösterdik#uyuma  
                t2.start()
                
            if count2==100:
                t1 = threading.Thread(target=f,args = ("thread-1", ))  #threadi tanımladık ve f fonksiyonunu hedef gösterdik#uyuma  
                t1.start()
                #winsound.PlaySound("2", winsound.SND_FILENAME)
                count2=0
                sayac2=0
             
                break
            else:
               
                break
        
       
       
        elif blinking_ratio <5.7:
            count2=0
            sayac=sayac+1
            sayac4=sayac-sayac3
      
 
  
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

cap.release()
cv2.destroyAllWindows()








