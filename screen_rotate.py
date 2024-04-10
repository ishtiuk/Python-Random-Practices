import rotatescreen
import time

scree = rotatescreen.get_primary_display()

for i in range(4):
    time.sleep(2)
    print(i)
    scree.rotate_to(i * 90 % 360)