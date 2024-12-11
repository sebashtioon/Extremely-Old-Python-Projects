#     01000111 01000001 01001101 01000101                                                                
#     01000010 01111001                                                                                  
#     01010011 01000101 01000010 01000001 01010011 01001000 01010100 01001001 01001111 01001111 01001110 

#     ____  ____  _     _________  _____    _     ____  ____  _    ____     #
#    /   _\/  _ \/ \ |\/  __/  __\/__ __\  / \  //  _ \/  __\/ \  /  _ \    #
#    |  /  | / \|| | //|  \ |  \/|  / \    | |  || / \||  \/|| |  | | \|    #
#    |  \__| \_/|| \// |  /_|    /  | |    | |/\|| \_/||    /| |_/\ |_/|    #
#    \____/\____/\__/  \____\_/\_\  \_/    \_/  \\____/\_/\_\\____|____/    #
                                                                   
# V 1.0.0


import time
import random

# VARIABLES AND LISTS FOR RANDOM
ancient_ruins_visited = False
choicesmm = ['1', '2', '3']

# > typewriter_effect(text) < #
def typewriter_effect(text):
    words = text.split()
    word_count = len(words)
    line_count = 0

    for i, word in enumerate(words):
        print(word, end=' ', flush=True)
        time.sleep(0.2)

        if (i + 1) % 20 == 0 and i < word_count - 1:
            line_count += 1
            print('\n', end='')  
# < END OF FUNCTION > #

# > forest_story() < #
def forest_story():
  print('Forest Biome')
  mainmenu()
  return
# < END OF FUNCTION > #

# > villiage_story() < #
def village_story():
  mainmenu()
  return
# < END OF FUNCTION > #

# > desert_story() < #
def desert_story():
  print('Desert Biome')
  mainmenu()
  return
# < END OF FUNCTION > #

# > ravine_story() < #
def ravine_story():
  ancient_ruins_visited = False
  choicesravine = ['1', '2', 'menu']
  if ancient_ruins_visited == True:
      ravinerandomps = ['river', 'monster', 'glowingmushrooms', 'endlessdarkness', 'waterfall', 'river', 'monster', 'glowingmushrooms', 'endlessdarkness', 'waterfall', 'river', 'monster', 'glowingmushrooms', 'endlessdarkness', 'waterfall', 'river', 'monster', 'glowingmushrooms', 'endlessdarkness', 'waterfall', 'river', 'monster', 'glowingmushrooms', 'endlessdarkness', 'waterfall', 'river', 'monster', 'glowingmushrooms', 'endlessdarkness', 'waterfall', 'timeportal']
  elif ancient_ruins_visited == False:
      ravinerandomps = ['river', 'monster', 'glowingmushrooms', 'endlessdarkness', 'waterfall', 'river', 'monster', 'glowingmushrooms', 'endlessdarkness', 'waterfall', 'river', 'monster', 'glowingmushrooms', 'endlessdarkness', 'waterfall', 'river', 'monster', 'glowingmushrooms', 'endlessdarkness', 'waterfall', 'river', 'monster', 'glowingmushrooms', 'endlessdarkness', 'ruins', 'waterfall', 'river', 'monster', 'glowingmushrooms', 'endlessdarkness', 'waterfall', 'timeportal']
  while True:
      ravine_story_biomes = ['            You come across a deep, dark ravine.', '            You come across a small ravine.', '            You come across a large ravine.']
      ravine_story_biomes_random = random.choice(ravine_story_biomes)
      print(ravine_story_biomes_random)
      print('            1. Go in')
      print('            2. Keep exploring')
      ravineinput = input('            Enter your choice ("menu" for Menu.): ')
      while True:
        if ravineinput == 'menu':
          mainmenu()
          break
        elif ravineinput == '2':
          story_mode()
          break
        elif ravineinput == '1':
          ravinerandompsv = random.choice(ravinerandomps)
          if ravinerandompsv == 'river':
            print('             ---------------')
            print(f"     There is a river in the ravine!\n     You can't walk past it or enter it.")
            print('             ---------------')
            story_mode()
            break
          elif ravinerandompsv == 'ruins':
            print(f'                ---------------')
            print(f'While exploring the ravine, you stumble upon a hidden\nentrance partially obscured by overgrown foliage.')
            while True:
              print('                ---------------')
              print('            1. Enter the ruins')
              print('            2. Leave the ravine')
              ruinsinput = input('            Enter your choice: ')
              if ruinsinput == '1':
                print(f'Intrigued, you enter the ancient ruins, revealing a vast labyrinthine\ncomplex of crumbling walls, grand chambers, and mysterious artifacts.')
                ancient_ruins_visited = True
                print('                ---------------')
                print('            Unlocked ancient ruins!')
                print('                ---------------')
                story_mode()
                break
              if ruinsinput == '2':
                story_mode()
          elif ravinerandompsv == 'glowingmushrooms':
            print('                ---------------')
            print(f'You see strange glowing mushrooms at the bottom of the ravine.')
            while True:
              print(f'                ---------------')
              print('            1. Discover the strange mushrooms')
              print('            2. Leave the ravine')
              glowingmushroomsinput = input('            Enter your choice: ')
              if glowingmushroomsinput == '1':
                print(f'                ---------------') 
                print("  You cautiously approach the strange mushrooms and examine them closely.")
                print('  They emit a soft, pulsating glow, casting an eerie light in the ravine.')
                print('  As you study them, you notice intricate patterns on their caps.')
                print('  You carefully collect a few samples of the glowing mushrooms, curious about their properties.')
                print('  With the mushrooms in your possession, you decide to return to conduct further research.')
                print(f'                ---------------')
                story_mode()
                break
              elif glowingmushroomsinput == '2':
                  print(f'                ---------------')
                  story_mode()
                  break
              else:
                print('             ---------------')
                print('      Please enter a valid option.')
                print('             ---------------')
          elif ravinerandompsv == 'endlessdarkness':
            print('             ---------------')
            print('      The darkness is endless! Go back.')
            print('             ---------------')
            time.sleep(0.5)
            story_mode()
            break
          elif ravinerandompsv == 'monster':
            print('             ---------------')
            print('              TO BE MADE')
            print('             ---------------')
            time.sleep(0.5)
            story_mode()
            break
        else:
          print('             ---------------')
          print('      Please enter a valid option.')
          print('             ---------------')
  return
