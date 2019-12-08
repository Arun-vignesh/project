##importing an image
import cv2

## Laoding the image
## 0 at indicates that the image is in a grey scale format
## For grey scale format It should contains a single channel
## 1 at indicates that the image is in a rgb format
## For rgb image it indicates that the image contains three channels
# img1 = cv2.imread("Image Location",0);
# img = cv2.imread("/home/dev/Downloads/bright-spring-view-cameo-island-260nw-1048185397.jpg",1);

## Printed the matrix of image
# print(img)

## To get the two dimensional arry of the image 
# print(img.shape)


## displaying the image And let the wait until the user pressed something
# cv2.imshow("Test image",img);
# cv2.waitKey(0);
## cv2.waitKey(3000)  Window wait for three seconds in other words three thousand milli seconds
# cv2.destroyAllWindows();


## resizing the image
# resized_image=cv2.resize(img,(650,500));
# cv2.imshow("Test image",resized_image);
# cv2.waitKey(0);
## cv2.waitKey(3000)  Window wait for three seconds in other words three thousand milli seconds
# cv2.destroyAllWindows();

## Getting the xml file to apply for the harcascade algorithm
face_cascade = cv2.CascadeClassifier("/home/dev/project/project/haarcascade_frontalface_default.xml")

## Face image so that we can get that detect it as a face
img = cv2.imread("/home/dev/project/project/images4.jpg",1) 

## Conversion of rgb image into greyscale image
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);


faces = face_cascade.detectMultiScale(grey_img,scaleFactor=1.05,minNeighbors = 5);

for x,y,w,h in faces:
	img = cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),3);

resized = cv2.resize(img , (int(img.shape[1]/7),int(img.shape[0]/7)));
cv2.imshow("gray",resized);
cv2.waitKey(0);
cv2.destroyAllWindows();
