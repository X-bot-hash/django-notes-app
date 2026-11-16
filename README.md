# 📝 Django Notes App

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0%2B-092E20.svg?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3.svg?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Простое и удобное веб-приложение для управления личными заметками, написанное на **Django** с использованием UI-фреймворка **Bootstrap 5**.

---

## ✨ Основные возможности

- 📋 **Просмотр списка заметок** — сортировка по дате создания (сначала новые).
- ➕ **Создание заметок** — с валидацией полей формы.
- 🔍 **Детальный просмотр** — просмотр полного содержания заметки и даты создания.
- ✏️ **Редактирование** — изменение заголовка и содержимого заметок.
- 🗑️ **Удаление заметок** — с подтверждением перед удалением.
- ⚙️ **Django Admin** — управление заметками через встроенную панель администратора.
- 🎨 **Современный интерфейс** — адаптивный дизайн на Bootstrap 5.

---

## 🛠️ Технологический стек

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite3

---

## 📁 Структура проекта

```
Django/
├── myproject/          # Основной модуль конфигурации Django
│   ├── settings.py     # Настройки проекта
│   ├── urls.py         # Главный URL-маршрутизатор
│   └── ...
├── notes/              # Приложение заметок
│   ├── models.py       # Модель Note (title, body, created_at)
│   ├── views.py        # Представления CRUD
│   ├── forms.py        # Django Form для Note
│   ├── urls.py         # URL-маршруты приложения
│   └── ...
├── templates/          # HTML-шаблоны
│   ├── base.html       # Базовый шаблон (Bootstrap 5)
│   └── notes/          # Шаблоны CRUD заметок
├── manage.py           # Утилита управления Django
├── requirements.txt    # Зависимости проекта
└── README.md           # Документация проекта
```

---

## 🚀 Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/X-bot-hash/django-notes-app.git
cd django-notes-app
```

### 2. Создание и активация виртуального окружения

**Windows (PowerShell / CMD):**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Применение миграций

```bash
python manage.py migrate
```

### 5. Создание суперпользователя (опционально)

Для доступа к админ-панели Django:
```bash
python manage.py createsuperuser
```

### 6. Запуск сервера разработки

```bash
python manage.py runserver
```

Откройте в браузере: [http://127.0.0.1:8000/notes/](http://127.0.0.1:8000/notes/)

---

## 📝 Пример использования URL-маршрутов

| URL | Метод | Описание |
|---|---|---|
| `/notes/` | GET | Список всех заметок |
| `/notes/create/` | GET, POST | Форма создания заметки |
| `/notes/<id>/` | GET | Детальная страница заметки |
| `/notes/<id>/edit/` | GET, POST | Форма редактирования заметки |
| `/notes/<id>/delete/` | GET, POST | Подтверждение и удаление заметки |
| `/admin/` | GET, POST | Админ-панель Django |

---

## 📄 Лицензия

Этот проект распространяется под лицензией MIT.
