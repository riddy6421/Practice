import turtle as b  # import turtle library as variable b


def draw_hand(short_h, long_h):  # clock drawing function
    t = b.Pen()  # initializes t to pen object
    t.shape("circle")  # draw circle
    t.color("green")  # select green color green
    t.stamp()  # draw object
    angle = 6  # set angle to 6 for representing each minute
    for i in range(60):  # loop through the clock
        if i == short_h:  # draw short hand
            t.penup()
            t.pendown()
            t.forward(38)
            t.penup()
            t.forward(12)
            t.pendown()
            t.forward(25)
            t.penup()
            t.forward(15)
        elif i == long_h:  # draw long hand
            t.penup()
            t.pendown()
            t.forward(75)
            t.penup()
            t.forward(15)
        else:  # draw every other hand
            t.penup()
            t.forward(50)
            t.pendown()
            t.forward(25)
            t.penup()
            t.forward(15)
        if i % 5 == 0:  # draw a circle every 5 minute
            t.stamp()
        t.home()
        t.right(angle)
        angle = angle + 6  # update angle
        if i == 59:
            t.reset()  # on the last tick reset the clock


def readFile(filename):  # reading file function
    hrvalid = None  # boolean to check if hour hand is valid
    draw_min = 0  # variable that gets hour hand
    draw_hr = 0  # variable that gets minute hand
    file = open(filename, "r+")  # open file

    for line in file.readlines():  # iterate through each line in the file
        values = line.split(":")  # split line into hr and minute with delimiter ":"

        for i in range(len(values)):  # iterate through the length of each line
            if i == 0:
                if 0 <= int(values[i]) < 24:  # check if hr is in range, and set hrvalid
                    hrvalid = True
                else:
                    hrvalid = False
            elif i == 1:
                if 0 <= int(values[i]) < 60:  # check if minute is in range and set minvalid
                    minvalid = True
                else:
                    minvalid = False
                if hrvalid and minvalid:  # check if both are valid
                    if 12 >= int(values[0]) >= 0:  # check if the hr is between 0 and 12
                        if int(values[1]) == 0 and int(values[0]) == 0:
                            angle = ((12 / 12) * 360)
                            if angle > 180:
                                angle = 360 - angle
                            print("Angle between %d and %d is: %d degrees" % (int(values[0]), int(values[1]), angle))
                            draw_hr = (int(values[0]) + (45 + (int(values[0]) * 4)))
                            draw_min = int(values[1]) + 45
                            if draw_hr >= 60:
                                draw_hr = draw_hr - 60 # update hr
                            if draw_min >= 60:
                                draw_min = draw_min - 60 # update min

                        elif int(values[1]) == 0 and int(values[0]) > 0:
                            angle = ((int(values[0]) / 12) * 360)
                            if angle > 180:
                                angle = 360 - angle
                            print("Angle between %d and %d is: %d degrees" % (int(values[0]), int(values[1]), angle))
                            draw_hr = (int(values[0]) + (45 + (int(values[0]) * 4)))
                            draw_min = int(values[1]) + 45
                            if draw_hr >= 60:
                                draw_hr = draw_hr - 60 # update hr
                            if draw_min >= 60:
                                draw_min = draw_min - 60 # update min

                        elif int(values[1]) > 0 and int(values[0]) > 0:
                            angle = ((int(values[0]) / 12) * 360)
                            angle = abs(angle - int(values[1]) * 6)
                            print("Angle between %d and %d is: %d degrees" % (int(values[0]), int(values[1]), angle))
                            draw_hr = (int(values[0]) + (45 + (int(values[0]) * 4)))
                            draw_min = int(values[1]) + 45
                            if draw_hr >= 60:
                                draw_hr = draw_hr - 60 # update hr
                            if draw_min >= 60:
                                draw_min = draw_min - 60 # update min

                    elif 12 < int(values[0]) < 24:  # check if between 12 and 24
                        time = int(values[0]) - 12
                        angle2 = ((time / 12) * 360)
                        angle2 = abs(angle2 - int(values[1]) * 6)
                        if angle2 > 180:
                            angle2 = 360 - angle2
                        print("Angle between %d and %d is: %d degrees" % (int(values[0]), int(values[1]), angle2))
                        draw_hr = (time + (45 + (time * 4)))
                        draw_min = int(values[1]) + 45
                        if draw_hr >= 60:
                            draw_hr = draw_hr - 60 # update hr
                        if draw_min >= 60:
                            draw_min = draw_min - 60 # update min
                    draw_hand(draw_hr, draw_min) # draw the clock based on the updated hr and minute

                else:
                    print("ERROR") # if not valid prints error
            continue


readFile("file.txt") # call readfile
