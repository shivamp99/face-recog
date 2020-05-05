import face_recognition
import os
import cv2
import time
import sys

# This is a demo of running face recognition on a video file and saving the results to a new video file.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Open the input movie file
input_movie = cv2.VideoCapture("video.mp4")
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file (make sure resolution/frame rate matches input video!)
frame_rate = input_movie.get(cv2.CAP_PROP_FPS)
width = int(input_movie.get(3))
height = int(input_movie.get(4))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter(
    'output.avi', fourcc, frame_rate, (width, height))

known_name = []
known_faces = []


known_entries = os.listdir('known')
for entry in known_entries:
    image = face_recognition.load_image_file('known/'+entry)
    try:
        known_faces.append(face_recognition.face_encodings(image)[0])
    except:
        print("No face found in this image")
    name = os.path.splitext(entry)[0]
    known_name.append(name)


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []

frame_number = 0
while True:
    # Grab a single frame of video
    input_movie.set(1, frame_number*frame_rate)
    ret, frame = input_movie.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        results = face_recognition.compare_faces(
            known_faces, face_encoding, tolerance=0.65)

        i = 0
        for name in known_name:
            if(str(results[i]) == 'True'):
                face_names.append(name)
            i+=1

    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 25),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 0.5, (255, 255, 255), 1)

    # Write the resulting image to the output video file
    i = int(100*frame_number*frame_rate/length)
    sys.stdout.write("\rProcessed\t%d%%" % i)
    sys.stdout.flush()

    output_movie.write(frame)

# All done!
print()
input_movie.release()
cv2.destroyAllWindows()