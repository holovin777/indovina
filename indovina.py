from getpass import getpass
play="si"
while play=="si":
    s = 10
    x = 11
    while s < 0 or s > 9:
        try:
            s=int(getpass("Numero segreto (0-9): "))
        except:
            print("Deve essere un numero!")
    while s!=x:
        try:
            x=int(input("Numero indovinato (0-9): "))
        except:
            print("Deve essere un numero!")
        if s!=x:
            print("No, prova ancora")
        else:
            print("Congratulazioni!")
    play=input("Vuoi giocare ancora? ").lower()
