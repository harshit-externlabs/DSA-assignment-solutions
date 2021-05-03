class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):  
        self.head = None
  
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
        print("After inserting",data,", nodes available in LL: ")
        self.printLL()

    def delete(self):
        if(self.head):
            if(self.head.next==None):
                self.head=None
                print("LL emptied")
            else:
                current = self.head
                while(current.next.next):
                    current=current.next
                lastnode=current.next
                current.next=None
                lastnode=None
                print("After deleting, nodes available in LL:")
                self.printLL()
        else:
            print("No nodes to delete")
        
    def countnodes(self):
        c=0
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
                c+=1
            return c+1
        else:
            return 0

    def insert_pos(self,data,pos):
        count=self.countnodes()
        if(self.head):
            if(pos>count+1):
                print("Only",count,"nodes available. Cannot insert node at position",pos)
            elif(pos==count+1):
                print("The given position is equal to number of nodes+1. Thus, inserting node at last")
                self.insert(data)
            else:
                newNode=Node(data)
                if(pos<=0):
                    print("Position cannot be negative or zero to insert")
                elif(pos==1):
                    newNode.next=self.head
                    self.head=newNode
                    print("After inserting",data,"at position",pos,", nodes available in LL: ")
                    self.printLL()
                else:
                    c=1
                    current=self.head
                    while(c<pos-1):
                        c+=1
                        current=current.next
                    demo=current.next
                    current.next=newNode
                    newNode.next=demo
                    print("After inserting",data,"at position",pos,", nodes available in LL: ")
                    self.printLL()
        else:
            print("No nodes available. Cannot insert node at position",pos)
                
    def delete_pos(self,pos):
        count=self.countnodes()
        if(self.head):
            if(pos<=0):
                print("Cannot have -ve or 0 position to delete")
            elif(pos>count):
                print("Only",count,"nodes available. Cannot delete node at position",pos)
            else:
                if(pos==count):
                    print("Position is equal to the number of nodes in LL. Thus, deleting last node")
                    self.delete()
                elif(pos==1):
                    current=self.head
                    self.head=self.head.next
                    current = None
                    print("After deletion from position",pos,", nodes available in LL:")
                    self.printLL()
                else:
                    c=1
                    current=self.head
                    while(c<pos-1):
                        c+=1
                        current=current.next
                    demo=current.next
                    current.next=current.next.next
                    demo=None
                    print("After deletion from position",pos,", nodes available in LL:")
                    self.printLL()
        else:
            print("No nodes to delete")

    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

'''Try running these commented commands too
to see every expected output'''
LL = LinkedList()
LL.delete()
LL.insert_pos(3,4)
LL.insert(1)
# LL.delete()
LL.insert(2)
LL.insert_pos(5,4)
LL.insert(3)
LL.insert(4)
LL.insert_pos(5,3)
# LL.insert_pos(9,6)
# LL.insert_pos(15,1)
# LL.insert_pos(20,8)
# LL.insert_pos(2,-4)
LL.delete_pos(5)
LL.delete()
LL.delete_pos(2)
LL.delete_pos(1)
# LL.delete_pos(-2)
# LL.delete_pos(1)
# LL.delete_pos(1)

