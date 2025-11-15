# 🧪 Portfólio de Engenharia de Qualidade e Automação (SDET & Playwright)

Este repositório é dedicado à automação de testes End-to-End (E2E), demonstrando proficiência em **Playwright + PyTest** e na aplicação de uma metodologia SDET rigorosa.

---

## 1. 🧪 Projeto E2E: YouTube Music - Página Inicial

Este projeto valida as funcionalidades e a robustez dos elementos da **página inicial do YouTube Music**, garantindo a qualidade da experiência do usuário em diferentes fluxos de navegação.

### 🎯 Metodologia e Desafios Técnicos

A automação seguiu as melhores práticas de SDET:

* **Prioridade `getByRole()`:** Utilização de localizadores de acessibilidade (como `get_by_role('link', name='Início')`) para máxima estabilidade e conformidade com WCAG.
* **Tratamento de Localizadores:** O código foi ajustado para resolver **conflitos de `strict mode violation`** (onde múltiplos elementos correspondiam ao mesmo localizador), garantindo o direcionamento correto dos elementos através do uso de métodos como `.first`.
* **Asserções Robustas:** Uso de `expect()` nativo do Playwright com *auto-retry* para estabilidade.

### ✅ Resultados Detalhados da Execução (100% Sucesso)

O script validou com sucesso **4 casos de teste**, demonstrando cobertura de navegação, carregamento e interatividade:

| ID do Teste | Objetivo Principal | Função no Código | Resultado |
| :--- | :--- | :--- | :--- |
| **CT001** | Validação de Carregamento e Elementos Principais. | `test_youtube_music_pagina_inicial` | **PASS** |
| **CT002** | Navegação e Seleção de Categorias de Música. | `test_youtube_music_navegacao_categorias` | **PASS** |
| **CT003** | Teste de Transição na Barra Lateral (Início/Explorar). | `test_youtube_music_navegacao_lateral` | **PASS** |
| **CT004** | Validação da Presença de Elementos Interativos (Botões). | `test_youtube_music_elementos_interativos` | **PASS** |

**Saída de Execução (Console):**

============================= test session starts ============================== ... playwright/e2e/test_youtube_music.py::test_youtube_music_pagina_inicial[chromium] PASSED [ 25%] playwright/e2e/test_youtube_music.py::test_youtube_music_navegacao_categorias[chromium] PASSED [ 50%] playwright/e2e/test_youtube_music.py::test_youtube_music_navegacao_lateral[chromium] PASSED [ 75%] playwright/e2e/test_youtube_music.py::test_youtube_music_elementos_interativos[chromium] PASSED [100%] ============================== 4 passed in 1X.XXs ==============================

### 💻 Exemplo de Código (Trecho)

O código demonstra o uso de localizadores robustos e asserções claras.

```python
@pytest.mark.e2e
def test_youtube_music_pagina_inicial(page):
    # Navegar para o YouTube Music e validar a URL
    page.goto('[https://music.youtube.com/](https://music.youtube.com/)')
    expect(page).to_have_url('[https://music.youtube.com/](https://music.youtube.com/)')
    
    # Validar elementos da barra lateral (usando .first para resolver o strict mode)
    expect(page.get_by_role('link', name='Início').first).to_be_visible()
    expect(page.get_by_role('link', name='Explorar').first).to_be_visible()
    
    # Validar que a barra de categorias está visível
    expect(page.get_by_role('tab', name='Podcasts')).to_be_visible()
    
    # Validar botão de login
    expect(page.get_by_role('button', name='Fazer login')).to_be_visible()
´´´

👨‍🏫 Créditos e Agradecimentos
Este projeto de automação (Playwright/PyTest) foi construído e inspirado nos ensinamentos e padrões de qualidade do professor Fernando Papito.

Saúde
