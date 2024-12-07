# Big O (1) meant constant time complexity which means the time remains constant regardless of the size of the input
def add (x,y):
    return x+y

#Big O(n) is linear time complexity which means the time is directly proportional to the size of input eg a loop

def examploop(n):
    steps = 0 
    for i in range (1, n+1):
        steps+=1
    print("when n is", n, "the steps are", steps)

# examploop(60)

# Big O (n^2) is a quadratic time complexity time taken grows quadratically with the input size eg a nested loop
def nestloop(n):
    steps=0
    for c in range (0,n):
        for j in range(0,n):
            print ("*", end=" ")
            steps +=1
        print("")
    print ("when n is ", n ,"steps are ", steps)
nestloop(3)
nestloop(4)
nestloop(5)