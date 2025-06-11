# 🚀 PHP, MySQL & Webmin Auto Installer Script

This Python script automates the installation and setup of **PHP**, **MySQL**, and **Webmin** on Ubuntu systems. It provides an interactive interface to choose which components to install, making it ideal for quick server setup.

---

## ✅ Features

- 📦 Updates your system (`apt update && upgrade`)
- ⚙️ Installs a user-specified version of PHP (e.g., 8.1, 8.2, etc.)
- 🛠 Installs MySQL Server
- 🔁 Starts and enables MySQL to run on boot
- 🌐 Optionally installs **Webmin**, a web-based system administration tool
- 🔐 Automatically opens port `10000` for Webmin access
- 📋 Displays installed PHP and MySQL versions at the end

---

## 📦 Requirements

- Ubuntu 20.04 or 22.04
- Python 3.6 or higher
- Root or `sudo` access

---

## 💻 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Echopxtechnologies/PHP_MySQL.git

```
```
python3 PHP_MySQL/install.py

```
