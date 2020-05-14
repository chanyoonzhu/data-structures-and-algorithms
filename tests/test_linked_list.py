from data_structures_and_algorithms import __version__
from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList, Node

def test_linked_list_creation():
    assert LinkedList().head == None

def test_node_creation():
    node = Node("Chengdu")
    assert node.val == "Chengdu"
    assert node.next == None

def test_linked_list():
    cities = LinkedList()
    cities.head = Node("Beijing")
    cities.head.next = Node("Shanghai")

    assert cities.head.next.val == "Shanghai"

def test_insert():
    cities = LinkedList()
    cities.insert("Beijing")
    cities.insert("Guangzhou")
    cities.insert("Chengdu")

    assert cities.head.val == "Chengdu"
    assert cities.head.next.val == "Guangzhou"
    assert cities.head.next.next.val == "Beijing"

def test_includes():
    cities = LinkedList()
    cities.insert("Beijing")
    cities.insert("Guangzhou")
    cities.insert("Chengdu")

    assert cities.includes("Chengdu")

def test_not_includes():
    cities = LinkedList()
    cities.insert("Beijing")
    cities.insert("Guangzhou")
    cities.insert("Chengdu")

    assert not cities.includes("Shanghai")

def test_to_string():
    cities = LinkedList()
    cities.insert("Beijing")
    cities.insert("Guangzhou")
    cities.insert("Chengdu")

    assert cities.__str__() == "{ Chengdu } -> { Guangzhou } -> { Beijing } -> NULL"

def test_empty_linked_list_to_string():
    cities = LinkedList()

    assert cities.__str__() == "NULL"