import re
from playwright.sync_api import Page, expect

def test_playwright_site_search_and_navigation(page: Page):
    # Шаг 1: Открываем главную страницу и проверяем наличие текста
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
    expect(page.get_by_text("Playwright enables reliable end-to-end testing")).to_be_visible()

    # Шаг 2: Работа с интерактивным элементом — клик по ссылке "Docs"
    page.get_by_role("link", name="Docs").click()
    expect(page).to_have_url(re.compile("/docs/intro"))
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

    # Шаг 3: Работа с формой поиска — вводим запрос и проверяем результат
    search_button = page.get_by_role("button", name="Search")
    search_button.click()

    search_input = page.get_by_placeholder("Search docs")
    search_input.fill("locator")
    page.keyboard.press("Enter")

    expect(page.get_by_text("Locators", exact=False).first).to_be_visible()
import re
from playwright.sync_api import Page, expect

def test_playwright_site_search_and_navigation(page: Page):
    # Шаг 1: Открываем главную страницу и проверяем наличие текста
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
    # Новый текст на главной странице
    expect(page.get_by_role("heading", name="Playwright enables reliable web automation")).to_be_visible()

    # Шаг 2: Работа с интерактивным элементом — клик по ссылке "Docs"
    page.get_by_role("link", name="Docs").click()
    expect(page).to_have_url(re.compile("/docs/intro"))
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

    # Шаг 3: Работа с формой поиска — вводим запрос и проверяем результат
    search_button = page.get_by_role("button", name="Search")
    search_button.click()

    search_input = page.get_by_placeholder("Search docs")
    search_input.fill("locator")
    page.keyboard.press("Enter")

    expect(page.get_by_text("Locators", exact=False).first).to_be_visible()

