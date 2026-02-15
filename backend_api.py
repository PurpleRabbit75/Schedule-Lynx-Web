### Schedule Lynx App ###

#------------------------------ IMPORTS ------------------------------#

from ImageLib2 import *
import time
import os
import json
import streamlit as st



#------------------------------ GLOBAL VARIABLES [USER PREFERENCES FROM config.json] ------------------------------#    

# These colors were selected from the standard CSS Colors, also called Web Colors. Rearranging the order of these will rearrange the order of the colors on the output image
with open('config/colors.json', 'r') as file:
    COLORS = [tuple(color) for color in list(json.load(file).values())]

with open('config/config.json', 'r') as file:
    config = json.load(file)

FONT_SIZE = config['font_size'] # defaults to 13
START_TIME = config['start_time'] # defaults to 7:00 AM
END_TIME = config['end_time'] # defaults to 10:00 PM
SPACER_PIXELS = config['spacer_pixels'] # Number of pixels to be inserted at the top of the sheet; added directly to the y position from the top of all blocks.
SCHEDULE_COLUMN_WIDTH = config['schedule_column_width'] # Width in pixels of each day's schedule column
TIME_COLUMN_WIDTH = config['time_column_width'] # defaults to 73, which is 75 minus a 2-pixel border
ROW_HEIGHT = config['row_height'] # Height in pixels of each time row
# DATA_DIRECTORY = config['data_directory'] # Directory where schedule JSON files are stored
OUTPUT_PATH = config['output_path'] # Directory where the program outputs the file



#------------------------------ GLOBAL VARIABLES [PROGRAM USE ONLY - DO NOT EDIT] ------------------------------# 

_APPLICATION_START_TIME = time.time()

def generate_times(start_time, end_time):
    times = []
    start_min = start_time[0] * 60 + start_time[1]
    end_min = end_time[0] * 60 + end_time[1]
    current = start_min
    while current <= end_min:
        hour = current // 60
        minute = current % 60
        if hour == 0:
            display_hour = 12
            ampm = "AM"
        elif hour < 12:
            display_hour = hour
            ampm = "AM"
        elif hour == 12:
            display_hour = 12
            ampm = "PM"
        else:
            display_hour = hour - 12
            ampm = "PM"
        time_str = f"{display_hour}:{minute:02d} {ampm}"
        times.append(time_str)
        current += 15
    return times

TIMES = generate_times(START_TIME, END_TIME)
WIDTH =  5 * (SCHEDULE_COLUMN_WIDTH + TIME_COLUMN_WIDTH) # 5 days
HEIGHT = (len(TIMES) + 1) * ROW_HEIGHT + SPACER_PIXELS # (len(TIMES) + 1) = number of rows 
_GRID = [[(255, 255, 255) for _ in range(HEIGHT)] for _ in range(WIDTH)]
_NAMES = [] # List of tuples in the form (name, (R, G, B))



#------------------------------ FUNCTIONS ------------------------------#

def add_name(name:str):
    _NAMES.append((name, COLORS[len(_NAMES)]))



def add_time_block(name:str, startTime:list[int], stopTime:list[int], daysStr:str):
    "Add a time block to the schedule for a given name, start and stop times, and days string."
    global _NAMES

    def define_block(startTime:list[int], stopTime:list[int], columnNo:int, weekday:int):
        "Define the coordinates of a time block given start and stop times, column number, and weekday."

        def time_to_y(time:list[int]):
            "Convert a time in [hours, minutes] format to a y coordinate on the image _GRID."
            global SPACER_PIXELS, TIME_COLUMN_WIDTH
            hours, minutes = time  
            hours -= START_TIME[0]      
            minutes += 60 * hours
            minutes -= START_TIME[1]
            y = minutes 
            y = int(y)
            y = y + SPACER_PIXELS
            return y

        startY = time_to_y(startTime)
        stopY = time_to_y(stopTime)

        startX = SCHEDULE_COLUMN_WIDTH/len(_NAMES) * columnNo + TIME_COLUMN_WIDTH * (weekday+1) + SCHEDULE_COLUMN_WIDTH*weekday
        stopX = startX + SCHEDULE_COLUMN_WIDTH/len(_NAMES)

        return [(startX, startY), (stopX, stopY)]


    def draw_block(coordinates, rgb):
        "Draw a block on the _GRID given coordinates and an RGB color."
        global _GRID
        xi, xf, yi, yf = coordinates[0][0], coordinates[1][0], coordinates[0][1], coordinates[1][1]
        
        for i in range(len(_GRID)):
            for j in range(len(_GRID[0])):
                if (i >= xi and i <= xf):
                    if (j >= yi and j <= yf):
                        _GRID[i][j] = rgb



