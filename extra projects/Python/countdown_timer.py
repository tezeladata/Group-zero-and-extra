import time

def countdown(user_seconds):

    while user_seconds:
        mins, secs = divmod(user_seconds, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)

        print(timer, end="\r")

        time.sleep(1)

        user_seconds -= 1

    print("Timer has finished")    

countdown(user_seconds=int(input("Enter the time in seconds: ")))