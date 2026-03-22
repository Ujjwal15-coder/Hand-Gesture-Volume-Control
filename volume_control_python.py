import cv2
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# 🔊 Volume setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

vol_min, vol_max = volume.GetVolumeRange()[:2]

# ✋ Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# 🎥 Webcam
webcam = cv2.VideoCapture(0)

# 🎯 Calibration values (IMPORTANT → adjust if needed)
min_length = 30
max_length = 180

while True:
    success, image = webcam.read()
    if not success:
        break

    h, w, _ = image.shape
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            drawing_utils.draw_landmarks(image, hand)

            landmarks = hand.landmark

            # 👍 Thumb tip (4) & Index tip (8)
            x1 = int(landmarks[4].x * w)
            y1 = int(landmarks[4].y * h)

            x2 = int(landmarks[8].x * w)
            y2 = int(landmarks[8].y * h)

            # Draw points
            cv2.circle(image, (x1, y1), 10, (255, 0, 0), -1)
            cv2.circle(image, (x2, y2), 10, (255, 0, 0), -1)

            # Line between fingers
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # 📏 Distance
            length = math.hypot(x2 - x1, y2 - y1)

            # Clamp length
            length = max(min_length, min(max_length, length))

            # 🎯 Map to volume
            vol = vol_min + (length - min_length) / (max_length - min_length) * (vol_max - vol_min)

            # 🔥 Force FULL volume for L gesture
            if length > 160:
                volume.SetMasterVolumeLevel(vol_max, None)
                vol_percent = 100
                status = "HIGH 🔊"

            elif length < 40:
                volume.SetMasterVolumeLevel(vol_min, None)
                vol_percent = 0
                status = "LOW 🔉"

            else:
                volume.SetMasterVolumeLevel(vol, None)
                vol_percent = int((length - min_length) / (max_length - min_length) * 100)
                status = "Adjusting..."

            # 🟩 Volume Bar
            bar_height = int((length - min_length) / (max_length - min_length) * 300)
            cv2.rectangle(image, (50, 150), (85, 450), (0, 0, 255), 3)
            cv2.rectangle(image, (50, 450 - bar_height), (85, 450), (0, 255, 0), -1)

            # 🔢 Text
            cv2.putText(image, f'{vol_percent} %', (40, 500),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

            cv2.putText(image, status, (200, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)

            # Debug length
            cv2.putText(image, f'Len: {int(length)}', (200, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    cv2.imshow("🔥 Hand Volume Control (Pro)", image)

    if cv2.waitKey(10) == 27:
        break

webcam.release()
cv2.destroyAllWindows()