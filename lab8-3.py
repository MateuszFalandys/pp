# pole szachownicy ma 64 pola
liczba_ziaren=0
for i in range(64):
    liczba_ziaren += 2**i

print("Liczba ziaren na 64 polach to:", liczba_ziaren)

# tysiąc ziaren waży 40g
waga_ziaren = liczba_ziaren / 1000 * 0.0004 / 1000
print("Waga ziaren wynosi: ", waga_ziaren, " ton.")
lata=round(waga_ziaren/782e6,2)
print("Przez tyle lat trzebaby produkować na całym świecie:",lata)

#jeden pociąg 2200 ton
trains_number=round(waga_ziaren/2200,0) + 1
print("Przewiezienie ziarna wymagałoby: ",trains_number," pociągów")
