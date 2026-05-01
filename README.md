# ♟️ Chaturanga

> *Chaturanga* (चतुरंग) — the ancient Indian predecessor to modern chess.

> ⚠️ **This project is currently under active development.** Expect incomplete features and breaking changes.

---

## 🚧 Development Status

| Component | Status |
|---|---|
| Chess Engine | 🔨 In Progress |
| Django REST API | 🔨 In Progress |
| Database Models | 🔨 In Progress |
| Tests (pytest) | 🔨 In Progress |
| Frontend / UI | 📋 Planned |
| Authentication | 📋 Planned |
| Deployment | 📋 Planned |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.x |
| API | Django REST Framework 3.15+ |
| Database | PostgreSQL |
| Testing | pytest, pytest-django |
| Language | Python 3 |

---

## ⚙️ Local Setup

```bash
git clone https://github.com/svedant1207/Chaturanga.git
cd Chaturanga
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/chaturanga
ALLOWED_HOSTS=localhost,127.0.0.1
```

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🗺️ Roadmap

- [ ] Core chess engine — move generation & validation
- [ ] Game model & database schema
- [ ] REST API for creating and playing games
- [ ] Player authentication
- [ ] Frontend / UI
- [ ] AI opponent
- [ ] Deployment setup

---

## 👤 Author

**Vedant S** — [@svedant1207](https://github.com/svedant1207)
