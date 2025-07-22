# 🎮 Fortnite Stats Viewer - Flask App

This is a web application built using **Python (Flask)** that allows users to retrieve and view real-time statistics of Fortnite players by consuming the public **[Fortnite API](https://fortnite-api.com/)**. Users can search by Epic username and receive key stats like Battle Pass progress, level, total kills, win rate, time played, and wins across different game modes (Solo, Duo, Squad).

## 📸 Screenshots

### 🏠 Home page
![Home Screenshot](https://i.imgur.com/pVN8T8C.png)

### 📊 Player statistics
![Stats Screenshot](https://i.imgur.com/yupPkMj.png)

---

## ⚙️ Technologies Used

- 🔹 Python 3
- 🔹 Flask (micro web framework)
- 🔹 HTML5
- 🔹 CSS3
- 🔹 Jinja2 templating
- 🔹 REST API (Fortnite API)

---

## 🚀 How It Works

1. The user enters an Epic Games username in the search form.
2. The backend sends a GET request to the Fortnite API:  
   `https://fortnite-api.com/v2/stats/br/v2`
3. The request includes an API key in the headers.
4. The response is received as JSON and parsed.
5. Time played is converted from minutes to hours or days.
6. A response template is rendered showing detailed stats.

---

## 📁 Project Structure

```
fortnite-stats-flask/
├── main.py
├── requirements.txt
├── README.md
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── home.html
    └── response.html
```

---

## 🔐 How to Get an API Key

1. Go to: [https://dash.fortnite-api.com/](https://dash.fortnite-api.com/)
2. Log in with your Discord account
3. Create a developer account and copy your API key
4. Replace `"YOUR_API_KEY"` in `main.py` with your personal key

---

## 🧪 Example of a Valid Player Name

```
Tfue
Ninja
Bugha
```

> If the username does not exist or has private stats, the API may return an error or empty response.

---

## 📦 Installation and Running Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/fortnite-stats-flask.git
cd fortnite-stats-flask
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your Fortnite API Key in `main.py`:

```python
api = "YOUR_API_KEY"
```

4. Run the application:

```bash
python main.py
```

5. Open your browser at:  
   👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ✅ Dependencies (`requirements.txt`)

```
Flask
requests
```

Generate it using:

```bash
pip freeze > requirements.txt
```

---

## 💡 Possible Future Improvements

- Error handling for invalid usernames or failed API calls
- Display more detailed mode-specific stats (K/D, matches played, etc.)
- Integrate interactive charts with Chart.js or Plotly
- Implement loading indicators or AJAX requests
- Improve responsiveness and UI with Bootstrap or Tailwind

---

## 👨‍💻 Author

**Alexis**  
GitHub: [https://github.com/your-username](https://github.com/Alexisluna10)

---
