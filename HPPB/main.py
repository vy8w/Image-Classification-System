import tensorflow as tf
import time
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import serial

# 아두이노 연결 및 대기
try:
    arduino = serial.Serial('/dev/cu.usbmodem11101', 9600, timeout=1)  # 포트 이름 확인 후 수정
    time.sleep(2)  # 아두이노 연결 안정화 대기
    print("Arduino connected.")
except serial.SerialException as e:
    print(f"Error: Could not connect to Arduino - {e}")
    exit()

# 모델 경로 및 레이블 경로 설정
saved_model_dir = '/Users/pyojeongin/Documents/HPPB/converted_savedmodel/model.savedmodel'
labels_path = '/Users/pyojeongin/Documents/HPPB/converted_savedmodel/labels.txt'

# 모델 로드
model = tf.saved_model.load(saved_model_dir)

# 레이블 불러오기
with open(labels_path, 'r', encoding='utf-8') as f:
    labels = [line.strip().split()[1] for line in f.readlines()]

# 웹캠 초기화
cap = cv2.VideoCapture(0)
time.sleep(2)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

threshold = 0.80  # 임계값 설정
hold_time = 2  # 2초 동안 유지

start_detection_time = None
last_label = None

font_path = "/Library/Fonts/AppleGothic.ttf"  # Mac에서 사용할 수 있는 기본 한글 폰트
font = ImageFont.truetype(font_path, 20)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    img = cv2.resize(frame, (224, 224))
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)

    predictions = model(img, training=False).numpy()[0]

    frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(frame_pil)

    y_offset = 30
    for i, (label, confidence) in enumerate(zip(labels, predictions)):
        text = f"{label}: {confidence:.2f}"
        draw.text((10, y_offset + i * 30), text, font=font, fill=(255, 255, 255))

    frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

    max_index = np.argmax(predictions)
    max_label = labels[max_index]
    max_confidence = predictions[max_index]

    current_time = time.time()

    if max_confidence >= threshold:
        if max_label == last_label:
            if start_detection_time is None:
                start_detection_time = current_time

            elif current_time - start_detection_time >= hold_time:
                print(f"{max_label} 감지: 아두이노로 신호 전송")

                try:
                    if max_label == '유리병':
                        arduino.write(b'1')  # 4, 5번 핀 제어
                    elif max_label == '비닐':
                        arduino.write(b'2')  # 6, 7번 핀 제어
                    elif max_label == '종이':
                        arduino.write(b'3')  # 8, 9번 핀 제어

                    arduino.flush()
                    time.sleep(0.5)  # 전송 후 짧은 대기 시간 추가
                except serial.SerialException as e:
                    print(f"Error: {e}")

                time.sleep(5)  # 서보모터 동작 대기
                start_detection_time = None
        else:
            last_label = max_label
            start_detection_time = None
    else:
        start_detection_time = None

    cv2.imshow('Material Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()