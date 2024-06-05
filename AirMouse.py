import cv2
import mediapipe as mp
import pyautogui
# import time


def resize(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


def euclidian_distance(x, y):
    return (((y[0]-x[0])**2) + ((y[1]-x[1])**2))**0.5


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
sens = 1.5

smooth_factor = 0.5
prev_x, prev_y = 0, 0

trackpad_x, trackpad_y, trackpad_w, trackpad_h = 170, 140, 300, 200

cap = cv2.VideoCapture(0)
if not cap:
    print("WEBCAM NOT ACCESSIBLE!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("NO FRAMES TO OUTPUT!")
        break

    frame = resize(frame, 1)
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        landmarks = []
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks,
                                   mp_hands.HAND_CONNECTIONS)
            for lm in hand_landmarks.landmark:
                lmx = int(lm.x * frame.shape[1])
                lmy = int(lm.y * frame.shape[0])
                landmarks.append([lmx, lmy])

            fore_finger = (landmarks[8][0], landmarks[8][1])
            index = (landmarks[12][0], landmarks[12][1])

            if trackpad_x <= fore_finger[0] <= trackpad_x + trackpad_w and trackpad_y <= fore_finger[1] <= trackpad_y + trackpad_h:
                # Map trackpad coordinates to screen coordinates
                relative_x = (fore_finger[0] - trackpad_x) / trackpad_w
                relative_y = (fore_finger[1] - trackpad_y) / trackpad_h
                screen_x = int(relative_x * screen_width)
                screen_y = int(relative_y * screen_height)

                screen_x = int(prev_x * (1 - smooth_factor) +
                               screen_x * smooth_factor)
                screen_y = int(prev_y * (1 - smooth_factor) +
                               screen_y * smooth_factor)
                prev_x, prev_y = screen_x, screen_y

                pyautogui.moveTo(screen_x, screen_y)

            if euclidian_distance(index, fore_finger) < 30:
                pyautogui.click()
                # last_click_time = current_time
                cv2.circle(frame, fore_finger, 3, (0, 255, 0), -1)
                cv2.circle(frame, index, 3, (0, 255, 0), -1)

    cv2.rectangle(frame, (trackpad_x, trackpad_y), (trackpad_x +
                  trackpad_w, trackpad_y + trackpad_h), (255, 0, 0), 2)

    cv2.imshow("Output", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
