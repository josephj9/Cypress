# Cypress

A web application built with Python, Flask, and JavaScript for user registration, login, and emergency report submissions with map integration.

---

## Features

- User registration, login, and password reset functionality.
<img width="959" alt="image" src="https://github.com/user-attachments/assets/a6fd50a6-fcd3-478b-bf52-b34377a75f06" />

- Admin login with dedicated admin dashboard.
<img width="957" alt="image" src="https://github.com/user-attachments/assets/6f85a8cf-3c56-4f08-91d5-952b646fb31d" />

- Emergency report submission with geolocation support.
<img width="959" alt="image" src="https://github.com/user-attachments/assets/9be1aa7b-6bed-43e9-a959-508b825f1f32" />

- Stores reports in a text file (`reports.txt`) as JSON lines.
<img width="959" alt="image" src="https://github.com/user-attachments/assets/e5c3c3c7-f826-4a8b-8167-f37b105731e1" />

- User-friendly interface styled with custom CSS and background images.
- Built with Flask backend and HTML templates.

---

## Project Structure

```
Cypress/
├── app.py                   # Main Flask application
├── reports.txt              # Stores submitted incident reports (JSON lines)
├── static/
│   ├── css/
│   │   ├── forgotPassword.css
│   │   ├── login.css
│   │   └── register.css
│   └── images/              # UI images (e.g., LoginBackground.jpg)
├── templates/               # HTML templates (register, login, userMap, admin, etc.)
├── .gitignore               # Git ignore file for Python virtual environments
└── README.md
```

---

## Installation

This project requires Python 3 and the Flask framework.

1. **Clone the repository:**
    ```bash
    git clone https://github.com/josephj9/Cypress
    cd Cypress
    ```

2. **Set up a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install flask
    # (Add any other dependencies here if used)
    ```

---

## Usage

1. **Run the Flask app:**
    ```bash
    python app.py
    ```

2. **Open your browser and go to:**
    ```
    http://127.0.0.1:5000/
    ```

3. **Use the web interface to:**
    - Register a new user
    - Log in as a user or as admin (`admin123`/`admin123`)
    - Submit incident reports via the map interface

---

## Notes

- Reports are appended to `reports.txt` in JSON format.
- CSS and images are located in the `static` folder.
- HTML templates are located in the `templates` folder.

---

## File Descriptions

- **app.py**: Main Flask application with routes for registration, login, password reset, admin, map, and report submission.
- **static/css/**: Custom CSS for UI styling.
- **static/images/**: Background and UI images.
- **templates/**: HTML templates for rendering pages.
- **reports.txt**: Stores incident reports as JSON lines.
- **.gitignore**: Ignores virtual environment directories.


