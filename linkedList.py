class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.start = None
    def insertLast(self, value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next !=None:
                temp = temp.next
            temp.next = newNode
    def traverseList(self):
        if self.start == None:
            print("list is empty")
        else:
            temp = self.start
            while temp != None:
                print(temp.value, end=' ')
                temp = temp.next
    def deleteFirst(self):
        if self.start == None:
            print("list is empty")
        else:
            self.start = self.start.next
    def deleteLast(self):
        if self.start == None:
            print("list is empty")
        else:
            temp = self.start
            while temp.next !=None:
                prev = temp
                temp = temp.next
            prev.next = None
    def insertFirst(self, value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            self.start = newNode
            self.start.next = temp
    def insertSpecific(self, value, position):
        newNode = Node(value)
        temp = self.start
        currPosition = 0

        while temp:
            currPosition += 1
            prev = temp
            temp = temp.next
            if currPosition == position:
                prev.next = newNode
                newNode.next = temp
                break

    def delSpecific(self, position):
        # newNode = Node(value)
        temp = self.start
        currPosition = 0
        while temp:
            currPosition += 1
            prev = temp
            temp = temp.next
            if currPosition == position:
                prev.next = temp.next
                break
    def delSpecVal(self, value):
        temp = self.start
        while temp:
            prev = temp
            temp = temp.next
            if temp.value == value:
                prev.next = temp.next
                break





lnList = LinkedList()
lnList.insertLast(10)
lnList.insertLast(20)
lnList.insertLast(30)
lnList.insertLast(40)
lnList.insertLast(50)
lnList.traverseList()
print()
lnList.deleteFirst()
lnList.traverseList()
print()
lnList.deleteLast()
lnList.traverseList()
print()
lnList.insertFirst(100)
lnList.traverseList()
print()
lnList.insertSpecific(60, 2)
lnList.traverseList()
print()
lnList.delSpecific(2)
lnList.traverseList()

print()
lnList.delSpecVal(30)
lnList.traverseList()

