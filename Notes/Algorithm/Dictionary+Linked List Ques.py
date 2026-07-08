# '''
# A cricket coach has the scores of 15 players.

# Requirements
#     Accept scores of all players.
#     Display the original list.
#     Sort the scores using Bubble Sort.
#     Display the sorted scores.
#     Ask the coach to enter a player's score.
#     Search for the score using Binary Search.
#     Display the player's rank based on the sorted list.
#     Also display:
#         Highest score
#         Lowest score
#         Total number of players
# '''


# Approach:

# 1st Step: To accept the scores we have to take user input.
# 2nd Step: To Display the original List we have to make a (Linked List-> head, node and reference)
#           And then we insert the data using Insertion.
# 3rd Step: To Sort the scores we have to use Bubble Sort(as mentioned in question and also bubble sort works on descending order).
# 4th Step: To Display the sorted score we have to New.List
# 5th Step: To ask the coach to enter a player's rank we have to take user input again.
# 6th Step: We have to use Binary Search(as mentioned in question)
# 7th Step: We have to to use Dictionary data structure here because we have 2 values i.e Score as well as Rank.
# 8th Step: We have to use Indexing instead of using Dictionary onlt because of space complexity.
#           The space complexity of Indexing is more than using Dictionary only. 


# Code:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def bubble_sort(self):
        if self.head is None:
            return

        swapped = True

        while swapped:
            swapped = False
            temp = self.head

            while temp.next:
                if temp.data > temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data
                    swapped = True
                temp = temp.next

    def to_list(self):
        arr = []
        temp = self.head

        while temp:
            arr.append(temp.data)
            temp = temp.next

        return arr


ll = LinkedList()

print("Enter scores of 15 players")

for i in range(15):
    score = int(input(f"Player {i+1}: "))
    ll.insert(score)

print("\nOriginal Scores:")
ll.display()

ll.bubble_sort()

print("\nSorted Scores:")
ll.display()

scores = ll.to_list()

key = int(input("\nEnter player's score to search: "))

low = 0
high = len(scores) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if scores[mid] == key:
        found = True
        break
    elif scores[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found:
    rank = len(scores) - mid
    print("Score Found")
    print("Rank:", rank)
else:
    print("Score Not Found")

print("Highest Score:", scores[-1])
print("Lowest Score:", scores[0])
print("Total Players:", len(scores))


