import random
import string
import time
import pyperclip as cboard
 
wert = "y"

while wert == "y":
    cboard.copy("")
    try:
        eingabe1 = int(input("Anzahl der der Zeichen: "))

        output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(eingabe1))


        print(output_string)
        cboard.copy(output_string)
        print("added to clipboard!")
        
        # if u want u can put here ur copy to clipboard time
        # time.sleep(10)
        # it will fill the clipboard with nothing
        # cboard.copy("")
        
        time.sleep(1)
        wert = input("Again (y/n): ")

    except Exception as e:
        print("Something went wrong! (1)")
        print(e)
        

if wert != "y":
    print("Exit (0)")
