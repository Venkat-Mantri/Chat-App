# 💬 Real-Time Chat Application

A modern **real-time chat application** built using **FastAPI**, **WebSockets**, **SQLite**, and **vanilla HTML, CSS, and JavaScript**.  
The application allows multiple users to join chat rooms and exchange messages instantly with a clean, responsive, and professional user interface.

---

## 🚀 Features

- 👤 Username-based user system  
- 🏠 Multiple chat rooms support  
- ⚡ Real-time messaging using WebSockets  
- 👥 Live online users list  
- 💬 Message broadcasting to all users in a room  
- ⏱ Message timestamps  
- 🎨 Modern and responsive UI (no frontend frameworks)  
- 💾 SQLite database integration  
- 🔄 Graceful user connect and disconnect handling  

---

## 🛠 Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript (Vanilla)

**Backend**
- Python
- FastAPI
- WebSockets (`uvicorn[standard]`)

**Database**
- SQLite

---

## 📁 Project Structure

chat-app/
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── websocket_manager.py
│ └── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── .gitignore
└── README.md

yaml
Copy code

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Venkat-Mantri/Chat-App.git
cd Chat-App
2️⃣ Backend Setup
bash
Copy code
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
Backend runs at:

cpp
Copy code
http://127.0.0.1:8000
3️⃣ Frontend Setup
Open a new terminal:

bash
Copy code
cd frontend
python -m http.server 5500
Open in browser:

arduino
Copy code
http://localhost:5500
🧪 How to Use
Open the app in your browser

Enter a username and room name

Click Join Room

Open another browser or incognito window

Join the same room with a different username

Start chatting in real time 🎉

📌 Future Enhancements
Typing indicator

Message history loading

Emoji support

Private chat rooms

User authentication

🎯 Learning Outcomes
Built real-time communication using WebSockets

Learned FastAPI async architecture

Integrated SQLite with backend logic

Designed a modern UI using HTML & CSS

Understood full-stack application workflow

👨‍💻 Author
Venkat Mantri
GitHub: https://github.com/Venkat-Mantri
