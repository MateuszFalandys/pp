# napisać program rozszywający
# Xq|`gf(bm{|(nibfq)
# dla każdego znaku zmieniono czwarty bit na przeciwny
# bity liczymy od najmniej znaczącego, 4 bit -> indeks 3

# print(ord("c")) #w ASCII
# print(bin(ord("c"))) #wartość binarna
# print("{:08b}".format(ord("c")))

# 01100011 - nasza liczba
# 00001000 - maska do procesu
# 01101011 - używamy XORa (alternatywa rozłączna)

print("{:08b}".format(ord("c") ^ (1 << 3)))
print(chr(ord("c") ^ (1 << 3)))

msg = "Xq|`gf(bm{|(nibfq)"
for c in msg:
    print(chr(ord(c) ^ (1 << 3)), end="")
