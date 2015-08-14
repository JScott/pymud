#!/usr/local/bin/python3
import pickle
import player_test

print('Welcome to the world of Pythonius!')

def save_game():
  with open('save.pickle', 'wb') as save_file:
    pickle.dump(player, save_file)

player = Player()

print('Welcome, oh great', player.name, 'the', player.profession)
save_game()
