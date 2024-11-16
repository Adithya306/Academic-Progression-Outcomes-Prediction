# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solutions.
# Student ID: 20531885/20230900
# Date: 12/10/2023

from graphics import *

#defined function for progression outcome
def progression_outcome(pass_credit,defer_credit,fail_credit):
    if total_credit!=120:
        return("Total incorrect")
    elif pass_credit==120:
        return("Progress")
    elif pass_credit==100:
        return("Progress(module trailer)")
    elif (pass_credit==80)or(pass_credit==60)or(pass_credit==40 and fail_credit<=60)or(pass_credit==20 and fail_credit<=60)or(pass_credit==0 and fail_credit<=60):
        return("Do not progress-module retriever")
    elif(pass_credit==40 and fail_credit==80)or(pass_credit==20 and fail_credit>=80)or(pass_credit==0 and fail_credit>=80):
        return("Excluded")

#defined function for histogram
def Histogram():
    win=GraphWin("Histogram",800,600)
    win.setBackground("White")
    sub=Text(Point(200,40),"Histogram Results")
    sub.setSize(20)
    sub.setStyle("bold")
    sub.setTextColor(color_rgb(83,83,83))
    sub.draw(win)
    ln=Line(Point(40,450),Point(760,450))
    ln.draw(win)
    bar1=Text(Point(140,470),"Progress")
    bar1.setStyle("bold")
    bar1.setSize(15)
    bar1.setTextColor(color_rgb(145,158,198))
    bar1.draw(win)
    bar2=Text(Point(300,470),"Trailer")
    bar2.setStyle("bold")
    bar2.setSize(15)
    bar2.setTextColor(color_rgb(145,158,198))
    bar2.draw(win)
    bar3=Text(Point(480,470),"Retriever")
    bar3.setStyle("bold")
    bar3.setSize(15)
    bar3.setTextColor(color_rgb(145,158,198))
    bar3.draw(win)
    bar4=Text(Point(650,470),"Excluded")
    bar4.setStyle("bold")
    bar4.setSize(15)
    bar4.setTextColor(color_rgb(145,158,198))
    bar4.draw(win)
    
    rec1=Rectangle(Point(90,450-progress*10),Point(190,450))
    rec1.setFill(color_rgb(132,248,118))
    rec1.draw(win)
    
    rec2=Rectangle(Point(250,450-trailer*10),Point(350,450))
    rec2.setFill(color_rgb(117,188,10))
    rec2.draw(win)

    rec3=Rectangle(Point(430,450-retriever*10),Point(530,450))
    rec3.setFill(color_rgb(132,154,5))
    rec3.draw(win)

    rec4=Rectangle(Point(600,450-exclude*10),Point(700,450))
    rec4.setFill(color_rgb(203,165,168))
    rec4.draw(win)

    tot=Text(Point(200,520),str(total_outcome)+ " outcomes in total.")
    tot.setStyle("bold")
    tot.setSize(20)
    tot.setTextColor(color_rgb(145,158,198))
    tot.draw(win)

    barOut = Text(Point(140, 440-progress*10),progress)
    barOut.setStyle("bold")
    barOut.setTextColor(color_rgb(145,158,198))
    barOut.draw(win)
    barOut = Text(Point(300, 440-trailer*10),trailer)
    barOut.setStyle("bold")
    barOut.setTextColor(color_rgb(145,158,198))
    barOut.draw(win)
    barOut = Text(Point(480, 440-retriever*10),retriever)
    barOut.setStyle("bold")
    barOut.setTextColor(color_rgb(145,158,198))
    barOut.draw(win)
    barOut = Text(Point(650, 440-exclude*10),exclude)
    barOut.setStyle("bold")
    barOut.setTextColor(color_rgb(145,158,198))
    barOut.draw(win)

   

#Declaring variables    
progress=0
trailer=0
retriever=0
exclude=0
total_credit=0
List=[]
output=0


#main 

while True:
    try:
        pass_credit=int(input("Please enter your credit at pass: "))
        if pass_credit not in [0,20,40,60,80,100,120]:
            print("Out of range")
            pass_credit=int(input("Please enter your credit at pass: "))
    except ValueError:
        print("Integer required")
        continue
    try:
        defer_credit=int(input("Please enter your credit at defer: "))
        if defer_credit not in [0,20,40,60,80,100,120]:
            print("Out of range")
            defer_credit=int(input("Please enter your credit at defer: "))
    except ValueError:
        print("Integer required")
        continue
    try:
        fail_credit=int(input("Please enter your credit at fail: "))
        if fail_credit not in [0,20,40,60,80,100,120]:
            print("Out of range")
            fail_credit=int(input("Please enter your credit at fail: "))
    except ValueError:
        print("Integer required")
        continue
    total_credit=int(pass_credit + defer_credit + fail_credit)
    if progression_outcome(pass_credit,defer_credit,fail_credit)=='Progress':
        print("Progress")
        output="Progress"
        progress=progress+1
    elif progression_outcome(pass_credit,defer_credit,fail_credit)=='Progress(module trailer)':
        print("Progress(module trailer)")
        output="Progress(module trailer)"
        trailer=trailer+1
    elif progression_outcome(pass_credit,defer_credit,fail_credit)=='Do not progress-module retriever':
        print("Do not progress-module retriever")
        output="Do not progress-module retriever"
        retriever=retriever+1
    elif progression_outcome(pass_credit,defer_credit,fail_credit)=='Excluded':
        print("Excluded")
        output="Excluded"
        exclude=exclude+1
    else:
        print("Total incorrect")
        continue


#Making a list and append values to list
    inputs_list = str(output) + " - " + str(pass_credit) + "," + str(defer_credit) + "," + str(fail_credit)
    List.append(inputs_list)

    total_outcome = progress + trailer + retriever + exclude

#checking whether user want to continue or end and get results    
    cp = input("Would you like to enter another set of data? \n Enter 'y' for yes or 'q' to quit and view results: ")
    cp=cp.lower()
    if cp=='q':
        print(*List,sep='\n')
        Histogram()

#text file
        with open('file.txt','w')as text:
            for item in List:
                text.write(item+'\n')
        
       
        break
    else:
        while (cp!='y'):
            cp = input("Would you like to enter another set of data? \n Enter 'y' for yes or 'q' to quit and view results: ")
            cp=cp.lower()
       
    

        

    
