# A list of houses as, for example, provided by MLS

import csv

class House:
  
  def __init__(self, MLS_entry):
    '''(House, list) -> None
    Create a House object representing all the data in the MLS_entry
    '''
    self.number = MLS_entry[0]
    self.street = MLS_entry[1]
    self.type = MLS_entry[2]
    self.size = MLS_entry[3]
    self.floors = MLS_entry[4]
    self.bedrooms = MLS_entry[5]
    self.bathrooms = MLS_entry[6]
    self.lot = MLS_entry[7]
    self.parking = MLS_entry[8]
    self.facing = MLS_entry[9]
    self.age = MLS_entry[10]
    self.taxes = MLS_entry[11]
    self.price = MLS_entry[12]

  def __str__(self):
    '''(House) -> str
    Returns string showing house address, size and price
    '''
    return 'Address: ' + str(self.number) + ' ' + str(house.street) + \
           ' Size: ' + str(house.size) + ' Price: $' + str(house.price)
  
  
def get_MLS_data(filename):
  '''
  (str)->list of lists of string
  Opens <filename> as a CSV file, reads in each row and returns the list of rows
  '''
  
  # read in the database
  MLS_data = [] 
  with open(filename, 'r') as csvfile:
    real_estate_reader = csv.reader(csvfile)
    
    for row in real_estate_reader:
      MLS_data.append(row)
      
  return MLS_data
    
def MLS_to_Houses(MLS_list):
  """ (list of lists) -> (list of House)
  create new list where each entry is a House object.
  """  
  
  house_list = []

  # for each house, create an entry (of what type?) in house_list
  # need code here
  for house in MLS_list:
        
    # create a Houuse object and add it to the list
    house_list.append(House(house))

  return house_list

def create_street_searchable_houses(house_list):
  """ (list of House) -> (dictionary of list of House)
  create new dictionary indexed by street name where each entry is a 
  list Houses on that street.
  """  
  
  # create a new dictionary with street as key and a list of houses
  # as the value 
  street_dict = {}
  
  # search through all dictionary items and organize by key field
  for house in house_list:
    if house.street not in street_dict:
      # A new street that we haven't yet used as a key - create the entry 
      street_dict[house.street] = [house]
    else:
      # If the street already exists, append the new house onto the 
      # corresponding list
      street_dict[house.street].append(house)
        
  return street_dict


# Convert MLS list to a list of houses 
MLS_data = get_MLS_data("real_estate.csv")
house_list = MLS_to_Houses(MLS_data[1:])

# Convert list of houses into dictionary indexed by street
houses_by_street = create_street_searchable_houses(house_list)

# Prompt user for list of streets and store them in  a list
street_list = []
done = False
while(not done):
  street = input('Enter a street name (type exit when done): ')
  if street !=  'exit':
    street_list.append(street)
  else:
    done = True

# print out the info for each house in the streets indicated by the user
for street in street_list:
  print("\nHouses on", street)
  if street in houses_by_street.keys():
    for house in houses_by_street[street]:
      print(house)
  else:
    print('No houses on', street)
