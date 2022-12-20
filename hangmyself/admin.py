import ast

with open('hangman_art.txt') as f:
    hangman_art = ast.literal_eval(f.read())

# Now you can use the hangman_art list in your game just like in the previous example
stage = 0
print(hangman_art[stage])
