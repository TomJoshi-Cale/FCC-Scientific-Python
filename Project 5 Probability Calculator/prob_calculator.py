from copy import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color in kwargs:
      for i in range(kwargs[color]):
        self.contents.append(color)
        i += 1
    self.init_cont = copy(self.contents)
  
  def draw(self, num):
    results = []
    if (num > len(self.contents)):
      num = len(self.contents)
    for i in range(num):
      num = random.randint(0, len(self.contents)-1)
      results.append(self.contents.pop(num))
      i += 1
    return(results)

  def restock(self):
    self.contents = copy(self.init_cont)
  


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  target = []
  successes = 0
  for ball in expected_balls:
    for i in range(expected_balls[ball]):
      target.append(ball)
      i += 1
  target = sorted(target)
  while i <= num_experiments:
    matches = 0
    drawn = (hat.draw(num_balls_drawn))
    drawn = sorted(drawn)
    for x in target:
      try:
        j = drawn.index(x)
        drawn.pop(j)
        matches += 1
      except ValueError:
        hat.restock()
        break
    if(matches == len(target)):
      successes += 1
    hat.restock()
    i += 1
  probability = successes / num_experiments
  return(probability)
