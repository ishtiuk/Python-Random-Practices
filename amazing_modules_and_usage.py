import string
import random

chars = string.ascii_letters                                         # 'string.ascii_letters' to index all a - z & A - Z letters 
print('all letters:',chars)

digit_numb = string.digits                                              # 'string.digits' to index all numbers 0 - 9
print('all nums:',digit_numb)                                           # but remember that these nums are taken here as str format,
                                                                        # we have to convert them to number if needed by writting int(digit) or float(digit)

symbols = string.punctuation                                            # 'string.punctuation' to index all punctuation marks or special_sybols like : }{:\|.?!} , etc.
print('all symbols:',symbols)                                           
                                                                       


rand_num = random.randint(0, 2000)                                      # 'random.randint(0, 2000)' to index any random number for range 0 to 2000
print('random number selection:',rand_num)



rand_single_choice = random.choice(chars)                               # 'random.choice(chars)' here if we use 'choice' then it can choose a single char or str(num) or symbols from
print('random_single_char_selection_from_str_or_list:',rand_single_choice)  # any string or list , but those will be in str format


rand_multiple_or_list = random.choices(chars, k=5)                           # 'random.choices(chars)' can take multiple chars or str(num) or symbols as a list from any string or list.
print(rand_multiple_or_list)                                                 # so, here if we defined 'k=5' or any number then it will take a list of multiple num according to the ' k 'value
#                                                                             # if k = 5 then it will take 5 chars as in a list, if k = 1000 then it will take 1000 chars in a list.


                          # these all will take chars, nums, symbols as a str format.

chars = ' '.join(chars)
print(chars)
