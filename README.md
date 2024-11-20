# Number Guessing Game with Streamlit

## Overview
This is a simple **Number Guessing Game** built using **Streamlit**, where the user tries to guess a randomly generated number between 1 and 100. The game provides feedback on whether the guess is too high, too low, or correct. The user can restart the game after successfully guessing the number.

## Features
- **Random Number Generation**: A number between 1 and 100 is randomly chosen by the computer.
- **User Interaction**: The user guesses the number by inputting a value, and feedback is given for each guess.
- **Session Persistence**: The game state (number and attempts) is stored using **Streamlit’s session state** to ensure continuity of gameplay.
- **Feedback Messages**: Color-coded feedback for "too low", "too high", and correct guesses.
- **Play Again Option**: After successfully guessing the number, the user can restart the game.

## Technologies Used
- **Streamlit**: For building the interactive web app.
- **Python**: The programming language for the backend logic.

## Installation

### Prerequisites
Make sure you have **Python** installed on your system. You can check if Python is installed by running the following command:

```bash
python --version
