import cv2,time

## To capture a video using inbuilt camera
video = cv2.VideoCapture(0);
face_cascade = cv2.CascadeClassifier("/home/dev/project/project/haarcascade_frontalface_default.xml")
a=1;
while True:
	a = a+1;
	check, frame = video.read();
	print(frame); 
	grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(grey,scaleFactor=1.05,minNeighbors = 5);
	for x,y,w,h in faces:
		frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),3);
	cv2.imshow('Capturing',frame);
	key = cv2.waitKey(1);
	if key == ord('q'):
		break
video.release();
cv2.destroyAllWindows()
