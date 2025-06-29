<p align="center">
  <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png" width="120" alt="Pikachu Sprite">
</p>

<h3 align="center">
<pre style="overflow-y:scroll; max-width:40px; height:30px;">
 _____                                                                                 _____ 
( ___ )-------------------------------------------------------------------------------( ___ )
 |   |                                                                                 |   | 
 |   |  ███████████           █████                █████████     ██████    █████       |   | 
 |   | ░░███░░░░░███         ░░███                ███░░░░░███  ███░░░░███ ░░███        |   | 
 |   |  ░███    ░███  ██████  ░███ █████  ██████ ░███    ░░░  ███    ░░███ ░███        |   | 
 |   |  ░██████████  ███░░███ ░███░░███  ███░░███░░█████████ ░███     ░███ ░███        |   | 
 |   |  ░███░░░░░░  ░███ ░███ ░██████░  ░███████  ░░░░░░░░███░███   ██░███ ░███        |   | 
 |   |  ░███        ░███ ░███ ░███░░███ ░███░░░   ███    ░███░░███ ░░████  ░███      █ |   | 
 |   |  █████       ░░██████  ████ █████░░██████ ░░█████████  ░░░██████░██ ███████████ |   | 
 |   | ░░░░░         ░░░░░░  ░░░░ ░░░░░  ░░░░░░   ░░░░░░░░░     ░░░░░░ ░░ ░░░░░░░░░░░  |   | 
 |___|                                                                                 |___| 
(_____)-------------------------------------------------------------------------------(_____)
</pre>
  </h3>
  <br>
<h1 align="center">
  <span style="font-size: 1.5em; color: #3b82f6;">Catch, Battle, Evolve!</span>
</h1>

<p align="center">
  Embark on an exciting journey in this captivating Command Line Interface (CLI) RPG, deeply inspired by the beloved classic Pokémon games! Built with Python and powered by MySQL, this adventure invites you to explore, catch powerful Pokémon, challenge formidable Gym Leaders, and ultimately rise to become a true Pokémon Master.
</p>

<p align="center">
  <a href="#features">✨ Features</a> •
  <a href="#getting-started">🚀 Getting Started</a> •
  <a href="#gameplay">🎮 Gameplay</a> •
  <a href="#technologies-used">⚡ Technologies Used</a> •
  <a href="#database-schema">🗃️ Database Schema</a> •
  <a href="#future-enhancements">🚧 Future Enhancements</a> •
  <a href="#contributing">🤝 Contributing</a> •
  <a href="#license">📄 License</a> •
  <a href="#acknowledgements">🙏 Acknowledgements</a>
</p>

---

## ✨ Features

-   **Catch 'Em All! 🎯** Encounter and capture a diverse array of wild Pokémon using various types of Poké Balls. Each catch brings you closer to completing your Pokédex!
-   **Dynamic Battles ⚔️:** Engage in strategic, turn-based combat against wild Pokémon and challenging Gym Leaders. Master type advantages and move sets to emerge victorious!
-   **Pokémon Evolution 🌱:** Witness your beloved Pokémon evolve into more powerful forms as they grow in strength and reach specific levels, unlocking new potential.
-   **Robust Leveling System 📈:** Gain experience points from battles, level up your Pokémon, and unlock a wider range of devastating moves to hone your team's skills.
-   **Intuitive Item Management 🎒:** Utilize Potions to restore your Pokémon's health during intense battles and manage your inventory of essential items, including different Poké Ball types.
-   **Challenging Gym Battles 🏆:** Conquer all 8 regional Gym Leaders, each specializing in a unique Pokémon type, to earn prestigious badges and prove your mettle as a trainer.
-   **Persistent Data Storage 💾:** All your hard-earned progress – player data, captured Pokémon, collected items, and earned badges – is securely saved to a MySQL database, allowing you to pick up right where you left off.
-   **Admin Mode 👑:** (For `admin` user only) Access special administrative features for testing, debugging, and managing game elements, suchs as adding Pokémon, resetting game data, or granting items.

---

## 🚀 Getting Started

To dive into the world of Pokémon CLI RPG, you'll need a Python 3 environment and a running MySQL server.

### Prerequisites ✅

