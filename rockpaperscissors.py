from sys import exit #so we can cleanly exit game at end
import random # so we can get computer to decide on selection
continueGame = 'y'
selection = ['rock', 'paper', 'scissors']
playerScore = 0
computerScore = 0



def start():
    while continueGame == 'y' or 'Y':
        mainGame()

def mainGame():
    bestOf = 3
    while bestOf > 0:
        player = playerSelection()
        computer = computerSelection()
        determineWinner(player, computer)
        bestOf-=1
    # overallWinner(playerScore, computerScore)
    print('You scored ', playerScore, ' - ', computerScore,'against the computer')


    keepPlaying()

def playerSelection():
    while True: #validation done in while loop
        choice = input('Rock, Paper or Scissors?')
        choice = choice.lower()
        if choice not in ('r', 'p', 's'):
            print("Not an appropriate choice. Use r, p or s")
        else:
            break
        # once it has passed validation we change to word form
    match choice: 
        case 'r':
            choice = 'rock'
        case 'p':
            choice = 'paper'
        case 's':
            choice = 'scissors'
    return choice # and return the word

def computerSelection():
    return selection[random.randint(0,2)] #return the selection in word form

def determineWinner(player, computer):
    global computerScore
    global playerScore
    wonBy = {'rock' : 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    if player == computer:
        print('tie')
    elif (wonBy[player]) == computer:
        print('you won', player, 'beats', computer)
        playerScore+=1
    elif (wonBy[computer]) == player:
        print('you lost', computer, 'beats', player)
        computerScore+=1
    print (player)
    print (computer)

def overallWinner():
    print('You scored ', playerScore, ' - ', computerScore,'against the computer')

def keepPlaying():
    while True:
        continueGame = (input('Do you want to contine? y') or 'y') # default of yes
        if continueGame.lower() not in  ('y', 'n'): #validate for y or n
            print("Not an appropriate choice. Use \'y\' or \'n\'")
        elif continueGame.lower() == 'n': 
            print('Nice playing, well done!')
            exit(0) #once user enters n quit game
        else:
            # playerScore = 0
            # computerScore = 0
            break
    
    



start()
