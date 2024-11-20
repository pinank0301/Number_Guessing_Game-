import streamlit as st
import random
import time

# Function to generate a random number and run the guessing game
def number_guessing_game():
    # Set page config and title for a cool header
    st.set_page_config(page_title="Guess the Number!", layout="centered")

    # Custom background color and fonts using markdown
    st.markdown(
        """
        <style>
        .title {
            font-size: 40px;
            color: #FF6347;
            font-family: 'Comic Sans MS';
        }
        .header {
            font-size: 25px;
            color: #20B2AA;
        }
        .success {
            font-size: 25px;
            color: #32CD32;
            font-weight: bold;
        }
        .failure {
            font-size: 25px;
            color: #DC143C;
            font-weight: bold;
        }
        .game-over {
            font-size: 30px;
            color: #FFD700;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)

    # Title and introduction
    st.markdown('<div class="title">🎉 Number Guessing Game 🎉</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">Guess the number between 1 and 100!</div>', unsafe_allow_html=True)

    # Set session state to store random number and attempts
    if 'number' not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0

    # Get user input for the guess (ensure a valid number is entered)
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess")

    if guess:
        st.session_state.attempts += 1

        # Display feedback based on the guess
        if guess < st.session_state.number:
            st.markdown('<div class="failure">Too low! Try again.</div>', unsafe_allow_html=True)
        elif guess > st.session_state.number:
            st.markdown('<div class="failure">Too high! Try again.</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="success">Congratulations! You guessed the number in {st.session_state.attempts} attempts.</div>', unsafe_allow_html=True)
            st.markdown('<div class="game-over">Game Over! 🎉</div>', unsafe_allow_html=True)
            
            # Adding a delay before restarting the game
            with st.spinner('Starting a new game...'):
                time.sleep(2)
                
            # Button to play again
            if st.button('Play Again'):
                st.session_state.number = random.randint(1, 100)
                st.session_state.attempts = 0



# Run the game
number_guessing_game()
