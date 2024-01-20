import time

def countdown3(hours):
  t = hours*3600
  while t:
    hours, mins = divmod(t, 3600)
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
    print(timer, end='\r')
    time.sleep(1)
    t -= 1

  print('Time is up!!')

hours = int(input('Enter time in hours: '))
countdown3(hours)

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

def countdown2(mins):
  t = mins*60
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end='\r')
    time.sleep(1)
    t -= 1
  
  print("Time is up!!")

mins = int(input("Enter time in minutes: "))
countdown2(mins)

