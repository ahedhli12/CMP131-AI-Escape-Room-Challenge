# ================================================================
# CMP 131 - AI ESCAPE ROOM CHALLENGE
# ================================================================
# Team members:
# Date:
#
# STORY:
# C.O.D.E., the classroom AI, accidentally locked the virtual lab.
# Complete the three levels to help the player escape.
#
# DIRECTIONS:
# Write your Python code below each numbered TODO.
# Use only concepts covered in class:
# print, input, variables, int, if/elif/else, and while loops.
# ================================================================


# ------------------------- INTRODUCTION --------------------------

# TODO 1:
# Ask the player to enter a name and save it in a variable.
# Display a welcome message that includes the player's name.
# Explain that the player must complete three levels to escape.


# ------------------- LEVEL 1: ACCESS CODE ------------------------

# TODO 2:
# Display the title "LEVEL 1: ACCESS CODE".
# Explain that the player must enter the correct code to unlock the door.
# The correct access code is 131.

# TODO 3:
# Create a variable that stores the word "locked".
# Create another variable that starts the attempt count at 0.

# TODO 4:
# Create a while loop that repeats while the door is "locked".
# Inside the loop:
#   1. Ask the player to enter an access code.
#   2. Convert the player's answer to an integer.
#   3. Add 1 to the attempt count.
#   4. Use if/else to check the answer.
#   5. If the code is 131, change the door status to "unlocked".
#   6. Otherwise, display a friendly message and allow another attempt.

# TODO 5:
# After the loop ends, display that the door is unlocked.
# Display the number of attempts the player used.


# ---------------- LEVEL 2: COOLING SYSTEM ------------------------

# TODO 6:
# Display the title "LEVEL 2: COOLING SYSTEM".
# Explain that a safe temperature is from 50 through 99.
# Ask the player to enter the system temperature as an integer.

# TODO 7:
# Create a while loop that repeats when the temperature is unsafe.
# A temperature is unsafe when it is below 50 OR 100 or higher.
# Inside the loop:
#   1. If the temperature is below 50, display "Too cold."
#   2. Otherwise, display "Overheating."
#   3. Ask the player to enter a new temperature.

# TODO 8:
# After the loop ends, display that the temperature is safe.


# --------------- LEVEL 3: SECURITY DECISION ---------------------

# TODO 9:
# Display the title "LEVEL 3: SECURITY DECISION".
# Tell the player to enter one of these choices:
# scan, shutdown, or share
# Ask for the player's choice and convert it to lowercase.

# TODO 10:
# Create a while loop that repeats when the choice is not valid.
# Inside the loop:
#   1. Display a friendly invalid-choice message.
#   2. Ask the player to enter scan, shutdown, or share again.

# TODO 11:
# After the loop ends, use if/elif/else to display a different
# message for scan, shutdown, and share.
# The share message must remind the player not to share passwords
# or private information with AI.


# ----------------------- FINAL ESCAPE ----------------------------

# TODO 12:
# Display the player's name and a congratulations message.
# Display that the player escaped from the virtual laboratory.
# Add one friendly or funny final message written by your team.
