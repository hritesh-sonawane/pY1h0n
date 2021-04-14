class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        # .encode() is a string method that converts a string into its corresponding bytes
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    # setter function
    # Collisions: This is when two different keys resolve to the same array index.
    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value is None:
            self.array[array_index] = [key, value]
        return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
        return

    # getter function
    # When we retrieve hash map values, we also need to be aware of the fact that two keys could point to the same array index.
    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None
        elif possible_return_value[0] == key:
            return possible_return_value[1]


# Testing
hash_map = HashMap(20)
hash_map.assign("Rock Lee", "Taijutsu")
print(hash_map.retrieve("Rock Lee"))