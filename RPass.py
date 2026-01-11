import random as r
#By Zenitharss
usable_chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789@#"
def ZrPass():
    while True:
        try:
            print("- zPASSWORD RANDOMIZER -")
            opcion = int(input("1-Randomize 0- Exit."))
            match opcion:
                case 1:
                    while True: 
                        try:
                            print("RANDOMIZER...")
                            condicion = int(input("8, 16 or custom chars password? (1, 2 or 3. 0 to exit.): "))
                            match condicion:
                                case 1:
                                    print("8 CHARACTER PASSWORD RANDOMIZER...")
                                    password = ''.join(r.choice(usable_chars)for _ in range(8)) 
                                    print(f"Your password is: {password}")
                                    break
                                case 2:
                                    print("16 CHARACTER PASSWORD RANDOMIZER...")
                                    password = ''.join(r.choice(usable_chars)for _ in range(16))
                                    print(f"Your password is: {password}")
                                    break
                                case 3:
                                    rang = int(input("INTRODUCE THE NUMBER OF CHARACTERS: "))
                                    print("CUSTOM CHARACTER PASSWORD")
                                    password =''.join(r.choice(usable_chars) for i in range(rang))
                                    print(f"Your password is: {password}")
                                    match rang:
                                        case 0:
                                            print("Error")
                                case 0: 
                                    print("EXITING...")
                                    break
                                case _:
                                    print("Error")
                        except ValueError: print("Error")
                case 0:
                    print("Exiting...")
                    break
                case _:
                    print("Error")
        except ValueError: print("Error")
        return password
ZrPass()
password = ZrPass()
print(password)