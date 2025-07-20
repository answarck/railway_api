from get_trains import get_trains, get_fare

trains = get_trains("ERN", "PGI", "20250720")['trainBtwnStnsList']

tl = list()

for train in trains:
    for clses in train['avlClasses']:
        print(get_fare(train['trainNumber'], "20250720", "ERN", "PGI" , clses))
    
print(tl)