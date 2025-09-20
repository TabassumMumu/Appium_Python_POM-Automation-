# Appium Android Test Automation (POM)

This repository contains **Appium automation tests** written in Python using the **Page Object Model (POM)** design pattern.  
The project demonstrates complete end-to-end flows for multiple Android app features such as **Clipboard Demo**, **List Demo**, and **Picker Demo**.

---

## 🚀 Features
- **Page Object Model (POM)** for clean and maintainable test code  
- Automated flows for:
  - Clipboard Demo
  - List Demo (with alert handling)
  - Picker Demo (date selection)  
- **Pytest integration** for structured test execution  
- Reusable driver setup for Android UI testing  

---

## 🛠️ Tech Stack
- **Language:** Python 3.x  
- **Framework:** Pytest  
- **Automation:** Appium (UIAutomator2)  
- **Design Pattern:** Page Object Model (POM)  

---

## 📂 Project Structure
Appium-POM-Tests/
│── pages/ # Page classes for each screen
│ ├── base_page.py
│ ├── clipboard_page.py
│ ├── list_page.py
│ ├── picker_page.py
│
│── test_app_flow.py
│ 
│
│── conftest.py # Driver setup for pytest
│── requirements.txt # Project dependencies
│── README.md # Project documentation
│── .gitignore

---

## ⚙️ Setup Instructions

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/YourUsername/Appium-POM-Tests.git
cd Appium-POM-Tests

2️⃣ Create Virtual Environment 
python -m venv venv
venv\Scripts\activate       # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Start Appium Server
appium --allow-cors
