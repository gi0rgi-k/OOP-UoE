""""Encapsulation Lab 2"""

import csv

# **********************************************
# code for the coffee object
# **********************************************

class CoffeeJournal:
  def __init__(self, file):
    self._file = file
    self._roaster = ""
    self._country = ""
    self._region = ""
    self._stars = ""
    self._old_coffee = self.load_coffee()
    self._new_coffee = []
    
  def load_coffee(self):
    coffee = []
    with open(self._file) as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        coffee.append(row)
    return coffee

  @property
  def roaster(self):
    return self._roaster
  
  @roaster.setter
  def roaster(self, new_roaster):
    self._roaster = new_roaster

  @property
  def country(self):
    return self._country
  
  @country.setter
  def country(self, new_country):
    self._country = new_country
    
  @property
  def region(self):
    return self._region
  
  @region.setter
  def region(self, new_region):
    self._region = new_region
    
  @property
  def stars(self):
    return self._stars
  
  @stars.setter
  def stars(self, new_stars):
    self._stars = new_stars


# **********************************************
# code for testing your script
# **********************************************

test_object = CoffeeJournal("code/encapsulation/test_journal2.csv")
test_object.roaster = "Peace River"
test_object.country = "Rawanda"
test_object.region = "Remera"
test_object.stars = "***"
print(test_object.roaster)
print(test_object.country)
print(test_object.region)
print(test_object.stars)