-   **Python 3.x:** Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).
-   **MySQL Server:** Install MySQL Community Server. You can find installation instructions and downloads on [mysql.com](https://dev.mysql.com/downloads/mysql/). Make sure to set a `root` password during installation and remember it.
-   **`mysql-connector-python`:** This is the Python library needed to connect to your MySQL database. Install it using pip:
    ```bash
    pip install mysql-connector-python
    ```

### Installation Steps 🛠️

1.  **Clone the repository:**
    Start by cloning the game's repository to your local machine:
    ```bash
    git clone [https://github.com/Shubhae/PokeSQL.git](https://github.com/Shubhae/PokeSQL.git)
    cd PokeSQL
    ```

2.  **Configure the Database Connection:**
    Open the main game file, `PokéSQL.py`, in your preferred code editor. Locate the `dbconfig` dictionary and update the `password` field with your MySQL `root` password.
    ```python
    dbconfig = {
        'user': 'root',                # Your MySQL username (usually 'root')
        'password': 'YourMySQLRootPassword', # <--- **IMPORTANT: Replace with your actual MySQL root password**
        'host': 'localhost'
    }
    ```

3.  **Run the Game! ▶️**
    Navigate to the project directory in your terminal and execute the Python script:
    ```bash
    python PokéSQL.py
    ```
    The game will automatically create the `pokemon_game` database and set up all necessary tables on its first launch. You're now ready to begin your adventure!

---

## 🎮 Gameplay

When you launch the game, you'll be prompted to enter your trainer name. If you're a new trainer, you'll embark on your journey by choosing a loyal starter Pokémon!

### Main Menu Options 📜

1.  **🗡️ Battle wild Pokemon:** Roam the wilderness and encounter various wild Pokémon. Defeat them to gain experience or try to catch them to expand your team!
2.  **🏆 Challenge Gym Leader:** Face off against the region's powerful Gym Leaders. Each victory earns you a badge, bringing you closer to the Pokémon League!
3.  **👥 View Team:** Inspect your current Pokémon roster. Check their stats, health, level, and learned moves. You can also strategically switch your active battle Pokémon here.
4.  **🎒 Use Items:** Access your inventory to manage and utilize your valuable items, such as Potions for healing or different types of Poké Balls for capturing.
5.  **💊 Visit Pokemon Center:** Restore all your Pokémon to full health and get them ready for the next challenge with the help of Nurse Joy!
6.  **💾 Save and Quit:** Securely save all your progress to the database and exit the game. Your adventure will be waiting for you!
7.  **👑 Admin Menu:** (Accessible only if you log in with the trainer name `admin`) This menu provides tools for testing, such as adding specific Pokémon, resetting the game database (use with caution!), setting badges, or granting yourself items.

### Battle Mechanics 💥

-   **Turn-Based Combat:** Battles unfold in turns, requiring strategic thinking.
-   **Move Selection:** Choose from your Pokémon's learned moves, each with unique power and type.
-   **Type Effectiveness:** A core element of Pokémon battles! Understand and exploit type matchups (e.g., a Water-type move deals increased damage to a Fire-type Pokémon, but reduced damage to a Grass-type).
-   **Fainting & Switching:** If your active Pokémon's health drops to zero, it faints. You'll then have the option to switch to another healthy Pokémon in your team. If all your Pokémon faint, your adventure leads you back to the nearest Pokémon Center for healing.

---

## ⚡ Technologies Used

This project leverages the following technologies to bring the Pokémon CLI RPG to life:

-   **Python 🐍:** The primary programming language used for the game logic, user interface, and database interactions.
-   **MySQL 🐬:** A robust open-source relational database management system used to persistently store all game data, including player progress, Pokémon statistics, and inventory.
-   **`mysql-connector-python`:** The official MySQL driver for Python, enabling seamless communication between the Python application and the MySQL database.

---

## 🗃️ Database Schema

The game organizes its data within a MySQL database named `pokemon_game`, structured with three primary tables: `players`, `pokemons`, and `player_pokemons`.

### `players` table 👤

Stores comprehensive information about each trainer (player).

| Column            | Type        | Description                                       |
| :---------------- | :---------- | :------------------------------------------------ |
| `id`              | `INT`       | Primary Key, Auto-incremented unique player ID.   |
| `name`            | `VARCHAR(50)` | Unique name of the player/trainer.                |
| `poke_balls`      | `INT`       | Quantity of standard Poké Balls.                  |
| `great_balls`     | `INT`       | Quantity of Great Balls.                          |
| `ultra_balls`     | `INT`       | Quantity of Ultra Balls.                          |
| `master_balls`    | `INT`       | Quantity of rare Master Balls.                    |
| `potions`         | `INT`       | Quantity of basic Potions.                        |
| `super_potions`   | `INT`       | Quantity of Super Potions.                        |
| `hyper_potions`   | `INT`       | Quantity of Hyper Potions.                        |
| `max_potions`     | `INT`       | Quantity of Max Potions.                          |
| `badges`          | `INT`       | Total number of Gym Badges earned by the player.  |
| `current_pokemon` | `VARCHAR(50)` | Name of the Pokémon currently selected for battle. |

### `pokemons` table 🧬

Contains the base statistics and attributes for all available Pokémon species in the game. This table acts as a lookup for new Pokémon.

| Column           | Type        | Description                                       |
| :--------------- | :---------- | :------------------------------------------------ |
| `name`           | `VARCHAR(50)` | Primary Key, Unique name of the Pokémon species. |
| `type`           | `VARCHAR(20)` | The elemental type of the Pokémon (e.g., 'Grass', 'Fire', 'Water'). |
| `base_health`    | `INT`       | The base Health Points (HP) for this Pokémon species. |
| `base_attack`    | `INT`       | The base Attack stat for this Pokémon species.    |
| `base_defense`   | `INT`       | The base Defense stat for this Pokémon species.   |
| `base_speed`     | `INT`       | The base Speed stat for this Pokémon species.     |
| `evolve_level`   | `INT`       | The level at which this Pokémon typically evolves (or `NULL` if it doesn't evolve). |
| `evolve_to`      | `VARCHAR(50)` | The name of the Pokémon species it evolves into (or `NULL`). |
| `is_legendary`   | `BOOLEAN`   | `TRUE` if the Pokémon is a legendary species, `FALSE` otherwise. |

### `player_pokemons` table ⚡

Stores the unique instances of Pokémon owned by each player, including their individual progress and current state.

| Column            | Type        | Description                                       |
| :---------------- | :---------- | :------------------------------------------------ |
| `id`              | `INT`       | Primary Key, Auto-incremented unique ID for each player's Pokémon. |
| `player_id`       | `INT`       | Foreign Key, links to the `id` in the `players` table. |
| `name`            | `VARCHAR(50)` | The name of this specific Pokémon (e.g., 'Bulbasaur', 'Charizard'). |
| `level`           | `INT`       | The current level of this Pokémon.                |
| `experience`      | `INT`       | The current experience points accumulated by this Pokémon. |
| `health`          | `INT`       | The current Health Points of this Pokémon.        |
| `max_health`      | `INT`       | The maximum Health Points this Pokémon can have.  |
| `attack`          | `INT`       | The current Attack stat of this Pokémon.          |
| `defense`         | `INT`       | The current Defense stat of this Pokémon.         |
| `speed`           | `INT`       | The current Speed stat of this Pokémon.           |
| `type`            | `VARCHAR(20)` | The primary elemental type of this Pokémon.        |
| `moves`           | `VARCHAR(200)`| A comma-separated string of the moves this Pokémon has learned. |

---

## 📸 Screenshots (Coming Soon!)

Add some awesome screenshots of your game in action here to give users a visual preview!

<p align="center">
  <!-- Example: replace with actual screenshot image links -->
  <img src="https://placehold.co/400x250/E0F2F7/000000?text=Screenshot+1" alt="Gameplay Screenshot 1" style="margin: 10px;">
  <img src="https://placehold.co/400x250/E0F2F7/000000?text=Screenshot+2" alt="Gameplay Screenshot 2" style="margin: 10px;">
  <img src="https://placehold.co/400x250/E0F2F7/000000?text=Screenshot+3" alt="Gameplay Screenshot 3" style="margin: 10px;">
</p>

---

## 🚧 Future Enhancements

We're always looking to expand the world of Pokémon CLI RPG! Here are some ideas for future development:

-   **Pokémon Storage System 📦:** Implement a PC-like system to store Pokémon beyond the active team limit.
-   **Item Shop 🏪:** Allow players to buy and sell items using an in-game currency earned from battles.
-   **Multiplayer Battles 🧑‍🤝‍🧑:** Explore options for head-to-head battles against other players (requires more complex networking).
-   **Graphics/ASCII Art Improvements 🎨:** Enhance the visual fidelity of battles and menus with more intricate ASCII art representations of Pokémon and environments.
-   **More Regions & Pokémon Generations 🗺️:** Expand the game world with new areas, Gym Leaders, and Pokémon from different generations.
-   **Side Quests & Events 📜:** Introduce mini-quests, special events, and hidden challenges to provide more variety and depth.

---

## 🤝 Contributing

We welcome contributions from the community to make this game even better! If you have suggestions for improvements, new features, or find a bug, please feel free to:

1.  **Fork the repository:** Click the "Fork" button at the top right of this page on GitHub.
2.  **Create a new branch:**
    ```bash
    git checkout -b feature/your-awesome-feature-name
    ```
3.  **Make your changes:** Implement your new feature or bug fix.
4.  **Commit your changes:**
    ```bash
    git commit -m 'feat: Add a concise description of your changes'
    ```
5.  **Push to the branch:**
    ```bash
    git push origin feature/your-awesome-feature-name
    ```
6.  **Open a Pull Request:** Go to your forked repository on GitHub and click the "New Pull Request" button. Describe your changes clearly!

---

## 🐛 Reporting Issues

Encountered a bug? Have a suggestion? Please open an issue on the [GitHub Issues page](https://github.com/Shubhae/PokeSQL/issues). Please provide as much detail as possible, including steps to reproduce the issue.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.

---

## 🙏 Acknowledgements

A heartfelt thank you to:

-   **Nintendo, Game Freak, and The Pokémon Company:** For creating the incredible world of Pokémon that inspired this project.
-   **The open-source community:** For providing countless tools, libraries, and knowledge that make projects like this possible.

---

<p align="center">
  Made with ❤️ by a Pokémon Fan
  <br>
  <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/133.gif" width="50" alt="Eevee Animation">
</p>
w
