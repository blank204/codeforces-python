import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1)
cap = cv2.VideoCapture(0)

gesture_to_emoji = {
    "thumbs_up": "👍",
    "fist": "👊",
    "open_palm": "🖐️"
}


def detect_gesture(landmarks):
    # Simple rule-based example:
    thumb_tip = landmarks[4].y
    index_tip = landmarks[8].y
    middle_tip = landmarks[12].y

    if thumb_tip < landmarks[3].y and index_tip > landmarks[6].y:
        return "thumbs_up"
    elif all(lm.y > landmarks[0].y for lm in landmarks[5:]):
        return "fist"
    else:
        return "open_palm"


while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(handLms.landmark)
            emoji = gesture_to_emoji.get(gesture, "")
            cv2.putText(img, emoji, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5)

    cv2.imshow("Hand Gesture to Emoji", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()