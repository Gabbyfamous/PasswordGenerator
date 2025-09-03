# 🔑 Python Random Password Generator

This is a simple **Python command-line tool** that generates strong, random passwords.  
It uses Python's built-in [`secrets`](https://docs.python.org/3/library/secrets.html) module to ensure **cryptographically secure randomness**, making the generated passwords safe for real-world use.


## 🚀 Featuresss
- Generate one or multiple passwords at a time.  
- Enforce **minimum length of 8 characters** (recommended security standard).  
- Option to include/exclude:
  - ✅ Uppercase letters (A–Z)  
  - ✅ Lowercase letters (a–z)  
  - ✅ Numbers (0–9)  
  - ✅ Symbols (!, @, #, $, %, etc.)  
- Handles **invalid inputs gracefully** (e.g., entering text instead of numbers).  
- Ensures user selects at least one character type.  

---

## 📦 Requirements
- Python 3.7 or higher (no external libraries needed).

---

## 🖥️ Usage

1. Clone or copy the project into your local machine.  
2. Run the script in your terminal or inside PyCharm/VS Code:  

   ```bash
   python password_generator.py
