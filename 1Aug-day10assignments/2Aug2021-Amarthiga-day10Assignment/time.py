import time

# %H - Hours
# %M - Minutes 
# %S - Seconds
# %h -month (August)
# %m -month (08)

current_time=time.localtime()
print(current_time)
current_clock_time=time.strftime("%h:%m:%S",current_time)
print(current_clock_time)