# < END OF FUNCTION > #

# > cave_story() < #
def cave_story():
    leftrightcave = ['1', '2']
    keepexploringcave = ['3']
    menucavecc = ['menu']
    caveps = ['deadend', 'monster', 'endlessdarkness']
    while True:
      print('            You stumble across a cave. There are two passages.')
      print('            1. Go left')
      print('            2. Go right')
      print('            3. Keep exploring')
      caveglgr = input('            Enter your choice ("menu" for Menu.): ')
      if caveglgr == 'menu':
        print('             ---------------')
        mainmenu()
        break
      if caveglgr == '3':
        print('             ---------------')
        story_mode()
        break
      if caveglgr not in leftrightcave and keepexploringcave and menucavecc:
        print('             ---------------')
        print('       Please enter a valid option.')
        print('             ---------------')
      if caveglgr in leftrightcave:
          cavepsv = random.choice(caveps)
          if cavepsv == 'deadend':
            print('             ---------------')
            print('      You reached a deadend. How unlucky!')
            print('             ---------------')
            time.sleep(0.5)
            story_mode()
            break
          elif cavepsv == 'endlessdarkness':
            print('             ---------------')
            print('      The darkness is endless! Go back.')
            print('             ---------------')
            time.sleep(0.5)
            story_mode()
            break
          elif cavepsv == 'monster':
            print('             ---------------')
            print('              TO BE MADE')
            print('             ---------------')
            story_mode()
    return
# < END OF FUNCTION > #
  
# > story_mode() < #
def story_mode():
  storymodebiomes = ['cave', 'cave', 'forest', 'forest', 'ravine', 'ravine', 'desert','desert', 'village']
  storymodebiomes_rand = random.choice(storymodebiomes)
  if storymodebiomes_rand == 'cave':
    cave_story()
  elif storymodebiomes_rand == 'forest':
    forest_story()
  elif storymodebiomes_rand == 'ravine':
    ravine_story()
  elif storymodebiomes_rand == 'desert':
    desert_story()
  elif storymodebiomes_rand == 'village':
    village_story()
  return
# < END OF FUNCTION > #

# > inventory() < #
def inventory():
  print('               Not made yet!')
  mainmenu()
  return
# < END OF FUNCTION > #

# > shop() < #
def shop():
  print('               Not made yet!')
  mainmenu()
  return
# < END OF FUNCTION > #

# > mainmenu() < #
def mainmenu():
  print('         <<<<--- MAIN MENU --->>>>')
  time.sleep(0.5)
  while True:
      choicemm = input(f'        What would you like to do?\n        1. Story\n        2. Shop\n        3. Inventory\n        Enter a choice: ')
      choicemm_lower = choicemm.lower()
      if choicemm_lower in choicesmm:
          break
      elif choicemm_lower == 'seb?':
        typewriter_effect(f"Ah, yes. That's me. I'm the creator of this game. At the time I am writing this even the shop is not available. I am still developing this. Do you think Covert World has a future? Maybe it does. Anyway, you found this easter egg, but there are more. All you have to do is explore.")
        print(f'\n             ---------------')
      elif choicemm_lower == 'cage':
        print('             ---------------')
        print('                 Smash')
        print('             ---------------')
      else:
        print('             ---------------')
        print('       Please enter a valid option.')
        print('             ---------------')
  if choicemm_lower == '3':
    print('                𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡...')
    time.sleep(0.5)
    print('             ---------------')
    print('               INVENTORY')
    print('             ---------------')
    time.sleep(0.5)
    inventory()
  if choicemm_lower == '2':
    print('                𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡...')
    time.sleep(0.5)
    print('             ---------------')
    print('                 SHOP')
    print('             ---------------')
    time.sleep(0.5)
    shop()
  if choicemm_lower == '1':
    print('                𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡...')
    time.sleep(0.5)
    print('             ---------------')
    print('              STORY MODE')
    print('             ---------------')
    time.sleep(0.5)
    story_mode()
  return
# < END OF FUNCTION > #

#  #  #  #  #  #  #  #  #  #  #  #
#   _____    ____   _____   ______ 
#  / ____|  / __ \ |  __ \ |  ____|
# | |      | |  | || |  | || |__   
# | |      | |  | || |  | ||  __|  
# | |____  | |__| || |__| || |____ 
# \_____|   \____/ |_____/ |______|
#  #  #  #  #  #  #  #  #  #  #  #


print('          Welcome to Covert World.')
time.sleep(0.5)
mainmenu()
