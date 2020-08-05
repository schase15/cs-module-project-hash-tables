# HashTableEntry() class creates a node to store key and value in a linked list
# LinkedList() class creates an empty linked list to store HashTableEntry nodes
# HashTable() class creates an empty array to hold linked lists


class LinkedList():
    '''
    Linked list class that will hold HashtableEntry nodes
    Methods:
    - Find(): Looks through linked list to see if given key exists
    - Insert_at_head(): Inserts a HashTableEntry node with key and value at the head of the linked list
    - Delete(): If the given key exists, deletes the node associated with the key
    '''

    def __init__(self):
        # Add a head indicator to know where to start
        self.head = None

    # Search through the linked list to see if the key exists
    def find(self, key):
        cur = self.head

        # While there is still set
        while cur is not None:
            # If the value is found, return it
            if cur.key == key:
                return cur

            cur = cur.next

        # We we walk through until there is no more next node and haven't 
        # found the value we are looking for, return None
        return None    

    # Insert a new node at the head of the list
    def insert_at_head(self, node):
        # Move the current head to the next of the new node
        node.next = self.head
        # Set the new node as the head
        self.head = node

# Delete nodes by removing any next link pointers to them

    def delete(self, key):
        cur = self.head

        # Special case of deleting the head of the list
        if cur.key == key:
            # Move the head to the next node
            self.head = cur.next
            # Return deleted node
            return cur
        
        # General case of deleting from the rest of the list
        prev = cur
        cur = cur.next

        # Look at the current node.key
        while cur is not None:
            if cur.key == key:
                # Cut out the node, set the previous next to the cur.next
                prev.next = cur.next
                # Return deleted key for the user
                return cur
            else:
                # Bump prev and cur pointers up one, until cur falls off the end of the list
                prev = cur
                cur = cur.next

        # If we get here, we didn't find it
        return None

class HashTableEntry:
    """
    Creates node inside of a linked list to store key and value
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({repr(self.value)})'

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):

        # Hashtables have a minimum size
        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY

        # Create array of size capacity populated with None
        self.data = [None] * self.capacity

        # Counter to be used by load factor
        self.count = 0

        # Add a head indicator
        self.head = None


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """

        # Return capacity
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Number of items in hash table / number of slots
        return self.count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381

        for c in key:
            # ord() function returns an integer representing the Unicode character
            # adding the result of ord to 33*5381 - for each character in the key
            hash = (hash * 33) + ord(c)

        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
            # Divides hash of key by the capacity, 
            # returns the remainder to be used as the index location
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Use the hash_index() method to get the proper index
        index = self.hash_index(key)

        # If the slot is empty - None, Start a new linked list
        # and add a node with the key and value
        if self.data[index] == None:
            # Start new linked list
            self.data[index] = LinkedList()
            # Add in new node with key and value
            self.data[index].insert_at_head(HashTableEntry(key, value))
            # Add 1 to count whenever a node is added
            self.count += 1
        
        # If that slot isn't empty
        else:
            # Linked list at the specific index
            linked_list = self.data[index]

            # Search the linked list for the key
                # If it finds it, it will return the node that holds the key and value
                # If it doesn't find it, it will return None
            find_key = linked_list.find(key)

            # If the key doesn't exists, add a new node with the key and value
            if find_key == None:
                # Add node
                linked_list.insert_at_head(HashTableEntry(key, value))
                # Add 1 to count
                self.count += 1

            # if the key exists, overwrite the value
            else:
                find_key.value = value

        # Check the load factor, if it is more than 0.7 
            # Double table and re-hash
        if self.get_load_factor() > 0.7:
            # Run re-size function
            self.resize(self.capacity *2)
            # pass


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Find the index of the given key
        index = self.hash_index(key)

        # If there is nothing at that index, return Error Message
        if self.data[index] == None:
            print('Key is not found')

        # If there is something at that index,
        else:
        # Use the linked list delete method
            # If it finds the key, it will delete it and return the node deleted
            # If it doesn't find the key, it will return None

            linked_list = self.data[index]
            result = linked_list.delete(key)

            # If the result of delete is None,
                # Print "key not found" for the user
            if result == None:
                print('Key not found')
            # If the key is found and deleted
                # Return the deleted value
                # Subtract 1 from the count
            else:
                self.count -= 1
                # Print the deleted key for the user's reference
                print(f"Key deleted: {result.key}.")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Get the index location
        index = self.hash_index(key)

        # If there is nothing at that index, return None
        if self.data[index] == None:
            return None
        
        # Otherwise, examine the linked list at that index
        else:
            linked_list = self.data[index]
            # Use the find method to find the node at with the key
            #  Returns a Node with the key
            #  Or returns None if the key doesn't exist
            key_node = linked_list.find(key)

            # If key doesn't exits, return None
            if key_node == None:
                return None
            # If the key exists, return the value associated
            else:
                return key_node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Save the data from the old ht
        old_ht = self.data

        # Change the capacity to the new capacity
        self.capacity = new_capacity

        # Write over any data with None
        self.data = [None] * self.capacity

        # Re-set the count to 0
        self.count = 0

        # Re-set the head
        self.head = None

        # Use the data stored from the old Hashtable to re-hash and populate 
        # into the re-set, doubled capacity array

        # Iterate through each array of linked lists
        # Skip over indexes that don't have a linked list
        for linked_list in old_ht:
            # If linked_list is None
            if linked_list == None:
                pass
            else:
                # For each linked list, traverse each node
                cur = linked_list.head

                # While there is still a current node
                while cur is not None:
                    # Perform PUT with key and value
                    self.put(cur.key, cur.value)
                    # Move to the next node and repeat
                    cur = cur.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
