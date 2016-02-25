# Hello Peer Assessor
# Have a nice day ;)

def rpsls(player_choice): 
            
           
            print "Player chooses" , player_choice \
            
            if player_choice=="rock":
                player_choice=0
            elif player_choice=="Spock":
                player_choice=1
            elif player_choice=="paper":
                player_choice=2
            elif player_choice=="lizard":
                player_choice=3
            else:
                player_choice=4
            
        
            import random
            comp_number = random.randrange(0,5)    
            if comp_number ==0:  
                print 'Computer chooses rock'
            elif comp_number ==1:
                print 'Computer chooses Spock'      
            elif comp_number ==2:
                print 'Computer chooses paper'
            elif comp_number ==3:
                print 'Computer chooses lizard'
            else:
                print 'Computer chooses scissors'
            
            
           
            modulo=player_choice%5
            
            if comp_number==player_choice:
                print "Player and Computer tie!"
            elif comp_number-modulo >0:
                print 'Computer wins !' 
            else:
                print 'Player wins !'
            
            print "\n"


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

def f(a):
    b=-5*(a**5) + 69*(a**2) - 47
    return b 
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    FV= present_value*(1+rate_per_period)**periods
    print "$1000 at 2% compounded daily for 3 years yields $", FV
import math
(1/4)*5*(7**2)/math.tan(math.pi/5)


# Hello Peer Assessor
# Have a nice day ;)

def rpsls(player_choice): 
            
           
            print "Player chooses" , player_choice \
            
            if player_choice=="rock":
                player_choice=0
            elif player_choice=="Spock":
                player_choice=1
            elif player_choice=="paper":
                player_choice=2
            elif player_choice=="lizard":
                player_choice=3
            else:
                player_choice=4
            
        
            import random
            comp_number = random.randrange(0,5)    
            if comp_number ==0:  
                comp_choice="rock"
                
            elif comp_number ==1:
                comp_choice='Spock'      
            elif comp_number ==2:
                comp_choice='paper'
            elif comp_number ==3:
                comp_choice='lizard'
            else:
                comp_choice='lscissors'
            print 'Computer chooses rock', comp_choice
            
           
            
            
            if comp_number==player_choice:
                print "Player and Computer tie!"
            elif (comp_number-player_choice)%5 == 1 or (comp_number-player_choice)%5==2:
                print 'Computer wins !' 
            else:
                print 'Player wins !'
            
            print "\n"


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")