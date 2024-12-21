# Python slot machine...
import random
def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','🌠']

    return [random.choice(symbols) for symbol in range(3)]
# For every iteration in range(3), return random symbols

def print_row(row):
     print("*************")
     print(" | ".join(row)) # Using the join() method we are taking our iterable in this case as list, 
# joining each element by a space " | ".
     print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 15 
    return 0 # if all symbols do not match with our list, we do not want to give anything to user, they lost that spin!!
# We have to check to see , if all the elements in the 'row' is all same charcters....we do by 'if statement
# as above like if row[0] = index 0 of first symbols, is equal to row[1] index of 1 of second symbols,
# is equal to row[2] index of 2 of third symbols   

def main():
  balance = 100

  print("*************************")
  print("Welcome to Python Slots:" )
  print(" Symbols:  🍒🍉🍋🔔🌠")
  print("*************************")

  while balance > 0:
      print(f" Current balance: £{balance}")

      bet = input("Place your bet amount: ")

      if not bet.isdigit():
          print(" Enter a valid number: ")
          continue   # With this keywork 'continue' will skip current loop and start from bigining back to line 23
      bet = int(bet)   # type cast our bet, As we are reassigning our bet to int type....bcoz the line 23 is str data type....!
      if bet > balance:
          print("Insufficient funds")
          continue
      if bet <= 0:
          print("Bet must be greater than 0")
          continue
      balance -= bet
      row = spin_row() # once substract our balance(line 35), we call spin_row() function to spin row...this function 
# will return list...where we are going to generate three random sysbols...then return them within a list..      
# Now we call the function spin_row(), then within function spin_row() we declare a list of symbols = [], at
# line 4
      print("Spinning....\n")
      print_row(row) # we will call here print_row() fun and pass the argument as 'row'

      payout = get_payout(row, bet) 
# we will pass arguments as 'row' is a list, and 'bet', 'how much did we bet ?, to fun get_payout(),
# then we will be return with 'payout' which we will add to our balance...     
      if payout > 0:
          print(f" You won ${payout}")
      else:
          print("You lost this round")

      balance += payout        

      play_again = input("Do you want to spin again? (Y/N): ")

      if play_again == 'Y':
          break 
      print("*********************************************")
      print(f" Game over! Your final balance is ${balance}")
      print("*********************************************")
if __name__ == '__main__':
    main()
