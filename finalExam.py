import random
# Uma career training game

"""
UMAS:

Meijiro McQueen
Initial stats:
spd: 82
sta: 112
pow: 80
guts: 120
wit: 96

T.M. Opera O
Initial stats:
spd: 83
sta: 120
pow: 83
guts: 113
wit: 101

Special Week
Initial stats:
spd: 83
sta: 88
pow: 98
guts: 90
wit: 91
"""

"""
Base skill training levels:
1: +9
2: +16
3: +23
4: +30
5: +37
"""

"""
Mood effects:
Great: training lvl+20% (5)
Good: +10%
Normal: no change
Bad: -10%
Awful: -20%
"""

"""
Energy ranges 0-5
Failure Chance:
4-5: 0%
3: 5%
2: 10%
1: 20%
0: 40%
"""

speed = 0
stamina = 0
power = 0
guts = 0
wit = 0

# Trainee options
# Lists are the initial stats
# [Speed, stamina, power, guts, wit]
specialWeek = [83, 88, 98, 90, 91]
TMOperaO = [83, 120, 83, 113, 101]
meijiroMcQueen = [82, 112, 80, 120, 96]
goldShip = [87, 101, 105, 81, 76]

# If training fails, this function will run
# Decreases mood and the stat that failed training
def failure(mood):
    print("\nTraining Failed")
    if mood>1:
        mood = mood-1

# Determines training success based on energy level
# Returns boolean values
# True if training succeeds 
# False if training fails
def trainingSuccess(energy):
    num=random.randint(1,100)
    if energy >=4:
        return True
    elif (energy==3) & (num >= 10):
        return True
    elif (energy==2) & (num >= 20):
        return True
    elif (energy==1) & (num >= 30):
        return True
    else:
        return False

#Decreases trainee energy 
#If energy would go into the negatives, does not decrease
#Returns the new energy
def decreaseEnergy(energy):
    if energy>=1:
        energy = energy-1
    return energy

# Determines increase level for trained stat
# trainingLevel determines base increase level
# mood will add a multiplier to base increase
def statIncreaseLvl(trainingLevel,mood):
    statIncrease = trainingLevel*7+9
        
    if mood == 5:
        statIncrease = statIncrease+(statIncrease*.2)
    elif mood == 4:
        statIncrease = statIncrease+(statIncrease*.1)
    elif mood == 2:
        statIncrease = statIncrease-(statIncrease*.1)    
    elif mood == 1:
        statIncrease = statIncrease-(statIncrease*.2)

    return statIncrease

# Train stat
# Increases the selected stat if training succeeds
def trainStat(stat, trainingLevel, mood, energy):
    if trainingSuccess(energy) == True:
        print("\nTraining Success!")
        stat += statIncreaseLvl(trainingLevel,mood)
    elif trainingSuccess(energy) == False:
        failure(stat, mood)
        stat = stat-5
    return stat


# Increases energy and mood by 2
# Maximum of 5 for both
# Returns a list of the new stats
def restTrainee(energy,mood):
    if energy<=3:
        energy+=2
    elif energy == 4:
        energy+=1
    if mood<=3:
        mood+=2
    elif mood == 4:
        mood+=1
    energyMoodList = []
    energyMoodList.append(energy)
    energyMoodList.append(mood)
    return energyMoodList


# Allows user to decide between training or resting
# Returns True if train is selected
# Returns False if rest is selected
def trainOrRest():
    userInput = input("Do you want to train or rest your trainee?")
    userInput = userInput.upper()
    if userInput == "TRAIN":
        return True
    elif userInput == "REST":
        return False

# prints start prompts
# lets user selest trainee
def startGame():
    print("\nWelcome to Pretty Derby (Python edition)!\n")
    print("Select a trainee:")
    print("""1: Special Week
2: TM Opera O
3: Meijiro McQueen
4: Gold Ship""")
    uma = int(input(""))
    if uma == 1:
        runGame(specialWeek)
    elif uma == 2:
        runGame(TMOperaO)
    elif uma == 3:
        runGame(meijiroMcQueen)
    elif uma == 4:
        runGame(goldShip)

# contains all function calls
def runGame(uma):
    print("\nCareer start!\n")
    print("SPD, STA, POW, GUTS, WIT")
    print(uma, "\n")
    energy = 5
    mood = 3
    # from the list of stats of the selected uma
    # defines variables
    speed = uma[0] 
    stamina = uma[1]
    power = uma[2]
    guts = uma[3]
    wit = uma[4]


    # user trains or rests trainee 5x
    for i in range (7):
        if trainOrRest():
            # User selects stat to train
            # Runs trainStat function based on the stat selected
            trainedStat = input("What stat do you you want to train?")
            trainedStat = trainedStat.upper()
            if trainedStat=="SPD":
                speed = trainStat(speed,(i+1),mood,energy)
                print("SPD:", speed)
                    
            elif trainedStat=="STA":
                stamina = trainStat(stamina,(i+1),mood,energy)
                print("STA:", stamina)
                
            elif trainedStat=="POW":
                power = trainStat(power,(i+1),mood,energy)
                print("POW:", power)
                
            elif trainedStat=="GUTS":
                guts = trainStat(guts,(i+1),mood,energy)
                print("GUTS:", guts)
                    
            elif trainedStat=="WIT":
                wit = trainStat(wit,(i+1),mood,energy)
                print("WIT:", wit)
            energy = decreaseEnergy(energy)
        else:
            energy = restTrainee(energy,mood)[0]
            mood = restTrainee(energy,mood)[1]

        print("\nEnergy:", energy)
        print("Mood:", mood, "\n")
    

startGame()