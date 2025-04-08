import time
import datetime
import pygame #stores alarm sound


def set_alarm(alarm_time): #shows time in military time
    print(f"Alarm set for {alarm_time}")
    sound_file = "my-sound.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")   #module.class.method.method2
        #returns curr datetime, and then method2 allows formatting that
        print(current_time)
        if current_time == alarm_time:
            print("Wake up!")
            is_running = False
            pygame.mixer.init() #package.module.method- calls a constructor
            pygame.mixer.music.load(sound_file)     #package.module.module.method -loads the file
            pygame.mixer.music.play()   #package.module.module.method - plays the music.
            while pygame.mixer.music.get_busy(): # while the sound file is "busy" (playing)
                time.sleep(1) #While music plays this checks if it's still running every second.
                #Once music stops this will detect it and throw you out of the loop.

        time.sleep(1) # halts execution of program for a specified time (in seconds). Once that time passes - sys will throw you out of the loop.

        #is_running = False adding this in a loop helps prevent infinite loops during testing.
        # #Good for just minor checks you might want to perform in the loop

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)