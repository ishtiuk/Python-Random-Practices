import time

txt = '''It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.'''
inp = input('Enter "yes" when you are ready.. ').lower()

if inp == 'yes':
    t0 = time.time()
    text = input('''It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.
    :--> ''')
    t1 = time.time()

time_taken = t1 - t0
print(time_taken)

wpm = len(txt) / time_taken
print(wpm)