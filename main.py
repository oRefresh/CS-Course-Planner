# Final CS 111 Project created by Yusif Shawish


import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()

# Creates the Gen ED screen
def general_elective_screen():
    s.clearscreen()
    s.bgcolor("lavender")
    t.penup()
    t.goto(0, 0)
    t.write("Wait! You must choose a General Elective!", align="center", font=("Arial", 30, "normal"))
    global elective
    elective = []
    elective.append(turtle.textinput("General Elective", "Visit the UIC General Elective class: https://catalog.uic.edu/ucat/degree-programs/general-education/"))
    elective.append(turtle.textinput("How many hours?", "Write Credit hours: "))
    elective.append(turtle.textinput("Subject?", "Write Subject: "))
    elective.append(turtle.textinput("Course Number?", "Write Course Number: "))
    return elective


# Creates the Science Elective Screen
def science_elective_screen():
    s.clearscreen()
    s.bgcolor("green")
    t.penup()
    t.goto(0,0)
    t.write("Wait! You must choose a Science Elective!", align="center", font=("Arial", 30, "normal"))
    global elective
    elective = read_elective_file("Science Electives.txt")

# Creates the Math Elective Screen
def math_elective_screen():
    s.clearscreen()
    s.bgcolor("blue")
    t.penup()
    t.goto(0, 0)
    t.write("Wait! You must choose a Math Elective!", align="center", font=("Arial", 30, "normal"))
    global elective
    elective = read_elective_file("Math Electives.txt")

# Creates the tech Elective Screen
def technical_elective_screen():
    s.clearscreen()
    s.bgcolor("red")
    t.penup()
    t.goto(0, 0)
    t.write("Wait! You must choose a Technical Elective!", align="center", font=("Arial", 30, "normal"))
    global elective
    elective = read_elective_file("Technical Electives.txt")

# Reads the elective files and returns the elective choice so it can be reinputed into the schedule
def read_elective_file(file_name):
    elective_file = open(file_name)
    elective_file_list = elective_file.readlines()
    class_list = []
    for f in range(len(elective_file_list)):
        elective_class_info = elective_file_list[f].split(",")
        for g in range(len(elective_class_info)):
            elective_class_info[g] = elective_class_info[g].strip("\n")
        class_list.append(elective_class_info[0])
        print(f"Class Name: {elective_class_info[0]} \nCredits: {elective_class_info[1]} \nSubject: {elective_class_info[2]} \nCourse Number: {elective_class_info[3]}\n-----------------")
    elect_choice = turtle.textinput("Elective", "Choice: (Check the Console)")
    while(elect_choice not in class_list):
        elect_choice = turtle.textinput("Not a valid class: )", "Pick a Class: (Check the Console")
    for f in range(len(elective_file_list)):
        elective_class_info = elective_file_list[f].split(",")
        for g in range(len(elective_class_info)):
            elective_class_info[g] = elective_class_info[g].strip("\n")
        if elective_class_info[0] == elect_choice:
            elect_choice = elective_class_info
            return elect_choice


# Reads the original file and splits it as well as runs the elective files to read
def read_file(file_name ):
    raw_file = open("Semester" + file_name +".txt")
    file_list = raw_file.readlines()
    global schedule
    schedule = []

    for i in range(len(file_list)):
        class_info = file_list[i].split(",")
        for x in range(len(class_info)):
            class_info[x] = class_info[x].strip("\n")
            if class_info[0] == "Science Elective":
                science_elective_screen()
                class_info = elective
                break
            elif class_info[0] == "Math Elective":
                math_elective_screen()
                class_info = elective
                break
            elif class_info[0] == "Technical Elective":
                technical_elective_screen()
                class_info = elective
                break
            elif class_info[0] == "Gen ED":
                general_elective_screen()
                class_info = elective
                break
        schedule.append(class_info)
    choose_time_slot()

