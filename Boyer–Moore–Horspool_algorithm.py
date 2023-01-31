t = "suszy"

# Krok 1: Wygenerowanie tabeli offsetów

S = set()  # unikalne znaki w obrazie
M = len(t) # liczba znaków w obrazie
d = {}     # słownik przesunięć

for i in range(M-2, -1, -1): # iteracja od przedostatniego znaku
    if t[i] not in S:        # jeśli symbol nie został jeszcze dodany do tabeli
        d[t[i]] = M-i-1
        S.add(t[i])

if t[M-1] not in S:     # tworzą ostatni znak osobno
    d[t[M-1]] = M

d['*'] = M              # przesunięcia dla innych znaków

print(d)

# Krok 2: Wyszukiwanie obrazu w ciągu znaków

a = "W czasie suszy szosa sucha mucha"
N = len(a)

if N >= M:
    i = M-1       # licznik znaku, który ma być sprawdzony w łańcuchu

    while(i < N):
        k = 0
        j = 0
        flBreak = False
        for j in range(M-1, -1, -1):
            if a[i-k] != t[j]:
                if j == M-1:
                    off = d[a[i]] if d.get(a[i], False) else d['*']  # przesunięcie, jeżeli ostatni znak obrazu nie jest równy
                else:
                    off = d[t[j]]   # przesunięcie, jeśli nie jest równe ostatniemu znakowi obrazu

                i += off    # przesunięcie licznika wierszy
                flBreak = True  # jeśli znaki są niedopasowane, flBreak = True
                break

            k += 1          # offset dla porównywanego znaku w łańcuchu

        if not flBreak:          # jeśli dotarłeś do początku obrazka, to wszystkie jego symbole zostały dopasowane
            print(f'Znaleziono słowo - "{t}" w tekście "{a}", indeksem {i-k+1}')
            break
    else:
        print(f'Nie znaleziono słowo - "{t}" w tekście: "{a}"')
else:
    print(f'Nie znaleziono słowo - "{t}" w tekście: "{a}"')