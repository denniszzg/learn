count = 0
def hanoi(n, start, end, mid):
    global count
    if n == 1:
        count += 1
        print("{}:{}->{}".format(count,start,end))
        
    else:
        hanoi(n-1, start, mid, end)
        hanoi(1, start, end, mid)
        hanoi(n-1, mid, end, start)
        
def main():
    n = eval(input("pls input n= "))
    hanoi(n, 'A', 'C', 'B')

main()
