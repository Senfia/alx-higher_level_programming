#!/usr/bin/python3
"""
Node class creates a Node object.
"""


class Node(object):
    """
    Initialize Node object.
    """
    def __init__(self, data, new_node=None):
        if type(data) is not int or isinstance(data, bool):
            raise TypeError('data must be an integer')
        self.__data = data
        self.__new_node = new_node

    @property
    def data(self):
        """
        getter for data
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        setter for data
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def new_node(self):
        """
        getter for node
        """
        return self.__new_node

    @new_node.setter
    def new_node(self, value):
        """
        setter for node
        """
        if value is not None and type(value) is not Node:
            raise TypeError('next must be a Node object')
        self.__new_node = value


class SinglyLinkedList(object):
    """
    initialize SinglyLinkedList object
    """
    def __init__(self):
        """
        init
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts by int value
        """
        if not self.__head:
            self.__head = Node(value, None)
        else:
            current = self.__head
            prev = None
            while current and value > current.data:
                prev = current
                current = current.new_node
            if not current:
                prev.new_node = Node(value)
            elif current == self.__head:
                self.__head = Node(value, current)
            else:
                prev.new_node = Node(value, current)

    def __str__(self):
        """
        formats list for output
        """
        result = ""
        tmp = self.__head
        while tmp:
            result += str(tmp.data)
            tmp = tmp.new_node
            if tmp:
                result += '\n'
        return result
