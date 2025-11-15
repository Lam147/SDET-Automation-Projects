import pytest
from playwright.sync_api import Page, expect

@pytest.mark.e2e
def test_youtube_music_pagina_inicial(page: Page):
    page.goto('https://music.youtube.com/')
    expect(page).to_have_url('https://music.youtube.com/')

    # Barra lateral: .first evita strict mode
    expect(page.get_by_role('link', name='Início').first).to_be_visible()
    expect(page.get_by_role('link', name='Explorar').first).to_be_visible()
    expect(page.get_by_role('link', name='Biblioteca').first).to_be_visible()

    # Categorias: validação genérica
    expect(page.get_by_role('heading', level=2).first).to_be_visible()

    # Botão de login
    expect(page.get_by_role('button', name='Fazer login')).to_be_visible()


@pytest.mark.e2e
def test_youtube_music_navegacao_categorias(page: Page):
    page.goto('https://music.youtube.com/')
    expect(page).to_have_url('https://music.youtube.com/')

    podcasts_tab = page.get_by_role('tab', name='Podcasts')
    expect(podcasts_tab).to_be_visible()
    podcasts_tab.click()
    expect(podcasts_tab).to_have_attribute('aria-selected', 'true')

    # Validação genérica de conteúdo (qualquer heading)
    expect(page.get_by_role('heading', level=2).first).to_be_visible()


@pytest.mark.e2e
def test_youtube_music_navegacao_lateral(page: Page):
    page.goto('https://music.youtube.com/')
    expect(page).to_have_url('https://music.youtube.com/')

    explorar = page.get_by_role('link', name='Explorar').first
    explorar.click()
    expect(explorar).to_be_visible()

    inicio = page.get_by_role('link', name='Início').first
    inicio.click()
    expect(inicio).to_be_visible()
    expect(page.get_by_role('tab', name='Podcasts')).to_be_visible()


@pytest.mark.e2e
def test_youtube_music_elementos_interativos(page: Page):
    page.goto('https://music.youtube.com/')
    expect(page).to_have_url('https://music.youtube.com/')

    login = page.get_by_role('button', name='Fazer login')
    expect(login).to_be_visible()
    expect(login).to_be_enabled()

    # Botão de play via aria-label
    play_btn = page.locator('button[aria-label*="Reproduzir"]').first
    expect(play_btn).to_be_visible()

    # Links de música
    music_link = page.locator('a[href*="watch"], a[href*="playlist"]').first
    expect(music_link).to_be_visible()
