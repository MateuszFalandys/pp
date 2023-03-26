#  Zaimplementuj funkcję, która przyjmuje jako argument ciąg znaków i zwraca
# liczbę wystąpień każdego znaku w ciągu.
# Na przykład dla ciągu "abracadabra" funkcja powinna zwrócić słownik { 'a': 5, 'b':
# 2, 'r': 2, 'c': 1, 'd': 1 }.


def count_letters(string):
    stats = {}
    for char in string:
        if char in stats.keys():
            stats[char] += 1
        else:
            stats[char] =1
    return stats


print(count_letters("abrac12adabra"))
