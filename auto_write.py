#install pyautogui by running the following command
#pip install pyautogui
#Open the program or website where you want the text to be typed automatically (for example, a chat application or a text editor).
#Make sure the text input field (where the typing should happen) is active and ready for text input.
#Note: You have 5 seconds after you run the script to focus the text input field, as indicated in the script.

import random
import pyautogui as pg
import time

# Give the user some time to focus the text input area
print("You have 5 seconds to focus on the text input area!")
time.sleep(5)

# List of random messages
messages = [
    "I LOVE YOU",
    "You are amazing!",
    "You're the best!",
    "Can't stop thinking about you!",
    "You make my heart smile ♥",
    "You're my sunshine!",
    "I appreciate you so much!"
]

# Typing with random delays and sending without manual Enter press
for i in range(10):
    message = random.choice(messages)  # Choose a random message from the list
    pg.write(message)
    # Automatically press 'Enter' after each message is typed
    pg.press('enter')  # Sends the message by simulating the Enter key press
    # Random delay before typing the next message
    time.sleep(random.uniform(0.5, 1.5))  # Wait a random amount of time before typing the next message
