import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]

  def __str___(self):
    return self.rank + " of " + self.suit

class Deck:
  def __init__(self):
    self.allCards = []

    for suit in suits:
      for rank in ranks:
        self.allCards.append(Card(suit,rank))

  def shuffle(self):
    random.shuffle(self.allCards)

  def getACard(self):
    return self.allCards.pop()

class Player:
  def __init__(self, name):
    self.name = name

    self.allCards = []

  def getACard(self):
    return self.allCards.pop(0) # get the top card

  def addCards(self, newCards):
      if type(newCards) == type([]):
          self.allCards.extend(newCards)
      else:
          self.allCards.append(newCards)
  
  
  def __str__(self):
      return 'Player {} has {} cards.'.format(self.name, len(self.allCards))

####### SET UP THE GAME ########

playerOne = Player("One")
playerTwo = Player("Two")

newDeck = Deck()
newDeck.shuffle()

for x in range(26):
  playerOne.addCards(newDeck.getACard())
  playerTwo.addCards(newDeck.getACard())


######## PLAY THE GAME #########

gameOn = True
round = 0
while gameOn:

  round += 1
  print("Round: {}".format(round))

  if len(playerOne.allCards) == 0:
    print("Game is over, Player 1 has no more cards!")
    print("Player 2 has won the game!")
    gameOn = False
    break

  if len(playerTwo.allCards) == 0:
    print("Game is over, Player 2 has no more cards!")
    print("Player 1 has won the game!")
    gameOn = False
    break

  playerOneCards = []
  playerTwoCards = []

  playerOneCards.append(playerOne.getACard())
  playerTwoCards.append(playerTwo.getACard()) 

  atWar = True

  while atWar:
    if playerOneCards[-1].value < playerTwoCards[-1].value:
      playerOne.addCards(playerOneCards)
      playerOne.addCards(playerTwoCards)

      atWar = False

    elif playerTwoCards[-1].value < playerOneCards[-1].value:
      playerTwo.addCards(playerOneCards)
      playerTwo.addCards(playerTwoCards)

      atWar = False
      
    else:
      print("WAR!")

      # see if players have enough cards. In this game it's 10 cards.

      if len(playerOne.allCards) < 10:
        print("Game is over, Player 1 doesn't have 10 cards left")
        print("Player 2 has won the game!")
        gameOn = False
        break

      elif len(playerTwo.allCards) < 10:
        print("Game is over, Player 2 doesn't have 10 cards left")
        print("Player 1 has won the game!")
        gameOn = False
        break

      else:
        for i in range(10):
          playerOneCards.append(playerOne.getACard())
          playerTwoCards.append(playerTwo.getACard())