# **🗑️ AI-Based Waste Classification System**



### 📖 Overview
This project is an AI-powered waste classification system designed to identify and categorize waste into five different types using a machine learning model. By leveraging TensorFlow, OpenCV, and Arduino, this system can classify waste in real time and control hardware components like servo motors for automated sorting.



---



| **📅 Development Period** | **February 15, 2024 – November 18, 2024** |
|-------------------------|-------------------------------------------|



---



### 📊 Waste Categories

The system classifies waste into the following six categories:

| **Category** | **Type**        |
|--------------|-----------------|
| **0**        | Plastic         |
| **1**        | Glass Bottle    |
| **2**        | Paper           |
| **3**        | Can             |
| **4**        | Vinyl           |



---



### 💻 Technology Stack

- **Programming Languages**: Python 3.10, C++
- **Machine Learning Framework**: TensorFlow 2.16.2
- **Deep Learning Support**:
  - `keras` (2.8.0)
  - `tensorflow-macos` (2.8.0)
  - `tensorflow-io-gcs-filesystem` (0.37.1)
- **Image Processing**: OpenCV (4.5.5.64)
- **Hardware Integration**: Arduino (PlatformIO)
- **Other Tools**:
  - `numpy` (1.23.5) for numerical computations
  - `protobuf` (3.20.3) for model compatibility
  - `pyserial` (3.5) for Arduino communication

---

### 📂 Directory Structure
 
├── HPPB/
│   ├── converted_savedmodel/  # TensorFlow model in SavedModel format
│   └── resources/             # Additional assets and files
├── main.py                    # Python script for classification and image processing
├── main.cpp                   # Arduino script for servo motor control
└── README.md                  # Project documentation


---


### 🚀 How It Works

1. **Image Capture**: Real-time waste images are captured using OpenCV.
2. **Model Prediction**: A TensorFlow model processes the image and predicts the waste category.
3. **Hardware Control**: Based on the prediction, the Arduino-controlled servo motor sorts the waste.



---



### 📦 Installation

#### 1️⃣ Clone the Repository
````bash````
git clone https://github.com/your-repo-name.git
cd your-repo-name

#### 2️⃣ Create a Virtual Environment
````bash````
python3 -m venv myenv
source myenv/bin/activate


#### 3️⃣ Install Dependencies
````bash````
pip install -r requirements.txt


#### 4️⃣ Run the Python Script
````bash````
python3 main.py


#### 5️⃣ Upload the Arduino Code
	•	Open main.cpp in PlatformIO and upload it to your Arduino.



### 🤝 Contributors

We thank the following contributors for their hard work on this project:

- Pyo Jeong In
- Han Yoon Seo
- Baek Song Hee
- Park Seo Hyun


---



### 📧 Contact
	•	Email: puojeongin41@gmail.com
