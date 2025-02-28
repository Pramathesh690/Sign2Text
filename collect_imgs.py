import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

# Try different camera indices (0, 1, 2, ...) until one works
cap = None
for camera_index in range(10):  # Try up to 10 cameras
    cap = cv2.VideoCapture(camera_index)
    if cap.isOpened():
        print(f"Camera found at index: {camera_index}")
        break
    else:
        cap.release()
        cap = None

if cap is None:
    print("Error: No camera found.")
    exit()

for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        if not ret or frame is None: #check if the frame is valid
            print("Error: Could not read frame.")
            cap.release()
            cv2.destroyAllWindows()
            exit()

        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret or frame is None: #check if the frame is valid
            print("Error: Could not read frame.")
            cap.release()
            cv2.destroyAllWindows()
            exit()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()