stack=[]

def push():
    item=int(input("enter element:"))
    stack.append(item)

def pop() :
    if len(stack)==0:
        print("stack is empty ")
    else:
        print("removed element : ",stack.pop())       

def display():
    print("stack:",stack)

while (True):
    print("\n1.push 2.pop 3.display 4.exit")
    print("enter your choice:")
    ch=int(input())
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        break
    else :
        print('invalid choice')

