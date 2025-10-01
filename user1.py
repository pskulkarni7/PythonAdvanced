class User:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print(f"Welcome - {self.name}")

class FrenchUser(User):
  '''
  DIsplays a greeting in French
  '''
  def __init__(self, name):
    super().__init__(name)

  def greet(self):
    print(f"“Bonjour” - {self.name}")   

class SpanishUser(User):
    '''
    Displays a greeting in Spanish
    '''
    def __init__(self, name):
        super().__init__(name)

    def greet(self):
        print(f"Hola! - {self.name}")

