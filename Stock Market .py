import turtle
import random
import math
import datetime


turtle.hideturtle()


#Background
turtle.setup(800,400)
turtle.bgcolor("white")


#Stock Graph frame
graph = turtle.Turtle()
graph.speed(0)
graph.penup()
graph.goto(-120,-60)
graph.pendown()
graph.left(90)


# 1) Make a sqaure
graph.color("AliceBlue")
graph.begin_fill()
for square in range(2):
    graph.forward(225)
    graph.right(90)
    graph.forward(480)
    graph.right(90)
    
graph.hideturtle()
graph.end_fill()


#Company List
companyList = ["Alphabet Class A",20.00,"Apple",10.00,"Meta Platforms",
           5.00,"Tesla",50.00]


#Company sqaure
companySqaure = turtle.Turtle()
companySqaure.speed(0)
companySqaure.penup()
companySqaure.goto(-150, -40)
companySqaure.pendown()
companySqaure.right(180)
for i in range(2):
    companySqaure.forward(220)
    companySqaure.right(90)
    companySqaure.forward(205)
    companySqaure.right(90)

companySqaure.hideturtle()


#Stock text (title)
userS = turtle.Turtle()
userS.hideturtle()
userS.speed(0)
userS.penup()
userS.goto(-295, 143)
userS.pendown()
userS.write("Stock List", font=("Arial", 15))


#Stock text (body)
userSb = turtle.Turtle()
userSb.hideturtle()
userSb.penup()
bodyYcor = 120
for company in companyList:
    userSb.goto(-350, bodyYcor)
    userSb.pendown()
    userSb.write(company, font=("Arial", 15))
    userSb.penup()
    bodyYcor -= 20


#Dictionary of company
companyD = {}

for i in range(len(companyList)):
    if i % 2 == 0:
        onlyName = companyList[i]
    else:
        onlyPrice = companyList[i]
        if onlyName not in companyD:
            companyD[ onlyName ] = onlyPrice
            

#Saving the data of user's stock report
def stockReport():
    global stockReportF
    stockReportD = {}
    if userStockI != "":
        stockReportD[ userStockI ] = investB
        now = datetime.datetime.now()
        stockReportF = {}
        stockReportF[now.strftime("%Y-%m-%d %H:%M:%S")] = stockReportD
        print(stockReportF)
        

#User budget sqaure
budgetSqaure = turtle.Turtle()
budgetSqaure.speed(0)
budgetSqaure.penup()
budgetSqaure.goto(-150, -60)
budgetSqaure.pendown()
budgetSqaure.right(180)
for i in range(2):
    budgetSqaure.forward(220)
    budgetSqaure.left(90)
    budgetSqaure.forward(100)
    budgetSqaure.left(90)

budgetSqaure.hideturtle()


#Budget text
userB = turtle.Turtle()
userB.hideturtle()
userB.penup()
userB.goto(-350, -140)
userB.pendown()
userB.write("Budget: £ ", font=("Arial", 20))


#Profit and stock report sqaure
turtle.speed(0)
turtle.penup()
turtle.goto(-120, -90)
turtle.pendown()
for i in range(2):
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)

turtle.penup()
turtle.goto(120, -90)
turtle.pendown()
for i in range(2):
    turtle.forward(240)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)


# 1) Profit text
profit = turtle.Turtle()
profit.penup()
profit.hideturtle()
profit.goto(-90, -135)
profit.pendown()
profit.write("Value: £",font=("Arial", 20) )


# 2) US & UK Indices text
usIndices = turtle.Turtle()
usIndices.hideturtle()
usD = {"Kospi" : 2.909, "S&P 500" : 4.594, "Nasdaq 100" : 16025,
       "FTSE 100" : 7.044}

usIndicesY = -107
for indices in usD:
    usIndices.penup()
    usIndices.goto(137, usIndicesY)
    usIndices.pendown()
    usIndices.write(indices, font=("Arial", 12, "bold"))
    usIndicesY -= 17
    
usIndicesY = -107
for indices in usD:
    usIndices.penup()
    usIndices.goto(240, usIndicesY)
    usIndices.pendown()
    usIndices.write(usD[indices], font=("Arial", 13))
    usIndicesY -= 17
    

#Asking user Name
userN = turtle.Turtle()
userN.hideturtle()
userN.penup()
userN.goto(-350, -100)
userN.pendown()
userN.write("Name: ", font=("Arial", 20))


#Asking user name
userName = input("Name: ")
if userName != "":
    userN.penup()
    userN.forward(70)
    userN.pendown()
    userN.write(userName, font=("Arial", 20))
        

