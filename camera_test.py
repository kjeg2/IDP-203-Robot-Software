import cv2

<<<<<<< HEAD
r = requests.get(url= 'http://localhost:8081/stream/video.mjpeg', stream=True)
=======
#print("Before URL")
cap = cv2.VideoCapture('rtsp://admin:123456@192.168.1.216/H264?ch=1&subtype=0')
#print("After URL")
>>>>>>> be3d6ea475683bc6bde35bb665b77148fb4a71c5

while True:

    #print('About to start the Read command')
    ret, frame = cap.read()
    #print('About to show frame of Video.')
    cv2.imshow("Capturing",frame)
    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()