# FullAndPointBot  
A Telegram bot that facilitates communication with problem authors for an olympiad. The process consists of several steps:  

- Entering the problem authors  
- Entering the problem statement  
- Confirmation before submission  

## Commands  
- `/start` – Start working with the bot  
- "Submit Problem" – Begin the problem submission process  

## How to Use  
1. Start a conversation with the bot using the `/start` command  
2. Click the "Submit Problem" button  
3. Follow the bot's instructions  

## Technical Details  
- The bot is written in Python using the `pyTelegramBotAPI` library  
- Supports confirmation/cancellation before submission  
- Automatically restores connection if interrupted  

To run the bot, you need to set `BOT_TOKEN` and `GROUP_ID` in the code.  
