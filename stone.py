bot = {"stone", "paper", "scissors"}
player = input( "'stone''paper''scissors' >>> " )
a = bot.pop()
print(a)

if bot == player:
    print( "draw" )
elif player == "scissors" and a == "stone":
    print( "BOT WIN" )
elif player == "paper" and a == "stone":
    print( "Player WIN" )
elif player == "stone" and a == "paper":
    print( "BOT WIN" )
elif player == "scissors" and a == "paper":
    print( "Player WIN" )
elif player == "paper" and a == "scissors":
    print( "BOT WIN" )
elif player == "stone" and a == "scissors":
    print( "Player WIN" )
else:
    print( "Leave NOW !" )
