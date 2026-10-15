# ================================================================
# CMP 131 - AI ESCAPE ROOM CHALLENGE
# ================================================================
# Team members:
# Date:
#
# Complete every section marked TODO.
# Use only variables, input, print, if/elif/else, and while loops.
# ================================================================


# ------------------------- INTRODUCTION --------------------------

# Ask the player for a name so the game can personalize its messages.
player_name = input("Enter your name, brave programmer: ")

# Introduce the story and explain the player's mission.
print("\nWelcome,", player_name + "!")
print("C.O.D.E., the classroom AI, has locked the virtual lab.")
print("Complete three challenges before it assigns homework forever!")


# ------------------- LEVEL 1: ACCESS CODE ------------------------

print("\nLEVEL 1: ACCESS CODE")
print("You have three attempts to unlock the laboratory door.")

# Store the correct code. Do not ask GitHub Copilot to reveal it.
correct_code = 131

# TODO 1: Create a variable that counts how many attempts were used.

# TODO 2: Create a Boolean variable that remembers whether the door is unlocked.

# TODO 3: Write a while loop that allows no more than three attempts.
# Inside the loop:
#   - Ask the player to enter an integer access code.
#   - Increase the attempt counter.
#   - Use if/else to check the code.
#   - Display the number of attempts remaining after an incorrect code.

# TODO 4: After the loop, determine whether the player may continue.
# If the door was not unlocked, display a game-over message.
# The other levels should run only when the door is unlocked.


# ---------------- LEVEL 2: COOLING SYSTEM ------------------------

# TODO 5: Place Level 2 inside the correct condition from Level 1.

# Display the Level 2 title and directions.

# TODO 6: Ask for the system temperature.

# TODO 7: Use a while loop that continues while the temperature is unsafe.
#   - 100 or higher: overheating
#   - Below 50: too cold
#   - 50 through 99: safe
# Ask for a new temperature when it is unsafe.

# TODO 8: Display a message when the system reaches a safe temperature.


# --------------- LEVEL 3: SECURITY DECISION ---------------------

# TODO 9: Display the Level 3 title and the three choices:
# scan, shutdown, or share

# TODO 10: Ask the player for a choice and convert it to lowercase.

# TODO 11: Use a while loop to reject invalid choices.
# Continue asking until the player enters scan, shutdown, or share.

# TODO 12: Use if/elif/else to display a different result for each choice.
# The share message must remind the player not to share passwords or
# private information with AI.


# ----------------------- FINAL ESCAPE ----------------------------

# TODO 13: Display the player's name, a success message, and the number
# of access-code attempts used.

# TODO 14: Add one friendly or funny final message written by your team.