# Creates the rules uesd in placing each class in its place
def choose_time_slot():
    global schedule
    list_of_times_monday = ["8:00", "9:00", "10:00", "11:00", "12:00","1:00", "2:00", "3:00", "4:00", "5:00", "6:00"]
    list_of_times_tuesday = ["8:00", "10:00","12:00","2:00","4:00"]
    for i in range(len(schedule)):
        s.clearscreen()
        t.write(f"What time would you like to take \n{schedule[i][0]} ", align="center", font=("Arial", 20, "normal"))

        if schedule[i][2] == "ENGR":
            schedule[i].append("8:00")
            schedule[i].append("Thursday")
            list_of_times_tuesday.remove("8:00")

        elif schedule[i][2] == "English" or schedule[i][2] == "PHYS" or schedule[i][2] == "BIOS" or schedule[i][2] == "CHEM" or schedule[i][2] == "EAES":
            time = turtle.textinput("Class time", "Enter the time ")
            while (time not in list_of_times_tuesday):
                time = turtle.textinput("Class time", "Enter a valid time ")
            schedule[i].append(time)
            list_of_times_tuesday.remove(time)
            schedule[i].append("Tuesday")

        else:
            time = turtle.textinput("Class time", "Enter the time ")
            while (time not in list_of_times_monday):
                time = turtle.textinput("Class time", "Enter a valid time ")
            list_of_times_monday.remove(time)
            schedule[i].append(time)
            schedule[i].append("Monday")
    s.clearscreen()
    draw_schedule()

# Creates random colors
def random_color():
    all_colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple","skyblue",
                  "cyan", "turquoise", "lightgreen", "green","gray"]
    rand_int = random.randint(0, len(all_colors) - 1)
    color = all_colors[rand_int]
    all_colors.pop(rand_int)
    return color

# Draws the main Scheduele sheet
def draw_schedule():
    global schedule
    turtle.tracer(False)

    s.setup(810,610)
    s.screensize(800,600)
    list_of_times = ["8:00am", "9:00am", "10:00am", "11:00am", "12:00am","1:00pm", "2:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm"]

    t.penup()
    t.goto(-400,300)
    for i in range(0,800,100):
        t.goto(-400 + i,300)
        t.pendown()
        t.goto(-400 + i,-300)
        t.penup()

    t.penup()
    days = ["Weekdays/Time","Sunday", "Monday","Tueday","Wednesday","Thursday","Friday","Saturday"]
    count = 0
    for i in range(0, 800, 100):
        t.goto(-350 + i, 285)
        t.write(days[count], align="center")
        count+=1
    for i in range(0,600,50):
        t.goto(-400,300 - i)
        t.pendown()
        t.goto(400,300- i)
        t.penup()

    t.goto(-400,-300)
    t.pendown()
    t.goto(400,-300)
    t.goto(400,300)
    t.penup()

    count = 0
    for i in range(225,-276,-50):
        t.goto(-387,i)
        t.write(f"{list_of_times[count]}",align="left", font=("Arial", 12, "normal"))
        count += 1
        t.goto(-200,250)
    color = random_color()


    time_dictionary = {
        "8:00": 250,
        "9:00": 200,
        "10:00": 150,
        "11:00": 100,
        "12:00": 50,
        "1:00": 0,
        "2:00": -50,
        "3:00": -100,
        "4:00": -150,
        "5:00": -200,
        "6:00": -250
    }



    for i in range(len(schedule)):
        color = random_color()
        fontsize = 9
        if len(schedule[i][0]) > 16:
            fontsize -= 5
        elif len(schedule[i][0]) > 24:
            fontsize -= 7
        elif len(schedule[i][0]) > 24:
            fontsize = 1
        if schedule[i][5] == "Monday":
            for j in range(-200,300,200):
                draw_class_monday(j,time_dictionary[schedule[i][4]],color)
                t.goto(j + 5, time_dictionary[schedule[i][4]] - 15)
                t.write(f"{schedule[i][0]}", align="left", font=("Arial", fontsize, "normal"))

        elif schedule[i][5] == "Tuesday":
            for j in range(-100, 101, 200):
                draw_class_tuesday(j, time_dictionary[schedule[i][4]], color)
                t.goto(j + 5,time_dictionary[schedule[i][4]]-15)
                t.write(f"{schedule[i][0]}", align="left", font=("Arial", fontsize, "normal"),)
        elif schedule[i][5] == "Thursday":
            draw_class_monday(100, time_dictionary[schedule[i][4]], color)
            t.goto(105, time_dictionary[schedule[i][4]] - 15)
            t.write(f"{schedule[i][0]}", align="left", font=("Arial", fontsize, "normal"))

    turtle.addshape("back.gif")
    back = turtle.Turtle()
    back.shape("back.gif")
    back.color("white")
    back.shapesize()
    back.penup()
    back.goto(350, -275)
    back.shapesize(stretch_wid=2.4,stretch_len=4.9)
    back.onclick(welcome_screen)


    turtle.tracer(True)

