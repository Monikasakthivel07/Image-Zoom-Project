import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Open video capture
cap = cv2.VideoCapture(0)

# Initialize zoom factor
zoom_factor = 1.0
prev_distance = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip image horizontally for a mirror effect
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert BGR to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Process detected hands
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get coordinates for index finger and thumb
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            x1, y1 = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            x2, y2 = int(thumb_tip.x * w), int(thumb_tip.y * h)

            # Calculate Euclidean distance between fingers
            distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # Set reference distance initially
            if prev_distance is None:
                prev_distance = distance

            # Calculate zoom factor based on distance change
            zoom_factor += (distance - prev_distance) * 0.01  # Adjust sensitivity
            zoom_factor = max(1.0, min(3.0, zoom_factor))  # Limit zoom range

            prev_distance = distance

            # Draw zoom factor text
            cv2.putText(frame, f'Zoom: {zoom_factor:.2f}x', (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Resize and display the zoomed image
    zoomed_frame = cv2.resize(frame, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Hand Zoom Control", zoomed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
