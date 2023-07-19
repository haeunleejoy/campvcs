def stats(list):
    print("min: " + str(min(list))) # we do not always know what is in the list and what is the minimum, so we do min(list) to figure out the minimum
    print("max: " + str(max(list)))
    print("avg: " + str(sum(list)/len(list)))
stats([1,2,3])
