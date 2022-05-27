import keyboard
import time
import os
cols, lines = os.get_terminal_size()
max = ((cols * lines) - 160)
print("start")
playerxy = 3
timeout = 0
playerxy -= 1
player = "p"

def main():
    prin = ""
    x = playerxy
    y = 0
    while y < x:
        y += 1
        prin += "."
    prin += player
    y += 1

    x = max
    while y < x:
        y += 1
        prin += "."
    os.system("cls")
    print(prin)
main()
while 1==1:
    if keyboard.is_pressed('a') and not playerxy - 1 == -1:
            player = "q"
            playerxy -= 1
            main()
    if keyboard.is_pressed('d') and not playerxy + 1 == max:
        player = "p"
        playerxy += 1
        main()
    if keyboard.is_pressed("s") and not playerxy + cols > max:
        playerxy += cols
        main()
    if keyboard.is_pressed("w") and not playerxy - cols < 0:
        playerxy -= cols
        main()