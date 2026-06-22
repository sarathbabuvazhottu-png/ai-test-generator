# 🤖 AI Test Case Generator

![Python](https://img.shields.io/badge/Python-3.10-blue)
![React](https://img.shields.io/badge/React-18-cyan)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Claude AI](https://img.shields.io/badge/Claude-AI-purple)
![Tests](https://img.shields.io/badge/Tests-151%20Passing-brightgreen)
![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen)

> Automatically generate Python test cases using 
> Claude AI — in seconds!

---

## 🎯 What This Project Does

This tool takes ANY Python code and automatically 
generates pytest test cases using Claude AI with 
3 different prompt strategies.

Instead of spending hours writing tests manually,
developers paste their code and get comprehensive
tests instantly!

---

## ✨ Features

- 🤖 AI-powered test generation using Claude AI
- 3 prompt styles — Basic, Detailed, Expert
- 🌐 Beautiful React web interface
- ▶️ Run tests directly from the browser
- 📊 Real-time results table
- 📋 Copy tests with one click
- ⬇️ Download tests as .py file
- 🐛 Automatically finds bugs in your code!
- 📈 Code coverage measurement

---

## 📊 Results

| Prompt Style | Tests Generated | Pass Rate | Coverage |
|-------------|----------------|-----------|----------|
| Basic       | 49             | 100%      | 100%     |
| Detailed    | 27             | 100%      | 100%     |
| Expert      | 75             | 100%      | 100%     |

**Total: 151 tests, 100% pass rate, 100% coverage!**

---

## 🏗️ Project Architecture
User pastes code in browser

↓

React Frontend (localhost:3000)

↓

Flask Backend (localhost:5000)

↓

Claude AI API

↓

Tests generated instantly!


---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python 3.10 | Backend logic |
| Claude AI API | Test generation |
| Flask | REST API backend |
| React | Web frontend |
| Pytest | Test runner |
| Pytest-cov | Code coverage |

---

## 📁 Project Structure

ai-test-generator/

│

├── src/

│   ├── functions.py

│   ├── generator.py

│   ├── evaluator.py

│   └── app.py

│

├── frontend/

│   └── src/

│       └── App.js

│

├── generated_tests/

│   ├── test_basic.py

│   ├── test_detailed.py

│   └── test_expert.py

│

├── results/

├── conftest.py

└── README.md

---

## 🚀 How To Run

**1 — Clone the repository:**
```bash
git clone https://github.com/sarathbabuvazhottu-png/ai-test-generator
cd ai-test-generator
```

**2 — Install Python libraries:**
```bash
pip install anthropic pytest pytest-cov python-dotenv flask flask-cors
```

**3 — Install React libraries:**
```bash
cd frontend
npm install
cd ..
```

**4 — Add your API key:**
**4 — Add your API key:**
```
Create .env file in main folder:
ANTHROPIC_API_KEY=your-key-here

Get your free API key at:
https://console.anthropic.com
```

**5 — Start Flask backend:**
```bash
python src/app.py
```

**6 — Start React frontend:**
```bash
cd frontend
npm start
```

**7 — Open browser:**
```
http://localhost:3000
```

---

## 💡 How To Use

```
Step 1 — Paste any Python code
Step 2 — Select prompt style
Step 3 — Click Generate Tests!
Step 4 — Click Run Tests!
Step 5 — See results instantly!
```

---

## 🐛 Bug Detection Example

The AI automatically finds bugs!

**Buggy code:**
```python
def add_numbers(a, b):
    return a - b  # Wrong operator!
```

**Claude finds it:**
```
FAILED test_add_numbers
assert add_numbers(2, 3) == 5
AssertionError: -1 != 5
```

---

## 🔮 Coming Soon

- [ ] GPT-4 comparison
- [ ] JavaScript support
- [ ] Java support
- [ ] Online hosting — anyone can use!

---

## 👨‍💻 Author

**Sarath Babu**
Masters Student | Python Developer | AI Enthusiast

GitHub: [@sarathbabuvazhottu-png](https://github.com/sarathbabuvazhottu-png)

---

## 📄 License

MIT License — feel free to use this project!