#include <Arduino.h>
#include <Servo.h>

Servo servo1;  // 4번 핀 서보모터
Servo servo2;  // 5번 핀 서보모터
Servo servo3;  // 6번 핀 서보모터
Servo servo4;  // 7번 핀 서보모터
Servo servo5;  // 8번 핀 서보모터
Servo servo6;  // 9번 핀 서보모터

void setup() {
  Serial.begin(9600);

  servo1.attach(4);
  servo2.attach(5);
  servo3.attach(6);
  servo4.attach(7);
  servo5.attach(8);
  servo6.attach(9);

  // 모든 서보 초기화 (90도)
  servo1.write(180);
  servo2.write(180);
  servo3.write(180);
  servo4.write(180);

  // 8번과 9번 핀 초기화 (180도)
  servo5.write(180);
  servo6.write(180);
}

void rotateServosTogether(Servo &servoA, Servo &servoB, int angle, int duration) {
  servoA.write(angle);
  servoB.write(angle);
  delay(duration);
  servoA.write(90);
  servoB.write(90);
}

void rotateSingleServo(Servo &servoA, Servo &servoB, int angle, int duration) {
  // 목표 각도 설정
  int targetAngle = 180 - angle;  // 180도에서 angle만큼 감소 (반시계 방향)

  servoA.write(targetAngle);      // 목표 각도로 이동
  servoB.write(targetAngle); 
  delay(duration);               // 유지 시간
  servoA.write(180);              // 초기화 상태로 복귀
  servoB.write(180);
}


void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      rotateSingleServo(servo1, servo2, 90, 5000);  // 4번, 5번 핀: 180 → 90
    } else if (command == '2') {
      rotateSingleServo(servo3, servo4, 90, 5000);  // 6번, 7번 핀: 180 → 90
    } else if (command == '3') {
      rotateSingleServo(servo5, servo6, 90, 5000);             // 8번 핀: 180 → 90
    }
  }
}