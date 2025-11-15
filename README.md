# 🧪 Portfólio de Engenharia de Qualidade e Automação (SDET & Playwright)

Este repositório consolida projetos e artefatos de teste que demonstram proficiência em automação de testes End-to-End (E2E) com padrões modernos (Playwright/PyTest) e planejamento de qualidade.

---

## 1. 🧪 Testes de Automação E2E (YouTube Music)

Demonstração de proficiência na criação de testes End-to-End, seguindo uma metodologia SDET rigorosa (Exploração Manual + Implementação).

### 🎯 Metodologia SDET

Os testes foram desenvolvidos seguindo um **Prompt de Sistema (SDET Automator)**, que impôs um fluxo de trabalho em duas fases:
* **Fase 1 (Exploração Manual):** Análise de elementos interativos, estrutura HTML e atributos de acessibilidade (roles, labels).
* **Fase 2 (Implementação):** Criação de código automatizado usando **Playwright + PyTest**, priorizando localizadores acessíveis (`getByRole()`) e asserções nativas com auto-retry, conforme as **Regras Críticas** de qualidade definidas.

### ✅ Resultados de Execução (100% Sucesso)

O script validou o fluxo básico do **YouTube Music** com **4 testes E2E bem-sucedidos**:

| Caso de Teste | Objetivo | Resultado |
| :--- | :--- | :--- |
| `test_pagina_inicial` | Valida carregamento, título e elementos principais (navegação, login). | **PASS** |
| `test_navegacao_categorias` | Testa a seleção e mudança de conteúdo entre categorias (ex: Podcasts, Relax). | **PASS** |
| `test_navegacao_lateral` | Testa a transição entre as seções "Início" e "Explorar" na barra lateral. | **PASS** |
| `test_elementos_interativos` | Valida a presença e funcionalidade de botões de login e reprodução. | **PASS** |

**Comandos para Execução (Exemplo):**
```bash
# Executar os testes em modo visível (headed)
pytest playwright/e2e/test_youtube_music.py -v --headed

Cenário de Teste,Objetivo Principal,Artefatos Gerados
CT001 (Sucesso),Validar a adesão completa com pagamento autorizado.,1. Tabela de Endereço de Entrega. 2. Dados de Cartão Válido.
CT002 (Falha),Validar o tratamento de erro do sistema (pagamento recusado).,Dados de Cartão Inválido (Saldo Insuficiente).

Campo,Valor
CEP,04534-011
Logradouro,Rua Joaquim Floriano
Cartão,Visa Válido (4242...4242)

👨‍🏫 Créditos e Agradecimentos
Este portfólio de metodologias SDET e scripts de automação (Playwright/PyTest) foi construído e inspirado nos ensinamentos e padrões de qualidade do professor Fernando Papito.
