class stack:
    def __init__(self):
        self.stack=[]
    def push(self,val):
        self.stack.append(val)
        return "value added"
    def pop(self):
        if self.isempty:
            return "empty_stack"
        else:
            self.stack.pop()
            return "value removed"
    def isempty(self):
        if len(self.stack)==0:
            return "is empty"
        else:
            return "no empty"
    def peek (self):
        if len(self.stack)==0:
            return "empty_stack"
        else:
             return self.stack[-1]
    def view(self):
        return self.stack
    def menu(self):
        while True:
            print(" 1 push \n 2.pop \n 3.isempty \n 4.top \n 5.view ")
            option=int(input("enter option :"))
            match option:
                case 1:
                        print(obj.push(int(input("enter a number :"))))
                case 2:
                        print(obj.pop())
                case 3:
                        print(obj.isempty())
                case 4:
                        print(obj.peek())
                case 5:
                        print(obj.view())
                case _:
                      print("Thank you")
                      break
obj=stack()
obj.menu()