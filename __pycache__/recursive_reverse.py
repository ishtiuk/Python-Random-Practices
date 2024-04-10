def recursive_reverser(inputing):
    if len(inputing) == 0:
        return inputing
    
    else:
        return recursive_reverser(inputing[1:]) + inputing[0]

print(recursive_reverser(input("enter anything to reverse: ")))