# Healthy Programmer Exercise 7 CWH Python Tut
"""
9 am to 5 pm office time
water - water.mp3 ---every 40 mins  ----log drinking time in txt file
eyes - eyes.mp3  ----every 30 mins ---- log eyes exercise time
physical activity - physical.mp3 ----- every 45 mins ---log exercise time
"""
# Rule
# Pygame module to play audio


from pygame import mixer
from time import time
from datetime import datetime
from time import strftime

def musiconloop(*audio):
    mixer.init()
    mixer.music.load(audio[0])
    mixer.music.play()
    while True:
        a = input(f"Press {audio[1]} if you are done: ")
        if a == audio[1]:
            mixer.music.stop()
            break

def log_now(msg):
    with open("log.txt", "a") as f:
        f.write(f"{msg} at {datetime.now()}\n")

if __name__ == "__main__":

    init_water = time()
    init_eyes = time()
    init_ex = time()
    water_secs = 40 * 60  # 40 minutes
    eyes_secs = 30 * 60   # 30 minutes
    ex_secs = 45 * 60     # 45 minutes

    office = strftime('%H:%M:%S') > '09:00:00' and strftime('%H:%M:%S') < '17:00:01'
    while(office):

        if time() - init_water > water_secs:
            print("Time to drink water")
            musiconloop("water.mp3", "1")
            init_water = time()
            log_now("Drank water")

        if time() - init_eyes > eyes_secs:
            print("Time for eyes exercise")
            musiconloop("eyes.mp3", "2")
            init_eyes = time()
            log_now("Eyes relaxed")

        if time() - init_ex > ex_secs:
            print("Time for physical activity")
            musiconloop("physical.mp3", "3")
            init_ex = time()
            log_now("Physical activity")

    print("Office time over!!! You can go home!!!!")
