import names
import random
import os
import time

#table

#defining player names

p1, p2, p3, p4, p5, p6, p7, p8 = (names.get_full_name(), names.get_full_name(),
                                  names.get_full_name(), names.get_full_name(),
                                  names.get_full_name(), names.get_full_name(),
                                  names.get_full_name(), names.get_full_name())

#defining player position

p1Pos, p2Pos, p3Pos, p4Pos, p5Pos, p6Pos, p7Pos, p8Pos = (
  "(GK)",
  "(GK)",
  "(DEF)",
  "(DEF)",
  "(MID)",
  "(MID)",
  "(ATT)",
  "(ATT)",
)

#defining player OVR stat

p1OVR, p2OVR, p3OVR, p4OVR, p5OVR, p6OVR, p7OVR, p8OVR = (
  random.randint(50, 80),
  random.randint(50, 80),
  random.randint(50, 80),
  random.randint(50, 80),
  random.randint(50, 80),
  random.randint(50, 80),
  random.randint(50, 80),
  random.randint(50, 80),
)

#machday vairiables:

teamOVR = (p1OVR + p2OVR + p3OVR + p4OVR + p5OVR + p6OVR + p7OVR + p8OVR) / 8
selectionChoice = 'who would you like to pick(enter numbers 1 or 2):\n1:'
playerpick1 = ""
playerpick2 = ""
currentlyPickGK = ('you are currently picking: GK')
formationSelection = [
  '1', '121', 'one', '2', 'two', '211', '3', 'three', '112'
]
pickSelection = ['1', '2', 'one', 'two', p1, p2, p3, p4, p5, p6, p7, p8]
oneSelection = ['1', '121', 'one']
twoSelection = ['2', 'two', '211']
threeSelection = ['3', 'three', '112']
currentOpponent = ''
machday = 1
ansYes = ['1', 'yes', 'YES', 'Yes']
ansNo = ['2', 'no', 'NO', 'No']
currentFormation = 0

# leugue things
fourthDiv = 'Walkers Leugue 2'
thirdDiv = 'John West Leugue 1'
secondDiv = 'snackright championship'
firstDiv = 'attackasnak premier leugue'

currentLeugue = fourthDiv

# intro for when you first run the game


def intro():
  managerName = input(str("what will be your managers name\n>>"))
  teamName = str(input("what do you want to call your team\n>>"))
  teamName = teamName + " FC"
  os.system('clear')
  print("well", managerName, "here is the", teamName, "squad:\n", "1:", p1,
        p1Pos, p1OVR, "\n", "2:", p2, p2Pos, p2OVR, "\n", "3:", p3, p3Pos,
        p3OVR, "\n", "4:", p4, p4Pos, p4OVR, "\n", "5:", p5, p5Pos, p5OVR,
        "\n", "6:", p6, p6Pos, p6OVR, "\n", "7:", p7, p7Pos, p7OVR, "\n", "8:",
        p8, p8Pos, p8OVR, "\n\n\n")
  print(teamName, 'is ready for', currentLeugue)
  time.sleep(2)
  input('\n\npress enter to continue\n')

#functions for different formation selections 

#if 121 is selected
def oneselected():
  global DEFselected
  DEFselected = 'none'
  while DEFselected not in pickSelection:
      print("select your CB:")
      print(selectionChoice, p3, p3Pos, p3OVR, '\n2:', p4, p4Pos, p4OVR)
      DEFselected = input()
      if DEFselected in ["1", "one"]:
        DEFselected = p3
      if DEFselected in ["2","two"]:
        DEFselected = p4
  os.system('clear')
  print("your two midfielders are:\n", p5, p5OVR, "\n", p6, p6OVR)
  global ATTselected
  ATTselected = 'none'
  while ATTselected not in pickSelection:
      print("select your ST:")
      print(selectionChoice, p7, p7Pos, p7OVR, '\n2:', p8, p8Pos, p8OVR)
      ATTselected = input()
      if ATTselected in ["1", "one"]:
        DEFselected = p7
      if ATTselected in ["2","two"]:
        DEFselected = p8

#if 211 selected
def twoselected():
  print("211 selected")

#if 112 selected:
def threeselected():
    global DEFselected
    DEFselected = 'none'
    while DEFselected not in pickSelection:
      print("select your CB:")
      print(selectionChoice, p3, p3Pos, p3OVR, '\n2:', p4, p4Pos, p4OVR)
      DEFselected = input()
      if DEFselected in ["1", "one"]:
        DEFselected = [p3]
      if DEFselected in ["2","two"]:
        DEFselected = [p4]


def gkselection():
  global GKselected
  GKselected = 'none'
  while GKselected not in pickSelection:
      print("GK:")
      print(selectionChoice, p1, p1Pos, p1OVR, '\n2:', p2, p2Pos, p2OVR)
      GKselected = input()
      if GKselected in ["1", "one"]:
        GKselected = p1
      if GKselected in ["2","two"]:
        GKselected = p2
    
      os.system('clear')
      print('Nice!')











#function to call when it is machday


def machday():
  os.system('clear')
  formationPicked = input(
    'what formation would you like to play: (⊕ = GK ● = outfield player)\n1: 121:\n  ●  \n ● ●  \n  ● \n  ⊕  \n2: 211\n  ●  \n  ●  \n ● ●  \n  ⊕  \n3: 112:\n ● ●  \n  ●  \n  ●  \n  ⊕ \n\n>>'
  )
  while formationPicked not in formationSelection:
    os.system('clear')
    formationPicked = input(
      'please enter correct input:\n what formation would you like to play: (⊕ = GK ● = outfield player)\n1: 121:\n  ●  \n ● ●  \n  ● \n  ⊕  \n2: 211\n  ●  \n  ●  \n ● ●  \n  ⊕  \n3: 112:\n ● ●  \n  ●  \n  ●  \n  ⊕ \n\n>>'
    )
  os.system('clear')
  print('Nice!')
  #start of selection procces
  gkselection()
  #if 121 formation picked
  if formationPicked in oneSelection:
    oneselected()
  #if 211 formation picked
  elif formationPicked in twoSelection:
    twoselected()
  #if 112 formation picked
  elif formationPicked in threeSelection:
    threeselected()
  print(GKselected)
  print(DEFselected)



  



#main program
intro()
machday()
