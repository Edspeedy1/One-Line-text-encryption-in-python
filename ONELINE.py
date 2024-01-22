'''
Eric De Leenheer
100869527
09/27/23
Encryption and Decryption in python ONE LINE!!!
'''
list(map(lambda y: ((list(map(lambda x: ((alphebet:='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 'and False) or (selection := input('Would you like to Encrypt or Decrypt?\n1. Encrypt\n2. Decrypt\n? ')) not in '12' and (a.append(1) or print('Please input either 1 or 2') or (selection:=1))) or ((stringInput := input(f'Please input the string you would like to {["encrypt", "decrypt"][int(selection) - 1]}:\n')) and (key := input(f'Please input a key to {["encrypt", "decrypt"][int(selection) - 1]} the string with:\n')[:1])) and print(f'Here is the {["encrypt", "decrypt"][int(selection) - 1]}ed string:\n', ''.join([[alphebet[((alphebet.index(x) if x in alphebet else 0) + (alphebet.index(key) if key in alphebet else 0)) % 63] for x in stringInput],[alphebet[((alphebet.index(x) if x in alphebet else 0) - (alphebet.index(key) if key in alphebet else 0)) % 63] for x in stringInput]][int(selection)-1]), sep='') or None, a := [0]))) and False) or (exitSelect:=input('would like like to run the program again? y/N\n').lower()) not in 'n' and ((b.append(0) if exitSelect=='y'else 0 if exitSelect!='n' else 1) or ((print('Exiting...')))), b:=[0]))

