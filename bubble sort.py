def bubble_sort():
    items = [23, 41, 11, 17, 34, 56]
    print (items)
    n = len(items)-1
    
    for x in range (0, n):
        for index in range(0, n):
            if (items[index] > items [index + 1]):
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp

    print(items)

def while_swapped():
    items = [23, 41, 11, 17, 34, 56]
    print (items)
    n = len(items)-1
    swapped = True
    
    while(swapped):
        swapped = False
        for index in range(0, n):
            if (items[index] > items [index + 1]):
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp
                swapped = True
       
    print(items)
def while_swapped2():
    items = [23, 41, 11, 17, 34, 56]
    print (items)
    n = len(items)-1
    swapped = True
    
    while swapped and n> 0:
        swapped = False
        for index in range(0, n):
            if (items[index] > items [index + 1]):
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp
                
                swapped = True
                
        n = n -1
    print(items)
def size_list():
    import random
    y = 10
    items = [random.randint(0,100) for x in range(y)]
    print (items)
    n = len(items)-1
    swapped = True
    
    while swapped and n> 0:
        swapped = False
        for index in range(0, n):
            if (items[index] > items [index + 1]):
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp
                
                swapped = True
                
        n = n -1
    print(items)