#Asking user to start a stock simulation
def userStart():
    global userStockI
    global investB
    global budget
    userStart = "y"
    while userStart == "y":
        #Asking user about the stock
        print("")
        print("Stock list")
        count = 1
        for key in companyD:
            print(count,":", end = " ")
            print(key)
            count += 1
        print("")
        userStockI = input("Which stock you want to invest? ")
        while userStockI != "":
            if userStockI in companyList:
                print("")
                userStockB = input("How many quantitiy you want to buy? ")
                investB = (int(userStockB) * companyD[userStockI])
                if investB >= companyD[ "Meta Platforms" ] and investB < float(budget):
                    print("")
                    stockReport()
                    budget = (float(budget) - investB)
                    budget = "{:.1f}".format(budget)
                    userB.undo()
                    userB.write(budget, font=("Arial", 20))
                    userStockI = ""
                    userStart = "n"
                elif investB < companyD[ "Meta Platforms" ]:
                     print("")
                     print("Investing declined due to low balance...")
                else:
                    print("")
                    print("Investing declined due to higher price than your budget...")
            else:
                print("")
                userStockI = input("Try again: ")


#Inside of the graph
bar = turtle.Turtle()
bar.hideturtle()
bar.speed(0)
bar.penup()
bar.goto(-110, 50)
bar.pendown()
bar.left(90)


# 1) Blue and red bar; aka chart
def chart():
    global investB
    global earning
    global budget
    barYcor = 50
    barRandom  = random.randint(-20,20)
    while bar.xcor() <= 350:
        if barRandom > 0:
            bar.begin_fill()
            bar.color("red")
            for i in range(2):
                bar.forward(barRandom)
                bar.right(90)
                bar.forward(10)
                bar.right(90)
            bar.end_fill()
            bar.penup()
            bar.goto(bar.xcor() + 12, barYcor)
            bar.pendown()
            
        elif barRandom == 0:
            bar.begin_fill()
            bar.color("black")
            for i in range(2):
                bar.forward(barRandom)
                bar.right(90)
                bar.forward(10)
                bar.right(90)
            bar.end_fill()
            bar.penup()
            bar.goto(bar.xcor() + 12, barYcor)
            bar.pendown()
            
        else:
            bar.begin_fill()
            bar.color("blue")
            for i in range(2):
                bar.forward(barRandom)
                bar.right(90)
                bar.forward(10)
                bar.right(90)
            bar.end_fill()
            bar.penup()
            bar.goto(bar.xcor() + 12, barYcor)
            bar.pendown()
            
        #Calculating an earning rate
        barRandomF = barRandom / 100

        if barRandom > 0:
            earning = investB * (1 + barRandomF)
            print("Current Rate: +{0}%".format(barRandom))
            print("Current Value: £{:.1f}".format(earning))
            
        else:
            earning = investB * (1 + barRandomF)
            print("Current Rate: {0}%".format(barRandom))
            print("Current Value: £{:.1f}".format(earning))
            
        investB = earning
        barRandom = random.randint(-20,20)
        barYcor = barYcor + barRandom

    print("")
    print("Your profit: £{:.1f}".format(earning))
    turtle.undo()
    earningForProfit = "{:.1f}".format(earning)
    turtle.penup()
    turtle.goto(-18,-135)
    turtle.pendown()
    turtle.write(earningForProfit, font=("Arial", 20) )
    

    #Updating the budget
    userB.undo()
    budget = (float(budget) + earning)
    budget = "{:.1f}".format(budget)
    userB.write(budget,font=("Arial", 20))

         
#Defining a budget
budget = 100.00
userB.penup()
userB.forward(85)
userB.pendown()
userB.write(budget, font=("Arial", 20))



#Stock simulation begins
print("")
print("Hello {0}!".format(userName))
print("")
print("You can choose four types of differnt stocks to invest.")
print("Once your budget is lower than the lowest stock, you cannot invest!")
print("Show your investing skills!")
print("Good luck {0}!".format(userName))
print("")
playGame = input("Do you want to start? y or n: ")
while playGame != "":
    if playGame == "y":
        userStart()
        print("")
        userStockG = input("Press y to operate a graph: ")
        print("")
        if userStockG == "y":
            chart()
            print("")
            playGame = input("Do you want to invest again? y or n: ")
            if playGame == "y":
                bar.clear()
                bar = turtle.Turtle()
                bar.hideturtle()
                bar.speed(0)
                bar.penup()
                bar.goto(-110, 50)
                bar.pendown()
                bar.left(90)
            else:
                print("")
                print("Stock market closed...")
                break
    else:
        playGame = input("Try again: ")







