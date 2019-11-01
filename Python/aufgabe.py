#Split String
line = ' Water : 9.876 : at 20°C'

#print(line.split(':'));

name, value, desc = line.split(':')
#rint(value);

#Open File
f=open('phoentic.dat', encoding='utf-8')
#print(f.read())
f.close()

#Subprocess, Commands on OS
import subprocess
#ret=subprocess.call(["ping","-c1","8.8.8.8"])

#Functions
number = 1234;
def reverse(number):
    """reverses the digit sequence of a number
    Args: number: the number to be reversed
    """
    s = list(str(number))[::-1]
    return ''.join(s)

print(reverse(number))

#print(reverse.__doc__)
#help(reverse)

