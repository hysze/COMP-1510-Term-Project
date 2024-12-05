# COMP-1510-Term-Project

Every program needs a README.md

This is written in markdown. Read about markdown here: [markdowncheatsheet](https://www.markdownguide.org/cheat-sheet/)

## Your name:
Hei Yeung Sze

## Your student number:
A01365835

## Your GitHub name:
hysze

## Any important comments you'd like to make about your work:
This game is called "One Way Out". If possible, please play the game first before you review the 
codes. 

And my apology. I underestimated the time required for this term project, and perhaps do not have 
enough time to update the flowchart.

## Inclusion of manadatory elements
| appropriate? | appropriate use of ...                  | module    | line no. | comments                                                                                                                                                                                                                    |
|--------------|-----------------------------------------|-----------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              | immutable data structures               | map       | 23   | immutable tuples to store coordinates (row and column) representing fixed location                                                                                                                                          |
|              | mutable data structures                 | character | 22 - 32 | mutable dictionary to store character stats where character stats will be varying during the game                                                                                                                           |
|              | exceptions and exception handling       | combat    | 88 - 93 | convert user input to integer; raise a ValueError exceptional case when user input is not an integer to prevent the game from crashing                                                                                      |
|              | minimised scope                         | combat    | 59   | create a copy of the enemy's stats; its scope is limited to the function itself and also its helper function and will be destroyed right after                                                                              |
|              | atomic, independent, reusable functions | goal      | 14 - 17 | further modularize part of the program into a smaller helper function to verify if the goal has been attained instead of hardcoding the value inside the main function                                                      |
|              | flat code                               | goal      | 14 - 17 | simple if-else statement without nesting                                                                                                                                                                                    |
|              | list / dictionary comprehensions        | combat    | 85 - 103 | utilize the mutability of a dictionary; the battle_with_foe function directly updates the character status inside the character dictionary and doesn't not need to return the dictionary due to the dictionary's mutability |
|              | selection using if-statements           | goal      | 14 - 17 | simple if-else statement to check if the player attains the goal                                                                                                                                                            |
|              | repetition with for/while-loop          | game      | 17   | use while loop to repeat several operations until either the character dies or the player attains the goal                                                                                                                  |
|              | membership operator                     | move      | 12 - 13 | use membership operator to verify if user input is in a list of valid inputs                                                                                                                                                |
|              | range function                          | map       | 21 - 22 | utilize range functions to efficiently produce a map                                                                                                                                                                        |
|              | a function from itertools               |           |      |                                                                                                                                                                                                                             |
|              | random module                           | combat    | 86   | generate a random number for a number-guessing game                                                                                                                                                                         |
|              | function annotations                    | goal      | 1    | annotate types of the function's argument and also the return value                                                                                                                                                         |
|              | doctest/unit tests (see pdf)            | --        | --   |                                                                                                                                                                                                                             |
|              | f-strings, format(), or old formatting  | combat    | 93   | use f-strings to print the statement, including a variable that is the character's current HP                                                                                                                               |