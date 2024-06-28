# Discord Bot

This Bot is a versatile Discord bot designed to enhance your server experience. It comes equipped with various features including greeting new members, responding to specific commands, voice channel management, content moderation, and even integrating external APIs like jokes and translations.

## Features

- **Greeting New Members**: Sends a welcome message to new members joining the server.
- **Command Responses**: Responds to specific commands like `!hello` and `!angrycat`.
- **Voice Channel Management**: Commands to join and leave voice channels.
- **Content Moderation**: Deletes messages containing specific bad words.
- **Embeds**: Sends rich embed messages.
- **AI Integration**: Chat with Gemini AI for intelligent responses.
- **Translations**: Translate messages to English using Google Translate.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nowa0281/discord-bot.git
   cd leobot
   ```

2. Install the required packages:
   ```bash
   pip install googletrans==3.1.0a0
   ```

3. Set up environment variables:
   - `DISCORD_TOKEN`: Your Discord bot token.
   - `GEMINI_API_KEY`: Your Gemini AI API key.


### Commands

- `!hello`: The bot will greet you.
- `!join`: The bot will join your voice channel.
- `!leave`: The bot will leave the voice channel.
- `!angrycat`: Sends an embed message with an angry cat image.
- `!dancingcat`: Sends an embed message with a dancing cat image.
- `!translate [message]`: Translates the given message to English.
- `!ask [question]`: Asks a question to Gemini AI and receives a response.


## Usage

Run the bot with:
```bash
python bot.py
```


### Event Listeners

- `on_member_join`: Welcomes new members and sends a joke.
- `on_member_remove`: Says goodbye to members who leave.
- `on_message`: Checks for specific messages and responds accordingly. Handles translation and AI question commands.

## Configuration

Customize the bot behavior by modifying the source code as needed. Ensure to replace placeholders like `"your channel ID"` and `API_KEY` with actual values.

## License

This project is licensed under the  GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
.

---

Feel free to contribute to this project by opening issues or submitting pull requests on [GitHub](https://github.com/nowa0281/discord-bot.git).

Enjoy using Bot!