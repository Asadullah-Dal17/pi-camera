from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
width, Height = 640, 480


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (width, Height)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(width, Height))
# allow the camera to warmup

time.sleep(0.1)
frame_counter =0
start_time = time.time()
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    frame_counter +=1
    image = frame.array
    # calculating the fps 
    fps = frame_counter/(time.time() - start_time)
    cv2.putText(image, f'FPS: {round(fps,2)}', (30,40), cv2.FONT_HERSHEY_PLAIN, 1.3, (0,255,0),2)
    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break