import time
from time import sleep, gmtime, strftime

def main():
    print()
    print("Press [1] to start a pomodoro")
    print()
    user_input = input("What would you like to do?: ")

    if user_input == '1':
        pomodoro()

def pomodoro():
    current_standard_time = strftime("%H:%M", gmtime(time.time()))
    end_unix_time = time.time() + 5
    end_standard_time = strftime("%H:%M", time.gmtime(end_unix_time))
    print(f"It is currently {current_standard_time}, your pomodoro will finish at {end_standard_time}")

    while time.time() <= end_unix_time:
        sleep(1)

    print()
    print("Your pomodoro has finished")
    rest()

def pomodoro_after_rest():
    print()
    print("Press [1] to start another pomodoro")
    print("Press [2] to exit")
    print()
    user_input = input("What would you like to do?: ")

    if user_input == '1':
        pomodoro()

def rest():
    print()
    print("Press [1] to start your break")
    print("Press [2] to exit")
    print()
    user_input = input("What would you like to do?: ")

    if user_input == '1':
        current_standard_time = strftime("%H:%M", gmtime(time.time()))
        end_unix_time = time.time() + 5
        end_standard_time = strftime("%H:%M", time.gmtime(end_unix_time))
        print(f"It is currently {current_standard_time}, your break will finish at {end_standard_time}")

        while time.time() <= end_unix_time:
            sleep(1)

        print()
        print("Your break has finished")
        pomodoro_after_rest()


if __name__ == '__main__':
    main()
