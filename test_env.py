from playwright.sync_api import sync_playwright

try:
    with sync_playwright() as p:
        print("Playwright initialized.")
        browser = p.chromium.launch(headless=True)
        print("Browser launched (headless).")
        page = browser.new_page()
        page.goto("https://example.com")
        print(f"Page title: {page.title()}")
        browser.close()
        print("Test passed.")
except Exception as e:
    print(f"Test failed: {e}")
