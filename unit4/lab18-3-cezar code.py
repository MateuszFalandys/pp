#  Rozszyfruj poniższą wiadomość wiedząc, że została ona zaszyfrowana szyfrem
# cezara z parametrem przesunięcia równym 3.
# VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ

delta = 3

print(ord("A"))
print(ord("Z"))

for i in range(ord("A"), ord("Z") + 1):
    print(chr(i), end="")

print()
for i in range(ord("A") + delta, ord("Z") + 1 + delta):
    if i > ord("Z"):
        i -= ord("Z") - ord("A") + 1
    print(chr(i), end="")


def dicode_letter(letter, delta):
    if letter < "A" or letter > "Z":
        return letter
    n = ord(letter) - delta
    if n < ord("A"):
        n += ord("Z") - ord("A") + 1
    return chr(n)


def decode(string, delta):
    decoded = ""
    for char in string:
        decoded += dicode_letter(char, delta)
    return decoded

print()
print(decode("VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ", delta))
