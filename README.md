# TubeArchivist Discord Bot

## Setup
Environment:
- `BOT_TOKEN`: Register bot on the server to get token

## Install
Compose file:
```yml
services:
  discord-bot:
    container_name: discord-bot
    build: https://github.com/tubearchivist/discord-bot.git
    restart: always
    env_file:
      - ./env/discord-bot.env
```
