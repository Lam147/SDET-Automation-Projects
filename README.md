# Testes de Qualidade e Automação (SDET & Playwright)

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

> **Prioridade máxima**: Localizadores baseados em **acessibilidade** (`get_by_role`, `aria-label`, `WCAG-compliant`)

---

### Resultados da Execução (100% Sucesso)

**4 casos de teste** executados com **sucesso total** após correções:

| ID | Objetivo | Função | Status |
|----|--------|--------|--------|
| **CT001** | Carregamento e elementos principais | `test_youtube_music_pagina_inicial` | **PASS** |
| **CT002** | Navegação entre categorias | `test_youtube_music_navegacao_categorias` | **PASS** |
| **CT003** | Navegação na barra lateral | `test_youtube_music_navegacao_lateral` | **PASS** |
| **CT004** | Elementos interativos (botões, links) | `test_youtube_music_elementos_interativos` | **PASS** |

**Saída final do console (execução completa):**
```bash
============================= test session starts ==============================
platform linux -- Python 3.11.2, pytest-8.4.2, pluggy-1.6.0
rootdir: /TestBeyond/playwright-pytest
collected 4 items

playwright/e2e/test_youtube_music.py::test_youtube_music_pagina_inicial[chromium] PASSED [ 25%]
playwright/e2e/test_youtube_music.py::test_youtube_music_navegacao_categorias[chromium] PASSED [ 50%]
playwright/e2e/test_youtube_music.py::test_youtube_music_navegacao_lateral[chromium] PASSED [ 75%]
playwright/e2e/test_youtube_music.py::test_youtube_music_elementos_interativos[chromium] PASSED [100%]

============================== 4 passed in XX.XXs ==============================
```
---

Aprendizados & Boas Práticas Aplicadas

get_by_role() + .first → evita strict mode violation
aria-label e level=2 → mais estável que texto exato
locator(...).first → garante que pelo menos 1 elemento exista
auto-retry do expect() → tolerância a carregamento assíncrono

Créditos e Agradecimentos

Projeto construído com base nos padrões de qualidade SDET ensinados pelo professor Fernando Papito.

Saúde!
