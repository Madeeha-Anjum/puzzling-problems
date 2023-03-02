def simple_hash(key):
    return hash(key) % 11


hashmap = {}

if __name__ == "__main__":

    # Add key-value pairs to the hashmap
    hashmap[simple_hash("beans")] = 1.8
    hashmap[simple_hash("corn")] = 1.3
    hashmap[simple_hash("Rice")] = 1.5

    # Access values using the hashmap
    print("beans ", hashmap[simple_hash("beans")])
    print("corn ", hashmap[simple_hash("corn")])
    print("Rice ", hashmap[simple_hash("Rice")])
