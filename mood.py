import cv2
k = 0
feliz = cv2.imread("learn.jpg")
triste = cv2.imread("sad.jpg")
face_cascade = cv2.CascadeClassifier('C:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/opencv/sources/data/haarcascades/haarcascade_smile.xml')
#video = cv2.VideoCapture(0)
video = cv2.VideoCapture('test.mp4') 
while video.isOpened():
    ret, frame = video.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 10)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray,1.18,20)
            print(eyes)
            print(faces)
            if(len(eyes) >= 1 and len(eyes) < 2):
                cv2.imshow('FELIZ',feliz)
                cv2.destroyWindow('SAD')
            else:
                cv2.imshow('SAD',triste)
                cv2.destroyWindow('FELIZ')
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
video.release()
cv2.destroyAllWindows()