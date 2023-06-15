def info():
    program_name = "Rock, Paper, Scissors Game"
    build = "Build 2.04.25 Pre-Release"
    print ()
    print (program_name)
    print (build)

def error():
    print ()
    print ("Invalid Value. Try Again.")

results = ""
player = ""
bot = ""
s_p = 0
s_b = 0
ic = 0
c_m = False
print ()
username = input ("Enter Username: ")
info()
t = 1
while (t > 0):
    print ()
    print ("Main Menu", "\n1. Start Game", "\n2. Options", "\n3. Exit")
    choice = input("Select Choice (Number): ")
    if choice == "1":
        s_b = 0
        s_p = 0
        if c_m == False:
            t_1 = 1
            while (t_1 > 0):
                import random

                rng = random.randrange(1,4)
                if rng == 1:
                    bot = "Rock"
                elif rng == 2:
                    bot = "Paper"
                elif rng == 3:
                    bot = "Scissors"
        elif c_m == True:
            print ()
            print ("Competitive Mode")
            print ("Win condition: First to 5 points wins.")
            t_2 = 1
            while (t_2 > 0):
                import random

                rng = random.randrange(1,4)
                rng_1 = random.randrange(1,4)
                rng_2 = random.randrange(1,4)
                rng_3 = random.randrange(1,4)

                rng_avg = float(round((rng + rng_1 + rng_2 + rng_3)/4, 1))
                if rng_avg >= float(1.0) and rng_avg <= float(1.6):
                    bot = "Rock"
                elif rng_avg >= float(1.7) and rng_avg <= float(2.3):
                    bot = "Paper"
                elif rng_avg >= float(2.4) and rng_avg <= float(3.0):
                    bot = "Scissors"
        print ()
        if ic == 0:
            i_player = input ("Rock, Paper, Scissors, Forfeit: ")
            player = i_player.capitalize()
        elif ic == 1:
            print ("Guide:", "1. Rock", "2. Paper", "3. Scissors", "4. Forfeit")
            i_player_1 = input("Enter choice here: ")
            if i_player_1 == "1":
                player = "Rock"
            elif i_player_1 == "2":
                player = "Paper"
            elif i_player_1 == "3":
                player = "Scissors"
            elif i_player_1 == "4":
                player = "Forfeit"
        print ()
        print (str(username), "attacks with:", player)
        print ("Bot counters with:", bot)
        if player == "Forfeit":
            print (s_p,"-",s_b)
            if s_p > s_b:
                print (username, "Wins")
            elif s_p < s_b:
                print ("Bot Wins")
            elif s_p == s_p:
                print ("Draw")
            t_1 = 0
        elif player == "Rock" and bot == "Rock":
            results = "Draw"
        elif player == "Rock" and bot == "Paper":
            results = "Bot Wins"
        elif player == "Rock" and bot == "Scissors":
            results = str(username)+ " Wins"
        elif player == "Paper" and bot == "Rock":
            results = str(username)+ " Wins"
        elif player =="Paper" and bot == "Paper":
            results = "Draw"
        elif player == "Paper" and bot == "Scissors":
            results = "Bot Wins"
        elif player == "Scissors" and bot == "Rock":
            results = "Bot Wins"
        elif player == "Scissors" and bot == "Paper":
            results = str(username)+ " Wins"
        elif player == "Scissors" and bot == "Scissors":
            results = "Draw"
        else:
            results = "Error. Unknown Value."
        print ()
        print ("Results:" ,results)
        if results == "Bot Wins":
            s_b += 1
        elif results == "Draw" or results == "Error. Unknown Value.":
            pass
        elif results == str(username)+ " Wins":
            s_p += 1
        print (s_p,"-",s_b)
    elif choice == "2":
        t_2 = 1
        while (t_2 > 0):
            print ()
            print ("Options:", "\n1. Change input type", "\n2. Competitive Mode", "\n3. Reset to Default", "\n4. Debug: Show Memory", "\n5. Exit")
            choice_1 = input("Select (Number): ")
            if choice_1 == "1":
                print ()
                print ("Input type:", "\n1. Word-based", "\n2. Number-based")
                choice_2 = input("Select type (Number): ")
                if choice_2 == "1":
                    ic = 0
                elif choice_2 == "2":
                    ic = 1
                else:
                    error()
            elif choice_1 == "2":
                print ()
                print ("Competitive Mode: Yes or No?")
                i_choice_3 = input("Enter choice here: ")
                choice_3 = i_choice_3.casefold()
                if choice_3 == "yes":
                    c_m = True
                elif choice_3 == "no":
                    c_m = False
                else:
                    error()
            elif choice_1 == "3":
                ic = 0
                c_m = False
                print ("Reset successful")
            elif choice_1 == "4":
                print (t)
                print (t_2)
                print (ic)
                print (c_m)
            elif choice_1 == "5":
                t_2 = 0
            else:
                error()
    elif choice == "3":
        print ()
        i_choice_2 = input("Are you sure you want to quit? Yes or No? ")
        choice_2 = i_choice_2.casefold()
        if choice_2 == "yes":
            t = 0
            info()
        elif choice_2 == "no":
            pass
        else:
            error()