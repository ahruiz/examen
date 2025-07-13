from colorama import Fore
import os

os.system("clear")

print(f"{Fore.YELLOW}Justificando items de lista de listas: rjust, center y ljust.....{Fore.WHITE}")

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]


def capt():
    x = 0
    just = 10
    for _ in tableData:
        if x == 0:
            datos = (tableData[x][y]).rjust(just)
            print(datos, end = " ")
            x += 1        
        if x == 1:
            datos = (tableData[x][y]).center(just)
            print(f"{Fore.YELLOW} {datos} {Fore.WHITE}", end = " ")
            x += 1        
        if x == 2:
            datos = (tableData[x][y]).ljust(just)
            print(datos, end = " ")
            x += 1        
    just += 10
    print()
    
y = 0
while y <= 3:
    capt()
    y += 1