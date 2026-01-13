import random as r
import pyperclip as pc
#By Zenitharss
def pcopy(password):
    while True:
        try:
            print("Do you want to copy your password to the clipboard?")
            print("1 - Yes.")
            print("2 - No.")
            copy_to_clipboard = int(input("Select an option (1 or 2): "))
            match copy_to_clipboard:
                case 1:
                    pc.copy(password)
                    print("Copied to the clipboard")
                    break
                case 2:
                    print("Returning...")
                    break
                case _:
                    print("Error.")
        except ValueError: print("Error.")
    
def rPass(usable_chars):
        while True:
            try:
                print("PASSWORD LENGTH OPTIONS:")
                print("1. 8 characters")
                print("2. 16 characters")
                print("3. Custom length")
                print("4. Back to main menu")
                condicion = int(input("Select option (1-4): "))
                match condicion:
                    case 1:
                        print("-8 CHARACTER PASSWORD RANDOMIZER...-")
                        password = ''.join(r.choice(usable_chars)for _ in range(8)) 
                        print(f"Your password is: {password}")
                        pcopy(password)
                        return password
                    case 2:
                        print("-16 CHARACTER PASSWORD RANDOMIZER...-")
                        password = ''.join(r.choice(usable_chars)for _ in range(16))
                        print(f"Your password is: {password}")
                        pcopy(password)
                        return password
                    case 3:
                        print("-CUSTOM LENGTH CHARACTER PASSWORD RANDOMIZER...-")
                        rang = int(input("Introduce the number of characters, or 0 to go back: "))
                        if rang ==0:
                            print("Returning...")
                            break
                        elif 0 < rang <= 100:
                            password =''.join(r.choice(usable_chars) for _ in range(rang))
                            print(f"Your password is: {password}")
                            pcopy(password)
                            return password
                        else: print("The number can't be a number over 100 or below 0.")
                    case 4: 
                        print("RETURNING...")
                        break
                    case _:
                        print("Error")
            except ValueError:
                print("Error.")
def ZrPass():
    usable_chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789"
    while True:
        try:
            print("- zPASSWORD RANDOMIZER -")
            print("1 - Randomize.")
            print("2 - Exit.")
            opcion = int(input("Select an option (1 or 2): "))
            match opcion:
                case 1:
                    while True: 
                        try:
                            print("-RANDOMIZER...-")
                            print("Specify the characters the password could contain?")
                            print("1 - Yes.")
                            print("2 - No.")
                            print("0 - Exit.")
                            usable_confirmation = int(input("Select an option (1, 2 or 0): "))
                            match usable_confirmation:
                                case 1:
                                    print("")
                                    usable_chars = input("Write the usable characters: ")
                                    password = rPass(usable_chars)
                                    return password
                                case 2:
                                    print("-NORMAL RANDOMIZER-")
                                    password = rPass(usable_chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789")
                                    return password
                                case 0:
                                    print("Exiting...")
                                    break
                                case _: print("Error.")
                        except ValueError: print("Error")
                case 2:
                    print("Exiting...")
                    return None
                case _:
                    print("Error")
        except ValueError: print("Error")
password = ZrPass()
print(password)
