# Safe Calc 🛡️

A safe calculator written in Python that evaluates mathematical expressions securely using [`simpleeval`](https://github.com/danthedeckie/simpleeval).  
This project provides a simple, interactive calculator that avoids unsafe `eval` usage.

---

## ✨ Features

- Safe evaluation of expressions (no arbitrary code execution).
- Interactive: type expressions and get results instantly.
- Error handling for invalid expressions, undefined functions and division by zero.
- Lightweight & pure Python — only depends on `simpleeval`.

---

## 🚀 Getting Started

### Prerequisites

```bash
# 1. (Optional) create virtual environment
python -m venv env  

# 2. Activate the virtual environment  
# On Windows (PowerShell): 
.\env\Scripts\Activate.ps1  
# On Linux / macOS:
source env/bin/activate

# 3. Install dependencies (if using external libraries)
pip install -r requirements.txt  
```

### Run the calculator

```bash
python safe_calculator.py
```

---

## 🖥️ Usage

When you run the program, you’ll see:
```
Safe Calculator — type 'exit' to quit.
Enter an expression: 2 + 3 * 4
Result: 14
Enter an expression: exit
Goodbye!
```

---

## 📂 Project Structure

```
safe-calc/
├─ README.md
├─ requirements.txt
├─ safe_calculator.py
├─ Jenkinsfile # for user to run in Jenkin
├─ tests/
│   └─ test_safe_calculator.py
└─ .github/
    └─ workflows/
        └─ run_ci.yaml
```

---

### License

MIT License © wbc1wan(WanAnis)
