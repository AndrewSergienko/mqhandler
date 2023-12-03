# Message Queue Handler
<p align="center">
    <a href="https://codecov.io/gh/AndrewSergienko/mqhandler" > 
     <img src="https://codecov.io/gh/AndrewSergienko/mqhandler/graph/badge.svg?token=F3F4314Z6B"/> 
    </a>
    <img src="https://img.shields.io/badge/python-3.10.12-blue?logo=python" alt="Python Version">
    <a href="https://github.com/AndrewSergienko/simple-cdn-server/actions">
        <img src="https://img.shields.io/badge/tests-passed-green?logo=github" alt="Actions">
    </a>
    <a href="https://github.com/AndrewSergienko/simple-cdn-server/actions">
        <img src="https://github.com/AndrewSergienko/mqhandler/actions/workflows/docker.yml/badge.svg" alt="Actions">
    </a>
    <a href=https://results.pre-commit.ci/latest/github/AndrewSergienko/simple-cdn-server/master>
        <img src=https://results.pre-commit.ci/badge/github/AndrewSergienko/simple-cdn-server/master.svg>
    </a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code_style-black-black" alt="black"></a>
</p>

**mqhandler-bot**: https://github.com/AndrewSergienko/mqhandler-bot

## Про проект:
**Message Queue Handler** - це програма-виконавець, яка слухає дві черги повідомлень:

* Черга `"0"` - черга для команд
* Черга `"1"` - черга для інформації про повідомлення

**Команди**:
* ```print``` - вивести останнє повідомлення на екран
* ```send``` - надіслати POST запит з повідомленням

**Формат повідомлення:**
```json
{
  "username": "string",
  "text": "string",
  "time": "string (ISO format)"
}
```

## Інструкція по запуску:
1. Створити файл `.env`, заповнити його по прикладу з файла `.env.example`
2. Запустити команду `docker compose up`

## Тестування
Тести для програми находяться в папці `tests`. Для тестування використовується `pytest` та `coverage`
для визначення покриття тестами.

Тести запускаються за допомогою команди `pytest --cov tests`
