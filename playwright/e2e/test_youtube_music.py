import pytest
import re
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function")
def page_context(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => false});")
    page.goto('https://music.youtube.com/', wait_until="networkidle")
    yield page


@pytest.mark.e2e
def test_youtube_music_carregamento(page_context: Page):
    page = page_context
    expect(page).to_have_url("https://music.youtube.com/")
    expect(page).to_have_title(re.compile("YouTube Music"))


@pytest.mark.e2e
def test_youtube_music_barra_lateral(page_context: Page):
    page = page_context
    expect(page.locator("#guide-inner-content a").first).to_be_visible(timeout=10000)


@pytest.mark.e2e
def test_youtube_music_categorias(page_context: Page):
    page = page_context
    expect(page.locator('[role="tab"]').first).to_be_visible(timeout=10000)


@pytest.mark.e2e
def test_youtube_music_interatividade(page_context: Page):
    page = page_context
    expect(page.locator('button[aria-label*="play"], button[title*="play"]')).to_have_count(gte=1, timeout=10000)
