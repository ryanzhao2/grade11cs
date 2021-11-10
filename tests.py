import time
import sys
#first text
print('Hey.', end="")
#flush stdout
sys.stdout.flush()
#wait a second
time.sleep(1)
#write a carriage return and new text
print('\rHow is your day?')
