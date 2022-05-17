import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)
    self.contents = []
    for key in self.__dict__.keys():
      if key == 'contents':
        continue;
      self.contents.extend([key]*(self.__dict__[key])) 
    self.original_contents = copy.deepcopy(self.contents)

  def draw(self, numDraw):
    self.contents = copy.deepcopy(self.original_contents)
    if (numDraw > len(self.contents)):
      return self.contents
    chosen = []
    while numDraw > 0:
      draw = random.choice(self.contents)
      chosen.append(draw)
      self.contents.remove(draw)
      numDraw = numDraw - 1
    return chosen

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  total_experiments = num_experiments
  numPassed = 0
  for i in range(num_experiments):
    fail = False
    draw = hat.draw(num_balls_drawn)
    for key in expected_balls:
      if draw.count(key) < expected_balls[key]:
        fail = True
        break;
    if not fail: 
      numPassed += 1
  probability = numPassed / total_experiments
  return probability