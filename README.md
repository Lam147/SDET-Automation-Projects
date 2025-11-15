# 🧪 Portfólio de Engenharia de Qualidade e Automação (SDET & Playwright)

Este repositório demonstra proficiência em automação de testes End-to-End (E2E), aplicando uma metodologia SDET rigorosa com as ferramentas Playwright e PyTest.

---

## 1. 🧪 Testes de Automação E2E (YouTube Music)

O projeto valida funcionalidades básicas da página inicial do YouTube Music.

### 🎯 Metodologia SDET

Os testes foram desenvolvidos seguindo um **Prompt de Sistema (SDET Automator)**, priorizando um fluxo de trabalho em duas fases:
* **Fase 1 (Exploração Manual):** Análise da estrutura HTML e atributos de acessibilidade.
* **Fase 2 (Implementação):** Criação de código automatizado, priorizando localizadores acessíveis (`getByRole()`) e aderindo a **Regras Críticas** de qualidade e robustez.

### ✅ Resultados de Execução (100% Sucesso)

O script validou o fluxo básico do **YouTube Music** com **4 testes E2E bem-sucedidos**:

| Caso de Teste | Objetivo | Resultado |
| :--- | :--- | :--- |
| `test_pagina_inicial` | Valida carregamento, título e elementos principais (navegação, login). | **PASS** |
| `test_navegacao_categorias` | Testa a seleção e mudança de conteúdo entre categorias. | **PASS** |
| `test_navegacao_lateral` | Testa a transição entre as seções "Início" e "Explorar". | **PASS** |
| `test_elementos_interativos` | Valida a presença e funcionalidade de botões de login e reprodução. | **PASS** |

**Comandos para Execução (Exemplo):**
```bash
# Executar os testes em modo visível (headed)
pytest playwright/e2e/test_youtube_music.py -v --headed

👨‍🏫 Créditos e Agradecimentos
Este projeto de automação (Playwright/PyTest) foi construído e inspirado nos ensinamentos e padrões de qualidade do professor Fernando Papito.
