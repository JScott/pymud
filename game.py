#!/usr/local/bin/python3
import pickle

print('Welcome to the world of Pythonius!')

def save_game:
  with open('save.pickle', 'wb') as save_file:
    pickle.dump(player, save_file)

class Player:
  # For storing player data
  professions = ['Fighter', 'Bard', 'Wizard']
  def ask_name(self):
    self.name = input('What is thine name? ')
  def ask_profession(self):
    print('Professions')
    for profession in self.professions:
      print (' ', profession)
    self.profession = None
    while self.profession not in self.professions:
      self.profession = input('What is thine profession? ')
  def __init__(self):
    self.ask_name()
    self.ask_profession()

player = Player()

print('Welcome, oh great', player.name, 'the', player.profession)
save_game()
