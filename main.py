import string_utils
import random

def anagram():
    words_arr = ["anagram","tomato","robot","computer","artificial","something","Tuesday","lambda","square","python","viper","hypertext"]
    score = 0
    for l in words_arr:
        org_word = l
        shuf_word = string_utils.shuffle(l)
        print("------------------------")
        print("Unjumble the words, type pass to go to the next question")
        print("------------------------\n")
        print("Unshuffle the following word")
        print(shuf_word)
        loop_c =0
        while(loop_c!=2):
            user_ans = input("Enter your answer:")
            if(user_ans ==org_word):
                score+=1
                loop_c=0
                print("Correct Answer!!\n")
                break
            elif(user_ans=='pass'):
                loop_c=0
                print("Passed\n")
                break
            else:
                loop_c+=1
                print("Wrong Answer!\n")
        if(loop_c==2):
            print("Two wrong attempts!\nGAME OVER!!")
            print("Score:"+ str(score)+"\n")
            break
        elif(score==12):
            print("YOU WON!!\n")
        elif(l=='hypertext'):
            print("GAME OVER!!\n")
            print("Score:"+ str(score)+"\n")

def handcricket():
    choice = int(input("Press 1 for batting\nPress 2 for bowling: "))
    bat=0
    bowl=0
    if(choice==1):
        bat = batting()
        bowl = bowling()
    elif(choice==2):
        bowl = bowling()
        bat = batting()
    print("------------------------\nComputer batting score: "+ str(bowl))
    print("Player batting score: "+str(bat)+"\n------------------------\n")
    if(bat>bowl):
        print("Player wins")

    elif(bat<bowl):
        print("Computer wins")
    else:
        print("Match tied")

def batting():    
    print("------------------------\nPLAYER BATTING\n------------------------")  
    over=0
    ball=0
    player_bat_score=0
    while(over!=6):    
        print("("+str(over)+"."+str(ball)+")")
        batter = int(input("Enter a number from 0 to 6: "))
        comp_ball = random.randint(0,6)
        if(batter<0 or batter>6):
            print("Invalid number, bowled out")
            break
        elif(batter==comp_ball):
            print("OUT!!!\n\n")
            break
        else:
            print("Player scores: "+str(batter)+" runs \n")
            player_bat_score+= batter
        ball+=1
        if(ball==6):
            over+=1
            ball=0         
    print("Your batting score: "+str(player_bat_score))   
    return player_bat_score

def bowling():
    print("------------------------\nPLAYER BOWLING\n------------------------")
    over =0
    ball = 0
    comp_bat_score = 0
    while(over!=6):    
        print("("+str(over)+"."+str(ball)+")")
        bowler = int(input("Enter a number from 0 to 6: "))
        comp_bat = random.randint(0,6)
        if(bowler<0 or bowler>6):
            print("No ball, six runs awarded")
            comp_bat_score+=6
        elif(bowler==comp_bat):
            print("OUT!!!\n\n")
            break
        else:
            print("Computer scores: "+str(bowler)+" runs \n")
            comp_bat_score+= bowler
        ball+=1
        if(ball==6):
            over+=1
            ball=0         
    print("Computer batting score: "+str(comp_bat_score))   
    return comp_bat_score

print("------------------------\nWELCOME TO THE PLAY GAME!\n------------------------\n")

choice = 0
while(choice!=-1):
    choice = int(input("Enter 1 for jumbled words or 2 for hand cricket\nEnter -1 to exit "))
    if(choice==1):
        anagram()
    elif(choice==2):
        handcricket()
    elif(choice==-1):
        print("Thank you for playing!")
        break