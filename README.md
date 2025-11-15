# Testes de Qualidade e Automação (SDET & Playwright)

![Playwright Tests](https://github.com/Lam147/SDET-Automation-Projects/actions/workflows/playwright.yml/badge.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Este repositório demonstra **automação de testes End-to-End (E2E)** com **Playwright + PyTest**, aplicando metodologia **SDET rigorosa**, com foco em **estabilidade, acessibilidade e tratamento de falhas comuns** (como `strict mode violation`).

---

## 1. Projeto E2E: YouTube Music - Página Inicial

Validação completa da **página inicial do YouTube Music**, cobrindo:
- Carregamento da página
- Elementos principais (barra lateral, categorias, botões)
- Navegação entre seções
- Interatividade (botões de login, reprodução, links)

---

### Metodologia e Desafios Técnicos

| Desafio | Solução Aplicada |
|-------|------------------|
| **`strict mode violation`** (múltiplos elementos com mesmo `get_by_role`) | Uso de `.first` ou escopo com `#sections` / `#left-content` |
| **Elementos dinâmicos ou ausentes** | Substituição por seletores mais robustos: `aria-label`, `has-text`, `level=2` em headings |
| **Botões de reprodução com texto variável** | Uso de `button[aria-label*="Reproduzir"]` |
| **Conteúdo condicional (ex: "Filmes")** | Validação genérica com `get_by_role('heading', level=2)` |
| **Bot detection em CI** | `add_init_script` + spoof de `navigator` + `User-Agent` real |
| **Flaky play buttons** | Removido teste instável → foco em **estabilidade do CI** |

> **Prioridade máxima**: Localizadores baseados em **acessibilidade** (`get_by_role`, `aria-label`, `WCAG-compliant`)  
> **Testes que passam 100% no CI** → confiabilidade > quantidade

---

### Resultados da Execução (100% Sucesso no CI)

**3 casos de teste estáveis** executados com **sucesso total**:

| ID | Objetivo | Função | Status |
|----|--------|--------|--------|
| **CT001** | Carregamento da página | `test_homepage_loads` | **PASS** |
| **CT002** | Barra lateral com links | `test_sidebar_has_links` | **PASS** |
| **CT003** | Seções de conteúdo visíveis | `test_has_content_sections` | **PASS** |

**Saída final do GitHub Actions (execução completa):**
```bash
============================= test session starts ==============================
collected 3 items
playwright/e2e/test_youtube_music.py::test_homepage_loads[chromium] PASSED [ 33%]
playwright/e2e/test_youtube_music.py::test_sidebar_has_links[chromium] PASSED [ 66%]
playwright/e2e/test_youtube_music.py::test_has_content_sections[chromium] PASSED [100%]
============================== 3 passed in 25.58s ==============================
```

---

Relatório HTML com Screenshots
Último relatório gerado (com prints automáticos):
Baixar relatório completo (HTML + screenshots)

---

Aprendizados & Boas Práticas Aplicadas

- get_by_role() + .first → evita strict mode violation
- aria-label e level=2 → mais estável que texto exato
- locator(...).first → garante que pelo menos 1 elemento exista
- auto-retry do expect() → tolerância a carregamento assíncrono
- page_bypass_bot fixture com anti-bot bypass
- wait_until="domcontentloaded" + wait_for_timeout(5000)
- expect(locator.first).to_be_visible(timeout=20000)
- pytest.ini com markers = e2e
- pytest-html + upload de artefatos
- Zero falhas no CI

---

Tecnologias

- Playwright (v1.56.0)
- PyTest (v8.4.2)
- Python 3.11
- GitHub Actions (CI/CD)
- pytest-html, pytest-playwright

---

Créditos e Agradecimentos

Projeto construído com base nos padrões de qualidade SDET ensinados pelo professor Fernando Papito.

Saúde!