# Creates the monday sized classes
def draw_class_monday(x,y,color):

    t.fillcolor(color)
    t.begin_fill()
    t.goto(x, y)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.penup()
    t.end_fill()

# Creats the block for the larger tuesday classes
def draw_class_tuesday(x, y, color):
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x, y)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.penup()
    t.end_fill()


# The buttons associated with the onclick for the main buttons
def button1(x,y):
    read_file("1")
def button2(x,y):
    read_file("2")
def button3(x,y):
    read_file("3")
def button4(x,y):
    read_file("4")
def button5(x,y):
    read_file("5")
def button6(x,y):
    read_file("6")
def button7(x,y):
    read_file("7")
def button8(x,y):
    read_file("8")

# Creates the welcome screen
def welcome_screen(x,y):
    s.clearscreen()


    s.setup(810, 610)
    s.screensize(800, 600)
    t.penup()
    t.goto(0, 200)
    t.write("Welcome To The CS Course Planner!",align="center", font=("Arial", 30, "normal"))



    turtle.addshape("Semester1.gif")
    semester_1_button = turtle.Turtle()
    semester_1_button.penup()
    semester_1_button.goto(-100, 0)
    semester_1_button.shape("Semester1.gif")
    semester_1_button.onclick(button1)

    turtle.addshape("Semester2.gif")
    semester_2_button = turtle.Turtle()
    semester_2_button.penup()
    semester_2_button.goto(100, 0)
    semester_2_button.shape("Semester2.gif")
    semester_2_button.onclick(button2)

    turtle.addshape("Semester3.gif")
    semester_3_button = turtle.Turtle()
    semester_3_button.penup()
    semester_3_button.goto(-100, -50)
    semester_3_button.shape("Semester3.gif")
    semester_3_button.onclick(button3)

    turtle.addshape("Semester4.gif")
    semester_4_button = turtle.Turtle()
    semester_4_button.penup()
    semester_4_button.goto(100, -50)
    semester_4_button.shape("Semester4.gif")
    semester_4_button.onclick(button4)

    turtle.addshape("Semester5.gif")
    semester_5_button = turtle.Turtle()
    semester_5_button.penup()
    semester_5_button.goto(-100, -100)
    semester_5_button.shape("Semester5.gif")
    semester_5_button.onclick(button5)

    turtle.addshape("Semester6.gif")
    semester_6_button = turtle.Turtle()
    semester_6_button.penup()
    semester_6_button.goto(100, -100)
    semester_6_button.shape("Semester6.gif")
    semester_6_button.onclick(button6)

    turtle.addshape("Semester7.gif")
    semester_7_button = turtle.Turtle()
    semester_7_button.penup()
    semester_7_button.goto(-100, -150)
    semester_7_button.shape("Semester7.gif")
    semester_7_button.onclick(button7)

    turtle.addshape("Semester8.gif")
    semester_8_button = turtle.Turtle()
    semester_8_button.penup()
    semester_8_button.goto(100, -150)
    semester_8_button.shape("Semester8.gif")
    semester_8_button.onclick(button8)

    turtle.addshape("exit.gif")
    exit_button = turtle.Turtle()
    exit_button.shape("exit.gif")
    exit_button.penup()
    exit_button.goto(0,-225)
    exit_button.onclick(exit)

def exit(x,y):
    turtle.bye()

welcome_screen("","")


turtle.tracer(True)
turtle.mainloop()

