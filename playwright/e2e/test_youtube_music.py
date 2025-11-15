import pytest
import re
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function")
def page_bypass_bot(page: Page):
    page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {get: () => false});
        Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3]});
        Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
    """)
    page.set_extra_http_headers({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    })
    page.goto("https://music.youtube.com/", wait_until="domcontentloaded")
    page.wait_for_timeout(5000)
    yield page


@pytest.mark.e2e
def test_homepage_loads(page_bypass_bot: Page):
    expect(page_bypass_bot).to_have_url("https://music.youtube.com/")


@pytest.mark.e2e
def test_sidebar_has_links(page_bypass_bot: Page):
    expect(page_bypass_bot.locator("a[href*='youtube.com']").first).to_be_visible(timeout=20000)


@pytest.mark.e2e
def test_has_play_buttons(page_bypass_bot: Page):
    buttons = page_bypass_bot.locator("button").filter(has_text=re.compile("play|reproduzir", re.I))
    expect(buttons).to_have_count(greater_than=0, timeout=20000)


@pytest.mark.e2e
def test_has_content_sections(page_bypass_bot: Page):
    expect(page_bypass_bot.locator("ytmusic-section-list-renderer").first).to_be_visible(timeout=20000)
