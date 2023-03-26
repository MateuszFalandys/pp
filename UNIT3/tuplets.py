#-----------------------------------
animal_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
}

animal_dict["świnka"] = "pig"
animal_dict.update({"kurczak":"chciken"})
animal_dict.update({"świnka":"piggy"})
print(animal_dict)

dict2 = animal_dict.copy()
print(dict2)
del dict2["świnka"]
print(dict2)
dict2.popitem()
print(dict2)
dict2.clear()
print(dict2)

# #-----------------------------------

# animal_dict = {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# print(animal_dict.get("krowa", "brak takiego słowa"))
#
# for key in animal_dict.keys():
#     print(key, " -> ", animal_dict[key])
#
# for val in animal_dict.values():
#     print(val)
#
# for item in animal_dict.items():
#     print(item)
#
# for pl,eng in animal_dict.items():
#     print(pl, " -> ", eng)

# #-----------------------------------
# words = ["kot", "lew", "chomik"]
# for word in words:
#     if word in animal_dict:
#         print(word, "->", animal_dict[word])
#     else:
#         print("Nie znaleziono słowa ",word, "w słowniku.")

# -----------------------------------
# phones ={"Tomek": 535795535,
#          "Ada": 123123123,
#         "Bartek": 999999999}
# print(phones)


# #-----------------------------------
# numbers = "Ala ma kota"
# numbers = tuple(numbers)
#
# print(numbers)


# -----------------------------------
#
# numbers = tuple(x for x in range(10))
#
# print(numbers)


# -----------------------------------
# #numbers = (1, 2, 3)
# numbers = 1,2,3
# #numbers = ()
# #numbers = (1,)
#
# print(numbers[-2])
#
# for i in numbers:
#     print(i)
#
# print(numbers[:])
