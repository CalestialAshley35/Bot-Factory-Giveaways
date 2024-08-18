# Bot Factory Giveaways

**Bot Factory Giveaways** by Calestial Ashley is a simple and user-friendly module for creating and managing giveaways on your Discord server using Python. This module allows server administrators to host giveaways, where users can enter by reacting to a message, and a random winner is selected after a specified duration.

## Features
- **Start Giveaways:** Create a giveaway with a custom prize and duration in minutes.
- **Automatic Winner Selection:** The bot automatically picks a random winner after the giveaway ends.
- **Reroll:** If needed, you can reroll to select a new winner.

## Setup Instructions

### 1. Clone the Repository
To get started, clone the repository or fork it from [Bot Factory Giveaways on Replit](https://replit.com/@calestialashley/Bot-Factory-Giveaways?s=app).

### 2. Install Dependencies
Ensure `discord.py` is installed. Run the following command in your Replit Shell:
```bash
pip install discord.py
```

### 3. Add Your Bot Token
Replace `'YOUR_BOT_TOKEN'` in `main.py` with your actual Discord bot token. You can obtain the token from the [Discord Developer Portal](https://discord.com/developers/applications).

### 4. Run the Bot
Click the "Run" button in Replit to start the bot.

## Usage

### Commands

1. **Start a Giveaway**
   - Command: `!giveaway <minutes> <prize>`
   - Example: `!giveaway 10 $10 Amazon Gift Card`
   - This command will start a giveaway that lasts for the specified number of minutes. Users can enter by reacting with 🎉.

2. **Reroll the Winner**
   - Command: `!reroll <message_id>`
   - Example: `!reroll 123456789012345678`
   - Use this command to select a new winner if the original winner is not available or to reroll for any other reason.

### Permissions
- The bot requires administrator permissions to manage giveaways and reroll winners.

### Notes
- Make sure the bot has permissions to add reactions and read message reactions in your Discord server.

## License
This project is licensed under the MIT License. Feel free to modify and distribute it as per the terms of the license.

## Contributing
Contributions are welcome! If you have ideas or improvements, feel free to fork the repository and submit a pull request.

## Contact
For support or questions, you can reach out to Calestial Ashley on [GitHub](https://github.com/CalestialAshley35) or join the support Discord server.

---

Enjoy using Bot Factory Giveaways to enhance your Discord server with fun and engaging giveaways! 🎉
