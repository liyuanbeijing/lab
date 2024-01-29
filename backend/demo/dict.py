basket1 = {
    "apple": 10,
    "orange": 20,
    "banana": 30
}

basket2 = {
    "apple": 5,
    "pear": 10,
    "orange": 15
}

# Merge two dictionaries
basket_all = {
    key: basket1.get(key, 0) + basket2.get(key, 0)
    for key in basket1.keys() | basket2.keys()
}

####

list1 = ['a', 'b', 'c', 'a', 'b', 'e']

# dictionary comprehension
# Get unique items from list, remain order
list_uni_itmes = list(dict.fromkeys(list1))


def main():
    # print(basket_all)
    print(list_uni_itmes)


if __name__ == "__main__":
    main()
