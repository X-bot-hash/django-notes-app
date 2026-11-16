# 📝 Django Notes App

<p align="center">
  <a href="#english">English</a> | <a href="#russian">Русский</a>
</p>

<p align="center">
  <a href="https://github.com/X-bot-hash/django-notes-app">
    <img src="https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github" alt="GitHub Repository">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Django-6.0%2B-092E20.svg?logo=django&logoColor=white" alt="Django">
  </a>
  <a href="https://getbootstrap.com/">
    <img src="https://img.shields.io/badge/Bootstrap-5.3-7952B3.svg?logo=bootstrap&logoColor=white" alt="Bootstrap">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
</p>

<hr>

<details id="english">
  <summary>English</summary>
  
## ✨ Features

- 📋 **List of notes** — sorted by creation date (newest first)
- ➕ **Create notes** — with field form validation
- 🔍 **Detailed view** — view full note content and creation date
- ✏️ **Edit** — change note title and content
- 🗑️ **Delete** — with confirmation before deletion
- ⚙️ **Django Admin** — manage notes through the built-in admin panel
- 🎨 **Modern interface** — responsive design on Bootstrap 5

## 🛠️ Technology Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite3

## 📁 Project Structure

```text
Django/
├── myproject/          # Main Django project configuration
│   ├── settings.py     # Project settings
│   ├── urls.py         # Main URL router
│   └── ...
├── notes/              # Notes application
│   ├── models.py       # Note model (title, body, created_at)
│   ├── views.py        # CRUD views
│   ├── forms.py        # Django Form for Note
│   ├── urls.py         # Application URL patterns
│   └── ...
├── templates/          # HTML templates
│   ├── base.html       # Base template (Bootstrap 5)
│   └── notes/          # CRUD note templates
├── manage.py           # Django management utility
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 🚀 Quick Start

### 1. Repository Cloning

```bash
git clone https://github.com/X-bot-hash/django-notes-app.git
cd django-notes-app
```

### 2. Create and Activate Virtual Environment

**Windows (PowerShell / CMD):**

```bash
python -m venv venv
.env\Scriptsctivate
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (optional)

For Django admin access:

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Open in browser: [http://127.0.0.1:8000/notes/](http://127.0.0.1:8000/notes/)
</details>

<details id="russian">
  <summary>Русский</summary>
  
## ✨ Основные возможности

- 📋 **Список заметок** — сортировка по дате создания (сначала новые)
- ➕ **Создание заметок** — с валидацией полей формы
- 🔍 **Детальный просмотр** — просмотр полного содержания заметки и даты создания
- ✏️ **Редактирование** — изменение заголовка и содержимого заметок
- 🗑️ **Удаление заметок** — с подтверждением перед удалением
- ⚙️ **Django Admin** — управление заметками через встроенную панель администратора
- 🎨 **Современный интерфейс** — адаптивный дизайн на Bootstrap 5

## 🛠️ Технологический стек

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite3

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
.env\Scriptsctivate
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
</details>

<hr>

## 📄 License

This project is distributed under the MIT License.
