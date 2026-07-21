stact =[ ]

def push() :
    element = input("Enter element to push: ")
    stact.append(element)
    print(f"{element} pushed to stack.")

def pop_elemnt():
        if not stact:
            print("stack is empty")
        else:
            e = stact.pop()    
            print(f"{e} popped from stack.")
    
def peek():
        if not stact:
            print("stack is empty")
        else:
            print(f"Top element: {stact[-1]}")
    
while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            push()
        elif choice == '2':
            pop_elemnt()
        elif choice == '3':
            peek()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")