class Citizen(object):
  
  def __init__(self, name, country):
    self.name = name
    self.country = country
    
class Winner(Citizen):

  def __init__(self, name, country, category, year):
      super(Winner, self).__init__(name, country)
      self.category = category
      self.year = year
  def print_details(self):
      print('Winner %s from %s, category %s, year %s' %(self.name, self.country, self.category, str(self.year)))
      
w = Winner('Albert E.', 'Switzerland', 'Physics', 1921)
w.print_details()