# The days of the working week are "MTWRF"
    def dayStr2list(string:str):
        "Take a string of format 'MTWRF' and convert it to a list of mixed numbers equal to their index + 1 (if the day is present in the string) and else = False."
        output = [0] * 5 # Changed from "False" to 0
        for i, day in enumerate('MTWRF'):
            if day in string:
                output[i] = i + 1
        return output
    

    daysList = dayStr2list(daysStr)

    for i in range(0, len(_NAMES)):
        for j in range(0,5):
            if (name == _NAMES[i][0]):
                if(daysList[j] != False):
                    draw_block(define_block(startTime, stopTime, i, daysList[j]-1), _NAMES[i][1])

    

def write_to_image(data):
    "Write a single data file's information to the image _GRID. Data is in the form [name, [startTime, stopTime, daysStr, description], ...]"
    name = data[0]
    print("Data =", data)
    for i in range(1, len(data)):
        add_time_block(name, data[i][0], data[i][1], data[i][2])


def import_schedule_JSONs():
    schedules_list = st.session_state['user_data_array']
    for i in schedules_list:
        add_name(i[0])
    return schedules_list


def draw_lines_and_text():


    def draw_day_lines():
        global TIME_COLUMN_WIDTH
        for i in range(5):
            colNo = TIME_COLUMN_WIDTH*i + 400*i
            for j in range(len(_GRID)-4):
                for k in range(len(_GRID[0])):
                    if (j == colNo):
                        _GRID[j][k] = (0, 0, 0)
                        _GRID[j+1][k] = (0, 0, 0)
                        _GRID[j+2][k] = (0, 0, 0)
                        _GRID[j+3][k] = (0, 0, 0)
                        _GRID[j+4][k] = (0, 0, 0)
            colNo = TIME_COLUMN_WIDTH*(i+1) + 400*i
            for j in range(len(_GRID)-4):
                for k in range(len(_GRID[0])):
                    if (j == colNo):
                        _GRID[j][k] = (0, 0, 0)
                        _GRID[j+1][k] = (0, 0, 0)
                        _GRID[j+2][k] = (0, 0, 0)
                        _GRID[j+3][k] = (0, 0, 0)
                        _GRID[j+4][k] = (0, 0, 0)


    def draw_horizontal_lines():
        global SPACER_PIXELS
        for i in range(len(TIMES) + int(SPACER_PIXELS/15)):
            i *= ROW_HEIGHT
            if (i % 2 == 0):
                for j in range(WIDTH):
                    _GRID[j][i] = (0, 0, 0)
        

    def write_name_text(_NAMES, img):
        global TIME_COLUMN_WIDTH
        for day in range(5):
            for i in range(len(_NAMES)):
                writeText(img, _NAMES[i][0], (TIME_COLUMN_WIDTH*(day+1) + 10 + 400/len(_NAMES)*i + 400*day, 1+15), fontSize = FONT_SIZE)    
    

    def write_weekday_text(img):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for i in range(len(days)):
            writeText(img, days[i], ((SCHEDULE_COLUMN_WIDTH + TIME_COLUMN_WIDTH + 10 )/2 + SCHEDULE_COLUMN_WIDTH*i + TIME_COLUMN_WIDTH*i, 1), fontSize = FONT_SIZE)
    

    def write_time_text(img, xPos):
        global WIDTH, TIMES, SPACER_PIXELS
        for i in range(len(TIMES)):
            if (i % 2 == 0):
                writeText(img, TIMES[i], (xPos + 10, i * ROW_HEIGHT + SPACER_PIXELS + ROW_HEIGHT/2), fontSize = FONT_SIZE)


    print("Elapsed time:", time.time()- _APPLICATION_START_TIME, "s")       
    print("Writing grid into image")
    draw_day_lines()
    draw_horizontal_lines()
    print("Elapsed time:", time.time()- _APPLICATION_START_TIME, "s")
    print("Completing the formatting...")
    img = toImage(_GRID)
    for i in range(5):
        write_time_text(img, (SCHEDULE_COLUMN_WIDTH + TIME_COLUMN_WIDTH) * i)
    write_name_text(_NAMES, img)
    write_weekday_text(img)
    return img



def main():

    schedules = import_schedule_JSONs()
    for i in schedules:
        write_to_image(i)
    img = draw_lines_and_text()
    # print("Elapsed time:", time.time() - _APPLICATION_START_TIME, "s")
    return img, WIDTH

