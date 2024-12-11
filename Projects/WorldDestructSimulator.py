country__codes=['aus','sau','gbr','usa','uae']
print('Welcome to world destruction simulator.')
print('---------------')
def country_destruct():
  print('---------------')
  print('Welcome to Country destruct.')
  print('In this gamemode, you choose the country you want to destruct.')
  cd_choicefunc()
def cd_choicefunc():
  cd_choice_normal = input("Please input a 3 digit country code ('help' for the library of country codes, 'menu' for the menu) ")
  cd_choice = cd_choice_normal.lower
  if cd_choice == 'menu':
    menu()
  if cd_choice == 'help':
    print('---------------')
    print('Here are the available country codes:')
    print('AUS - Australia')
    print('SAU - Saudi Arabia')
    print('GBR - United Kingdom')
    print('USA - United States of America')
    print('UAE - United Arab Emirates')
    print('---------------')
    cd_choicefunc()
def menu():
  print('Select a gamemode:')
  print('1. Country destruction')
  print('2. World destruction')
  wds_choice = input(' ')
  if wds_choice == '1':
    country_destruct()
  elif wds_choice == '2':
    print('---------------')
    print('TO BE MADE')
  else:
    print('---------------')
    print('Please enter a valid option')
    print('---------------')
    menu()
    
    
menu()