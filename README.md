# Currency-Converter-API

Currency Converter API — простий конвертер валют на FastAPI.

## Встановлення

1. Клонуйте репозиторій:
	```bash
	git clone https://github.com/your-username/Currency-Converter-API.git
	cd Currency-Converter-API
	```
2. Встановіть залежності:
	```bash
	pip install -r requirements.txt
	```
	або вручну:
	```bash
	pip install fastapi uvicorn python-dotenv requests
	```
3. Створіть файл `.env` у корені проєкту та додайте ваш API ключ:
	```env
	API_EXCHANGERATE=your_api_key_here
	```

## Запуск

Запустіть сервер у режимі розробки:
```bash
uvicorn main:app --reload
```
Сервер буде доступний за адресою: http://127.0.0.1:8000/

## Використання API

- Головна сторінка (приклад):
  - `GET /` — повертає поточний курс USD до UAH у форматі JSON.

## Документація

Автоматична документація доступна за адресою:
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

---
**Примітка:** Не забувайте додавати `.env` у `.gitignore`, щоб не зберігати секрети у репозиторії.
