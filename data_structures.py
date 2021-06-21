



class Node():
    """
    Represents a single node that can be linked to another.
    """

    def __init__(self, data, next = None):
        """
        Constructor of the node.

        Args:
            data: The value of the node.
            next (optional): The reference or pointer to the next node. Defaults to None.
        """
        self.data = data
        self.next = next



class TwoWayNode(Node):
    def __init__(self, data, next = None, previous = None):
        """
        Similar to a single node but it has an extra atribute.

        Args:
            data: The value of the node.
            next (optional): The reference or pointer to the next node. Defaults to None.
            previous (optional: The reference or pointer to the previous node. Defaults to None.
        """
        super().__init__(data, next)
        self.previous = previous



class TwoWayNodeQueue():
    """
    This class represent a queue of nodes that respect the FIFO(first-in-first-out) concept.
    """

    def __init__(self):
        """
        Constructor of the class TwoWayNodeQueue.

        Args:
            front: Refers to the first node that entered the queue.
            rear: Refers to the last node that entered the queue.
            size: The length of the queue.
        """
        
        self.front = None
        self.rear = None
        self.size = 0
        

    
    def add(self, data):
        """
        This function add a new node in the end of the queue.
        """

        node = TwoWayNode(data)

        if self.front is None:
            self.front = node
            self.rear = node

        else:
            node.next = self.rear

            self.rear = node

            node.next.previous = node


        self.size += 1 

    
    def pop(self):
        """
        This function delete the first element of the queue.

        Returns:
            data: Returns the element that was deleted.
        """

        current_node = self.front
        
        if self.size == 1:
            self.size -= 1

            self.front = None
            self.rear = None

        elif self.size > 1:
            self.size -= 1

            self.front = self.front.previous
            self.front.previous.next = None

        return current_node.data

        