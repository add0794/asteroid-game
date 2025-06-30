# Asteroid Game

A classic arcade-style Asteroids game built with Python and Pygame.

## Features

- Player-controlled spaceship that can rotate, thrust, and shoot
- Asteroids of varying sizes that split into smaller pieces when shot
- Bullets with cooldown and velocity based on ship direction
- Collision detection between player, asteroids, and bullets
- Game over detection when the player collides with an asteroid

## Requirements

- Python 3.8+
- [Pygame](https://www.pygame.org/)  
- (Optional) Other dependencies as listed in `requirements.txt` or your environment

## How to Run

1. Install dependencies:
    ```bash
    pip install pygame
    ```

2. Run the game:
    ```bash
    python main.py
    ```

## Controls

- **W**: Thrust forward
- **S**: Thrust backward
- **A**: Rotate left
- **D**: Rotate right
- **Space**: Shoot
- **Esc / Close window**: Quit

## Project Structure
```
.
├── main.py              # The main game file and loop
├── player.py           # Player ship class and logic
├── asteroid.py         # Asteroid class and logic
├── asteroidfield.py    # Asteroid field management
├── shot.py            # Bullet/shot class and logic
├── circleshape.py      # Base class for circular game objects
├── constants.py        # Game constants and configuration
├── requirements.txt    # Project dependencies
├── README.md          # This README file
├── .gitignore         # Git ignore file
└── venv/              # Python virtual environment
```

## Customization

- Edit `constants.py` to modify game settings like screen size, colors, and speeds.
- Customize game mechanics in:
  - `player.py` for ship behavior and controls
  - `asteroid.py` for asteroid properties and movement
  - `shot.py` for bullet behavior and physics
  - `asteroidfield.py` for asteroid spawning and management
- Adjust the circular physics behavior in `circleshape.py`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.