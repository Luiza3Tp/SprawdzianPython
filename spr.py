parzyste =0
ilosc=0
tylkoZero=0
tylkoOne=0
koniecOne=0
palindromy=0
dlugoscNap={k: 0 for k in range(2,17)}

with open('napisy.txt','r') as plik:
    for line in plik:
        line =line.strip()
        dlugosc=len(line)
        dlugoscNap[dlugosc]+=1

        if dlugosc % 2 == 0:
            parzyste+=1

        if line.count('0')== line.count('1'):
            ilosc += 1

        if line.count('0') == dlugosc:
            tylkoZero=1
        elif line.count('1') == dlugosc:
            tylkoOne += 1

        if line.endswith('1'):
            koniecOne+=1

        if line == line[::-1]:
            palindromy+=1

with open('wynik.txt','w') as wyniki:
    wyniki.write(f"a. {parzyste}\n")
    wyniki.write(f"b. {ilosc}\n")
    wyniki.write(f"c. zer jest {tylkoZero} jedynek jest {tylkoOne}\n")
    wyniki.write(f"d. {koniecOne}\n")
    wyniki.write(f"e. {palindromy}\n")
    for k, ilosc in dlugoscNap.items():
        wyniki.write(f"f.Napisow {k}-znakowych: {ilosc}\n")

print("koniec wynik zobaczysz w pliku wynik.txt")
