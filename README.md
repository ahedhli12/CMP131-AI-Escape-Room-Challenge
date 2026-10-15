# CMP 131: AI Escape Room Challenge

## Mission

The classroom AI, **C.O.D.E.**, has accidentally locked everyone inside a virtual research lab. It is not evil. It simply installed an update without reading the directions.

Your team must complete three coding challenges before C.O.D.E. begins assigning homework forever.

## Learning Objectives

By completing this project, you will practice:

- Variables and user input
- Converting input to integers
- `if`, `elif`, and `else`
- Comparison and logical operators
- `while` loops
- Counters and limited attempts
- Testing different program paths
- Using GitHub Copilot as a tutor

## Team Roles

Choose a role for each team member. Rotate roles after each level.

- **Driver:** Types the code.
- **Navigator:** Reads the directions and reviews the logic.
- **Tester:** Tests correct, incorrect, and boundary values.
- **AI Prompt Manager:** Asks GitHub Copilot for explanations and small hints.

If your team has fewer than four members, one person may hold two roles.

## Challenge Rules

1. Open `escape_room.py`.
2. Complete every section marked `TODO`.
3. Use only concepts covered in class through `while` loops.
4. Do not use functions, lists, dictionaries, or imported libraries.
5. Test each level before moving to the next one.
6. Record your tests in `TEST-LOG.md`.
7. Complete `AI-Use-Report.md`.
8. Every team member must be able to explain the program.

## The Three Levels

### Level 1: Access Code

The player has three attempts to enter the correct access code.

Your program must:

- Use a `while` loop.
- Count the number of attempts.
- Display how many attempts remain.
- Unlock Level 2 when the code is correct.
- End the game after three incorrect attempts.

### Level 2: Cooling System

Ask the player to enter the AI system temperature.

- A temperature of `100` or higher means the system is overheating.
- A temperature below `50` means the system is too cold.
- A temperature from `50` through `99` is safe.
- The player must continue entering a temperature until it is safe.

Use a `while` loop and conditional statements.

### Level 3: Security Decision

Ask the player to choose one action:

- `scan`
- `shutdown`
- `share`

The program should accept only a valid choice. Use a `while` loop to repeat the question when the player enters something else.

Create your own results for the three choices. The message for `share` must remind the player not to share passwords or private information with AI.

## Final Escape Message

When the player completes all three levels, display:

- The player’s name
- A success message
- The number of access-code attempts used
- One friendly or funny message written by your team

## Required Testing

Test at least these scenarios:

1. Correct access code on the first attempt
2. Correct access code on the third attempt
3. Three incorrect access-code attempts
4. Temperature exactly `100`
5. Temperature exactly `50`
6. Invalid security choice followed by a valid choice

## Helpful GitHub Copilot Prompts

You may ask Copilot questions such as:

- “Explain how a counter works in a while loop.”
- “Give me one hint about why my loop does not stop.”
- “Help me trace this code using the value 100.”
- “Suggest test values without writing the solution.”
- “Explain this error message in simple language.”
- “Suggest a short funny message for an overheating AI.”

Do not ask Copilot to complete the entire project.

## Submission Checklist

- [ ] All three levels work.
- [ ] The program uses at least three `while` loops.
- [ ] The program handles invalid input choices.
- [ ] The program includes friendly, readable messages.
- [ ] `TEST-LOG.md` is complete.
- [ ] `AI-Use-Report.md` is complete.
- [ ] Every team member understands the code.
- [ ] The latest work is committed and pushed to GitHub.

## Git Commands

```bash
git status
git add .
git commit -m "Complete AI escape room challenge"
git push
```
