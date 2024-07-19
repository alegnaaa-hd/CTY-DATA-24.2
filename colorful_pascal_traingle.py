

RED = '\033[31m'
GREEN = '\033[32m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
LIGHTGREY = '\033[37m'
DARKGREY = '\033[90m'
LIGHTRED = '\033[91m'
LIGHTGREEN = '\033[92m'
YELLOW = '\033[93m'
LIGHTBLUE = '\033[94m'
PINK = '\033[95m'
LIGHTCYAN = '\033[96m'
RESET = '\033[0m'

print(PINK)
print("      *        ")
print("     ***       ")
print("    *****      ")
print("   *******     ")
print(RESET)


n = int(input("Enter size of triangle: "))
i = 0
stars="*"
for _ in range(2*n):
    stars += '*'

#print("current status of stars: ", stars)
print(LIGHTBLUE)
final_print = ""
lastline = str(stars) 
k = 0
l = len(stars)-1
while k<n :
    topline = str(lastline)
    s_t = list(topline)
    #print("current array of stars: ", s_t)
    s_t[k] = ' '
    s_t[l] = ' '
    
    # print("current array of stars: ", s_t)
    topline = str(''.join(s_t))
    final_print = final_print +'\n' + topline  
    lastline = str(topline)
    i += 1
    k += 1
    l -= 1

print(final_print)

print(RESET)