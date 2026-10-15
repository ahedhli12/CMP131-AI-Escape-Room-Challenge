# ================================================================
# CMP 131 - AI ESCAPE ROOM CHALLENGE
# ================================================================
# Team members:
# Date:
#
# Complete every section marked TODO.
# Starter variables and loop structures are provided for you.
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
print("Keep trying until you enter the correct access code.")

# Store the correct code and starting values.
correct_code = 131
door_status = "locked"
attempts = 0

# The loop repeats while the door is locked.
while door_status == "locked":
    # TODO 1: Ask the player for an integer access code.

    # Count this attempt.
    attempts = attempts + 1

    # TODO 2: Use if/else to check the code.
    # Correct code: change door_status to "unlocked" and print success.
    # Incorrect code: print a friendly message asking the player to try again.


# Display how many attempts the player used.
print("Access-code attempts used:", attempts)


# ---------------- LEVEL 2: COOLING SYSTEM ------------------------

print("\nLEVEL 2: COOLING SYSTEM")
print("A safe temperature is from 50 through 99.")

# Ask for the first temperature.
temperature = int(input("Enter the system temperature: "))

# Repeat while the temperature is too cold or overheating.
while temperature < 50 or temperature >= 100:
    # TODO 3: Use if/else to print "Too cold" or "Overheating".

    # Ask for another temperature so the loop can check again.
    temperature = int(input("Enter a new temperature: "))

# TODO 4: Print a message confirming that the temperature is safe.


# --------------- LEVEL 3: SECURITY DECISION ---------------------

print("\nLEVEL 3: SECURITY DECISION")
print("Choose: scan, shutdown, or share")

# Ask for the first choice and convert it to lowercase.
choice = input("Enter your choice: ").lower()

# Repeat when the player does not enter one of the three choices.
while choice != "scan" and choice != "shutdown" and choice != "share":
    # TODO 5: Print an invalid-choice message.

    # Ask again so the loop can check a new choice.
    choice = input("Enter scan, shutdown, or share: ").lower()

# TODO 6: Use if/elif/else to display a result for each valid choice.
# The share message must remind the player not to share passwords or
# private information with AI.


# ----------------------- FINAL ESCAPE ----------------------------

# Display the player's name and a success message.
print("\nCongratulations,", player_name + "!")
print("You escaped from C.O.D.E.'s virtual laboratory!")

# TODO 7: Add one friendly or funny final message written by your team.
