import time

def countdown(t):
  while t:
    mins, secs = divmod(t, 60)#returns a tuple of the quotient and the remainder
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end='\r')
    time.sleep(1)#1 second
    t -= 1
  
  print("time is up!")

t = int(input('Enter time in seconds: '))
countdown(t)