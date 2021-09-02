import random
import random as ran 
user_w=0
comp_w=0
n=int(input("Enter number of series you want paly: "))
i=0
for i in range(n):
    # choose th toss opetion 
    user=input("Choose ODD or EVEN: ").lower()
    if user=="odd":
        comp="even"
    else:
        comp="odd"
    print("user choosed:-",user)
    print("computer choosed:-",comp)

    # bounce the toss
    toss=0
    user_n = int(input("Enter any number between 1 to 6 including 1&6 :"))
    comp_n = ran.randint(1,6)
    
    print("user choosed:-",user_n)
    print("computer choosed:-",comp_n)
    
    toss=user_n+comp_n
    print("toss :- ",toss)

    # choose batting or balling
    if toss%2==0:
        if comp=="even":
            print("computer won the toss :) ")
            comp2=random.choice(("bat","ball"))
            print("\n computer choose "+comp2+" first \n")
            if comp2=="bat":
                user2="ball"
            else:
                user2="bat"
        else:
            print("user won the toss :) ")
            user2=input("choose bat or ball: ").lower()
            print("\n user choose "+user2+" first \n")
            if user2=="bat":
                comp2="ball"
            else:
                comp2="bat"
    else:
        if comp=="odd":
            print("computer won the toss :) ")
            comp2=random.choice(("bat","ball"))
            print("\n computer choose "+comp2+" first \n")
            if comp2=="bat":
                user2="ball"
            else:
                user2="bat"
        else:
            print("user won the toss :) ")
            user2=input("choose bat or ball: ").lower()
            print("\n user choose "+user2+" first \n")
            if user2=="bat":
                comp2="ball"
            else:
                comp2="bat"

    #func of batting and balling
    counter_c = 0
    counter_u = 0
    def user_bat_com_ball():
        global counter_c
        global counter_u
        comp_3=0
        user_3=1
        print("------user's batting-----")
        while comp_3 != user_3:
            comp_3 = ran.randint(1,6)
            user_3 = int(input("Enter any number between 1 to 6 including 1&6 :"))
            print("computer choose the run :-",comp_3)
            print("User choose the run :-",user_3)
            if(comp_3!=user_3):
                counter_u = counter_u + user_3  
        print("User's run :--",counter_u)

    def user_ball_com_bat():
        global counter_c
        global counter_u
        comp_3=0
        user_3=1
        print("------user's balling-----")
        while comp_3 != user_3:
            comp_3 = ran.randint(1,6)
            user_3 = int(input("Enter any number between 1 to 6 including 1&6 :"))
            print("computer choose the run :-",comp_3)
            print("User choose the run :-",user_3)
            if(comp_3!=user_3):
                counter_c = counter_c + comp_3
        print("computer's run :--",counter_c)

    #decide winner
    if comp2 == "bat":
        user_ball_com_bat()
        user_bat_com_ball()
        if counter_u > counter_c:
            print("User won....")
            user_w=user_w+1
        elif counter_c==counter_u:
            print("match tie....")
        else:
            print("computer won.....")
            comp_w=comp_w+1
        
    if comp2 == "ball":
        user_bat_com_ball()
        user_ball_com_bat()
        if counter_u > counter_c:
            print("User won")
            user_w=user_w+1
        elif counter_c==counter_u:
            print("match tie....")
        else:
            print("computer won")
            comp_w=comp_w+1

#decide series winner
print("Total match won by User: ", user_w)
print("Total match won by Computer: ", comp_w)
if user_w>comp_w:
  print("User won the series!!!!")
elif user_w==comp_w:
  print("series tie!!!!")
else:
    print("Computer won the series!!!!")