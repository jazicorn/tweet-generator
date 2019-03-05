#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        # % called modules calculates the remainder
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Loop through all buckets
        # Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) Why and under what conditions?
        Becuase you have to iterate over each bucket to count
        """
        # Count number of key-value entries in each bucket
        count = 0
        # loop through all buckets
        # n number entries
        # b number of buckets
        # l  n/b
        for bucket in self.buckets: # b iterations
            count += bucket.length() # O(l)
        return count
        # 0(l) / O(n +l) cancel (l) get (n) left
        # Overall =: O(b+1) --> 0(n) looking at each entry at least 1

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        # self.buckets is an array, arrays are contiguous in memory so faster to read
        bucket = self.buckets[index]
        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # Check out the entry that was returned = is it None?
        if entry is None:
            return False
        else: # entry is not None
            return True
        # shorter version
        return (entry is not None)

    def get(self, key):
        """Return the value associated with t wh e given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""

        # first find the index that has been hashed by the hash function
        index = self._bucket_index(key)
        # Find bucket where given key belongs
        bucket = self.buckets[index]

        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key) # 0(l) with l = bucket.length()
        # If found, return value associated with given key
        if entry is not None: # Found entry
            return entry[1] # Get value only at index 1

        # Otherwise, raise error to tell user get failed 
        else:
            raise KeyError('Key not found: {}'.format(key))


    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(l) or O(1) Why and under what conditions?
        Best case O(1) if located near head fo the list Worst O(l)"""
        # Find bucket where given key belongs
        # getting index of desired bucket
        index = self._bucket_index(key)
        bucket  = self.buckets[index]

        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key) # O(l)

        # If found, delete value associated with given key
        if entry is not None:
            # delete entry from bucket
            bucket.delete(entry) # O(l) worst case

        # Always insert given key-value entry into bucket
        entry = (key, value)    #O (1)
        bucket.append(entry) # O(1)

        # another way to replace
        # if entry is not None:
        #     bucket.replace(entry, entry2)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(n) Why and under what conditions?"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket  = self.buckets[index]
        # Check if key-value entry exists in bucket
        # 0(1) constant time operation because using array method
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # If found, delete entry associated with given key
        if entry is not None:
            # delete entry from bucket
            bucket.delete(entry)
            # alternate way get length of hash
            # self.tot_length -= 1
        # Otherwise, raise error to tell user delete failed
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
