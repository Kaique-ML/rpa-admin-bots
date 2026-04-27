# 🤖 RPA Bot para Processos Administrativos
> Automação de tarefas administrativas repetitivas: formulários, sistemas legados e relatórios

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.21-43B02A?logo=selenium)](https://selenium.dev)
[![Playwright](https://img.shields.io/badge/Playwright-Async-45ba4b)](https://playwright.dev/python)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker)](https://docker.com)

## 🎯 Sobre

Conjunto de **bots RPA** para automatizar as tarefas administrativas mais comuns: preenchimento de formulários em sistemas web legados, download e organização de documentos, sincronização entre sistemas e geração de relatórios.

**Redução de tempo:** 200h/mês → totalmente automático.

## 🤖 Bots Incluídos

| Bot | Tarefa | Economia |
|-----|--------|---------|
| `form_filler` | Preenchimento de formulários web | 40h/mês |
| `doc_downloader` | Download e organização de documentos | 30h/mês |
| `data_sync` | Sincronização entre sistemas | 60h/mês |
| `report_collector` | Coleta e consolidação de relatórios | 50h/mês |
| `email_processor` | Processamento automático de e-mails | 20h/mês |

## 🚀 Rodando

```bash
git clone https://github.com/Kaique-ML/rpa-admin-bots
cd rpa-admin-bots

pip install -r requirements.txt
playwright install chromium

python -m bots.form_filler --config config/form_filler.yaml
python scheduler.py
```

---
**Gabriel Kaique Portel Silva** | [LinkedIn](https://linkedin.com/in/gabriel-kaique-881475284) | [GitHub](https://github.com/Kaique-ML)
