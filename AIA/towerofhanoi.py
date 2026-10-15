def  towerofhanoi(n, source, destination, auxilary):
    if n == 1:
        print("move disk 1 from rod", source, "to rod", destination)
        return
    towerofhanoi(n-1, source, auxilary, destination)
    print("Move disk", n, "from rod", source, "to rod", destination)
    towerofhanoi(n-1, auxilary, destination, source)




n=4

towerofhanoi(n, 'A', 'B', 'C')