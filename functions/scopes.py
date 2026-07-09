def server_chai():
    chai_type = "masala" #local Scope
    print(f"Inside the fuction {chai_type}")

chai_type = "Lemon"

server_chai() # Global Scope

print(f"Out Side the fucntion : {chai_type}")

def chai_counter():
    chai_order = "lemon"
    def print_order():
        chai_order = "Ginger"
        print("Inner : ", chai_order)
    
    print_order()
    print("Outer : ", chai_order)

chai_order = "tulasi"

chai_counter()

print("Global : ", chai_order)