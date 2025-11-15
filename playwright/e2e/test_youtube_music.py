import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function")
def page_with_bypass(page: Page):
    # Spoof user-agent + bypass bot detection
    context = page.context
    context.add_cookies([{
        "name": "CONSENT",
        "value": "YES+cb20221114-18-p0.en+FX+123",
        "domain": ".youtube.com",
        "path": "/"
    }])
    page.goto("https://music.youtube.com/", wait_until="domcontentloaded")
    page.wait_for_timeout(3000)  # Espera JS carregar
    yield page

@pytest.mark.e2e
def test_homepage_loads(page_with_bypass: Page):
    expect(page_with_bypass).to_have_url("https://music.youtube.com/")

@pytest.mark.e2e
def test_sidebar_exists(page_with_bypass: Page):
    expect(page_with_bypass.locator("ytmusic-guide-renderer a").first).to_be_visible(timeout=15000)

@pytest.mark.e2e
def test_category_tabs(page_with_bypass: Page):
    expect(page_with_bypass.locator('[role="tab"]').first).to_be_visible(timeout=15000)

@pytest.mark.e2e
def test_play_buttons(page_with_bypass: Page):
    buttons = page_with_bypass.locator('button[aria-label*="play" i], button[title*="play" i]')
    expect(buttons).to_have_count(greater_than_or_equal=1, timeout=15000)
