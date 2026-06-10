import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

person_detected_frames = 0
person_missing_frames = 0
MIN_PERSON_FRAMES = 5  
eye_open_frames = 0
eye_closed_frames = 0
EYE_FRAME_THRESHOLD = 5  

person_confirmed = False
eyes_open = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) > 0:
        person_detected_frames += 1
        person_missing_frames = 0
    else:
        person_missing_frames += 1
        if person_missing_frames > 5:
            person_detected_frames = 0

    person_confirmed = person_detected_frames >= MIN_PERSON_FRAMES

    if person_confirmed:
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            if len(eyes) > 0:
                eye_open_frames += 1
                eye_closed_frames = 0
            else:
                eye_closed_frames += 1
                eye_open_frames = 0

            if eye_open_frames >= EYE_FRAME_THRESHOLD:
                eyes_open = True
            elif eye_closed_frames >= EYE_FRAME_THRESHOLD:
                eyes_open = False

    if not person_confirmed:
        status = "No Person Detected"
        color = (0, 255, 255)  
    else:
        if eyes_open:
            status = "Person Present - Eyes Open"
            color = (0, 255, 0)  
        else:
            status = "Person Present - Eyes Closed"
            color = (0, 0, 255) 

    text_size, _ = cv2.getTextSize(status, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    text_w, text_h = text_size
    cv2.rectangle(frame, (20, 10), (30 + text_w, 70), color, -1) 
    cv2.putText(frame, status, (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    if person_confirmed:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    cv2.imshow("Person & Eyes Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()