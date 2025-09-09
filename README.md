
# Mini Password Manager

A lightweight, beginner-friendly password manager built with **Python**.  
It uses a **master password** to derive an encryption key and securely stores your website credentials in an **encrypted local file**.  

Includes a simple **Tkinter GUI** to:  
- Unlock with master password  
- Add new credentials  
- View stored credentials  

---

## 📂 Project Structure

```
MiniPasswordManager/
│── .venv/                 # Virtual environment (not in repo)
│── requirement.txt        # Project dependencies
│── main.py                 # Entry point
│
├── manager/                # Core password manager logic
│   ├── __init__.py
│   ├── crypto_utils.py     # Hashing + encryption helpers
│   ├── storage.py          # File I/O (encrypted JSON store)
│   └── manager.py          # PasswordManager class
│
└── gui/                    # Tkinter GUI
    ├── __init__.py
    └── app.py              # PasswordManagerGUI class

```
---

## ⚙️ Features
- 🔐 **Master password** → generates AES key with SHA-256  
- 📂 **Encrypted storage** → credentials saved securely in local file  
- ➕ **Add credentials** (website, username, password)  
- 📜 **List / view credentials** in the GUI  
- 🖥️ **Cross-platform** (macOS, Linux, Windows with Python 3.8+)  

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/J-Phoenix/MiniPasswordManager.git
cd MiniPasswordManager
```
### 2. Create virtual environment
```bash
python -m venv .venv
```
### 3. Activate virtual environment
```bash
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```
### 4.Install dependencies
```bash
pip install -r requirement.txt
```
### 5. Run the app
```bash
python main.py
```

## My Project Showcase






[![My Project Showcase](https://img.youtube.com/vi/vkaUAswhLpI/0.jpg)](https://www.youtube.com/watch?v=vkaUAswhLpI)
