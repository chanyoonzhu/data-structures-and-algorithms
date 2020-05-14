# Singly Linked List
Singly linked lists contain nodes which have a data field as well as 'next' field, which points to the next node in line of nodes. Operations that can be performed on singly linked lists include insertion, deletion and traversal.

## Challenge
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

## Approach & Efficiency
Insertion: O(1); Traversal: O(n)

## API
* Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance
* Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
* Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"