import random

class Deck:
  def __init__(self):
    # self.QuantityofCards = [4,4,4,4,4,4,4,4,4,4,12]    #[Acecards, no. of face cards from 2-10(4 for each value), no of Special cards]
    # self.X = 10       #X is the special card (Joker ,King ,Queen)
    # self.ValueofCard = [11,2,3,4,5,6,7,8,9,10,self.X]
    self.Cards = []
    i = 2
    while i < 12:
      j = 0
      if i == 10:
        while j < 16:
          self.Cards.append(10)
          j += 1
      else:
        while j < 4:
          self.Cards.append(i)
          j += 1
      i += 1
    random.shuffle(self.Cards)

class Dealer:
  def __init__(self):
    self.dealer_deck = []

class Player:
  def __init__(self):
    self.player_deck = []

def Draw(PlayerX, DealerX, DeckX):
  i = 0
  while i < 2:
  #   x = random.choice(DeckX.ValueofCard)
  #   index1 = DeckX.ValueofCard.index(x)
  #   PlayerX.player_deck.append(x)
  #   DeckX.QuantityofCards[index1] -= 1
    PlayerX.player_deck.append(DeckX.Cards.pop(0))

  #   y = random.choice(DeckX.ValueofCard)
  #   index2 = DeckX.ValueofCard.index(y)
  #   DealerX.dealer_deck.append(y)
  #   DeckX.QuantityofCards[index2] -= 1
    DealerX.dealer_deck.append(DeckX.Cards.pop(0))
    i +=1

def ShowCard(PlayerX, DealerX):
  print(PlayerX.player_deck)
  print(DealerX.dealer_deck[0])
  
def Hit(obj):
  if obj == PlayerX:
    obj.player_deck.append(DeckX.Cards.pop(0))
  else:
    obj.dealer_deck.append(DeckX.Cards.pop(0))

def DoubleDown(PlayerX):
  PlayerX.player_deck.append(DeckX.Cards.pop(0))
  dealerloop()

def checkforaces(obj):
 ## Checking for Ace cards and their values
  if obj == PlayerX:
    while sum(obj.player_deck) > 21:
      if 11 in obj.player_deck:
        obj.player_deck[obj.player_deck.index(11)] = 1
  else:
    while sum(obj.dealer_deck) > 21:
      if 11 in obj.dealer_deck:
        obj.dealer_deck[obj.dealer_deck.index(11)] = 1

def checkwin(PlayerX, DealerX):
 
  if sum(PlayerX.player_deck)<=21 and sum(PlayerX.player_deck) > sum(DealerX.dealer_deck):
    print(PlayerX.player_deck)
    print(DealerX.dealer_deck)
    print("You have won")
  elif sum(PlayerX.player_deck) == sum(DealerX.dealer_deck):
    print(PlayerX.player_deck)
    print(DealerX.dealer_deck)
    print("It's a DRAW")
  else:
    print(PlayerX.player_deck)
    print(DealerX.dealer_deck)
    print("You have lost")

def playerloop():
  x = input("What do you wanna play? ")
  while x != "End":
    if (x == "Hit" or x== "hit") and sum(PlayerX.player_deck)<=21:
      Hit(PlayerX)
      print(PlayerX.player_deck)
      checkforaces(PlayerX)
      if sum(PlayerX.player_deck) > 21:
        print("You're Bust")
        break
    elif (x == "DoubleDown" or x == "doubledown") and sum(PlayerX.player_deck)<=21:
      DoubleDown(PlayerX)
      print(PlayerX.player_deck)
      break
    x = input("What do you wanna play? ")

def dealerloop():
  while sum(DealerX.dealer_deck) < 17:
    checkforaces(DealerX)
    Hit(DealerX)
    print(DealerX.dealer_deck)
  checkwin(PlayerX, DealerX)

def start():
  Draw(PlayerX, DealerX, DeckX)
  ShowCard(PlayerX, DealerX)
  playerloop()
  dealerloop()
  
DeckX = Deck()
PlayerX = Player()
DealerX = Dealer()

# print(DeckX.Cards)
start()
