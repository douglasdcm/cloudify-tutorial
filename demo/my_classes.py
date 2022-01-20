class Dog:
  def __init__(self):
    self._name = None

  def bark(self, voice):
    print(voice)

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, val):
    self._name = val


class DogOwner:
  def __init__(self):
    self._name = None
    self._dogs = []

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, val):
    self._name = val

  def call_dog(self, dog_name):
    print(dog_name.upper)

  def adopt(self, dog_name):
      self.dogs.append(dog_name)





