# `ROCK PAPER SCISSOR`
---
## Step 1
- Create a simple, one-round version of the game where we don’t enforce correct inputs.
- Use random.randint() to generate a random number, and use conditionals to let each random number choose a different option for the computer (e.g. 0 mean rock, 1 means paper, 2 means scissors).
- Use input() to get the user’s choice.
Use conditionals to see who wins.
>Hint: Break it down into cases! If the user chooses rock, then there are possibilities depending on what the computer picked. You can use and, or nested conditionals!
---
## Step 2
- Add while loops to re-prompt the use to enter their choice if they type something invalid.
- Use .lower() on the user’s input to make sure our stored value is always lowercase.
Write code so that while the user’s input is not one of the valid choices, it keeps prompting them to re-enter their choice.
---
## Step 3
- Use a while loop to let the user play over and over, and use variables to keep track of the scores.
- Use while True to create a loop that runs forever.
- After the end of the round, ask the user if they want to keep playing; if they say no, use break to end the loop.
- Use the same strategy from step 2 (.lower() and a while loop) to enforce a valid input for this choice too!
- Before the while True loop, create variables to keep track of the scores, and increment those variables in the right places.