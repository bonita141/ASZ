NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
        
    move(n - 1, source, target, auxiliary)
        
    target.append(source.pop())
        
    print(A, B, C, '\n')
            
    move(n - 1,  auxiliary, source, target)
              
move(NUMBER_OF_DISKS, A, B, C)