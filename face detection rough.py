import pathlib
import cv2

cascade_Path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
print(cascade_Path)
#this is proof of cv2 provided the path

clf = cv2.CascadeClassifier(str(cascade_Path))
camera = cv2.VideoCapture(0)

while True:
    _, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,

        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30),
        flags=0
        )
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 255, 0), 2)
        cv2.imshow("faces", frame)
        if cv2.waitKey(1) == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()

