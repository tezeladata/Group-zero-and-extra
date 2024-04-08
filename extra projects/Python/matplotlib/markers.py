import matplotlib.pyplot as plt
import numpy as np

def collatz(user_num):
    sequence = np.array([user_num])
    
    while user_num > 1:
        if user_num%2==0:
            user_num//=2
        else:
            user_num = user_num*3 +1
        sequence = np.append(sequence, user_num)

    return sequence

y_axis = np.array(collatz(user_num=int(input("Enter number: "))))
# Using fmt notation to change marker, line and color
plt.plot(y_axis, '.--k', ms=20, mec="c", mfc="g") #We can also use markersize - ms to change size of marker
# Markergecolor - mec to change color of marker edge
# Markerfacecolor - mfc to change color of inside
plt.show()

# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline


# '-'	Solid line	
# ':'	Dotted line	
# '--'	Dashed line	
# '-.'	Dashed/dotted line


# 'r'	Red	
# 'g'	Green	
# 'b'	Blue	
# 'c'	Cyan	
# 'm'	Magenta	
# 'y'	Yellow	
# 'k'	Black	
# 'w'	White