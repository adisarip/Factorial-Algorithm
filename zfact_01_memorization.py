from collections.abc import Callable


class Factorial(Callable):
  """ A Callable class to calculate Factorial"""
  def __init__(self):
    self.previous = {} #for memorization

  def __call__(self, n):
    """ This methods make the class callable """
    if n not in self.previous:
      self.previous[n] = self.compute(n)

    return self.previous[n]

  def compute(self, n):
    if n == 0 : return 1
    return n*self.__call__(n-1)

print (Factorial()(200))
