# Playwright Web Tests

Тесты на Python + Playwright для проверки веб-сервиса `playwright.dev`.

## Что проверяется
- Наличие текста на главной странице
- Переход по ссылке "Docs"
- Работа формы поиска (ввод запроса + Enter)

## Запуск
pip install -r requirements.txt
playwright install chromium
pytest tests/ -v
