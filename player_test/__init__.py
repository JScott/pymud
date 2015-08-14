class Player:
  # For storing player data
  professions = ['Fighter', 'Bard', 'Wizard']
  def ask_name(self):
    self.name = input('What is thine name? ')
  def print_professions(self):
    print('Professions')
    for profession in self.professions:
      print (' ', profession)
  def ask_profession(self):
    self.print_professions()
    self.profession = None
    while self.profession not in self.professions:
      self.profession = input('What is thine profession? ')
  def __init__(self):
    self.ask_name()
    self.ask_profession()
