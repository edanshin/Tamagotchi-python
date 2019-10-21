# Tamagotchi ASCII art.
SMALL = r'''

 _____
/ ^_^ \
\_____/
'''[1:-1]
MED = r'''
   _______
  /       \
 /  ^ _ ^  \
 \_________/
    U   U
'''[1:-1]
BIG = r'''
   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
'''[1:-1]


class Tamagotchi:
  """
  Represents a single Tamagotchi pet.
  """
  def __init__(self, name):
    """
    Given a name, initialises a Tamagotchi as though born with basic stats.
    """
    self._name = name
    self._is_dead = False
    self._age = 0
    self._hunger = 5
    self._boredom = 0

  def is_dead(self):
    """
    Returns True if the Tamagotchi is dead, False otherwise.
    """
    return self._is_dead

  def feed(self):
    """
    Decreases the Tamagotchi's hunger level.
    """
    if self.is_dead():
      return

    self._hunger -= 3

    # Check for overfeeding.
    if self._hunger < 0:
      self._hunger = 0
      self._is_dead = True
      
  def play(self):
    """
    Decreases the Tamagotchi's boredom level.
    """
    if self.is_dead():
      return

    self._boredom -= 5
    if self._boredom < 0:
      self._boredom = 0
  
  def increment_time(self):
    """
    Adjusts stats as though time has passed for this tamagotchi.
    """
    if self.is_dead():
      return

    self._hunger += 1
    self._age += 1
    self._boredom += 1
    if self._age > 15:
      self._is_dead = True
    if self._hunger > 10:
      self._is_dead = True
    if self._boredom > 10:
      self._is_dead = True
  
  def __str__(self):
    """
    Returns a string representing the current status of the tamagotchi.
    """
    if self.is_dead():
      return '''
Name:    {}
DEAD
'''.format(self._name)

    if self._age < 3:
      picture = SMALL
    elif self._age < 6:
      picture = MED
    else:
      picture = BIG
    return '''{}
Name:    {}
Hunger:  {}
Boredom: {}
Age:     {}
'''.format(picture, self._name, self._hunger*'o', self._boredom*'o', self._age)
