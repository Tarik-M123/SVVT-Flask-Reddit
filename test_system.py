from playwright.sync_api import sync_playwright
import time

def test_homepage_title():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:5000')
        assert page.title() == 'Flask reddit'
        browser.close()

def test_login_page_has_form():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:5000/auth/login')
        assert page.locator('input[name="email"]').is_visible()
        assert page.locator('input[name="password"]').is_visible()
        browser.close()

def test_register_page_has_form():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:5000/auth/register')
        assert page.locator('input[name="username"]').is_visible()
        assert page.locator('input[name="email"]').is_visible()
        browser.close()

def test_register_new_user():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:5000/auth/register')
        unique = str(int(time.time()))
        page.fill('input[name="username"]', f'user{unique}')
        page.fill('input[name="email"]', f'user{unique}@test.com')
        page.fill('input[name="password"]', 'testpass123')
        page.fill('input[name="confirm_password"]', 'testpass123')
        page.click('input[type="submit"]')
        page.wait_for_load_state('networkidle')
        assert page.url != 'http://localhost:5000/auth/register'
        browser.close()

def test_communities_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:5000/communities')
        assert 'communities' in page.url
        browser.close()

def test_homepage_shows_posts():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:5000')
        assert page.locator('h3').count() > 0
        browser.close()
