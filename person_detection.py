# import the necessary packages
import numpy as np
import cv2
from twilio.rest import Client
 
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

# open webcam video stream
cap = cv2.VideoCapture(0)

# the output will be written to output.avi
# out = cv2.VideoWriter(
#     'output.avi',
#     cv2.VideoWriter_fourcc(*'MJPG'),
#     15.,
#     (640,480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resizing for faster detection
    frame = cv2.resize(frame, (640, 480))
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    # print ("value:   ",boxes)

    if len(boxes) != 0:
        account_sid = 'ACfa44115d0ff5f4602437ca7a4130b110'
        auth_token = 'e054d9870d54ba655fa932e3ffabb83d'
        client = Client(account_sid, auth_token)
        mobile_number = {"Pratik":'+917000681073', "Nikhil":'+917415533803'}
        for name, num in mobile_number.items():
            message = client.messages \
                        .create(
                             body="Hello,\n This is Trail sms from Pratik Mahobiya\n to check the working of Alert System.\n\n Thank You",
                             from_='+19046377572',
                             to= num
                         )

            # print(message.sid)
            print("Sent to this: ",name)

    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
    
    # # Write the output video 
    # out.write(frame.astype('uint8'))
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
# and release the output
# finally, close the window
cv2.destroyAllWindows()