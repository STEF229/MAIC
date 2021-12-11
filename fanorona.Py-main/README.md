# Uniwersytet Śląski

## Wydział Nauk Ścisłych i Technicznych

### Teoria gier na przykładzie gry Fanarona

> Wykonał: Mateusz Klimaszewski, Krzysztof Para, gr. PGK 2.



## Spis treści:

- Złożność gry:
    - <a href="#ZG">Złożność gry Fanarona</a>
- Algorytm MinMax:
    - <a href="#AMM">Algorytm MinMax</a>
- Algorytm AlphaBeta:
    - <a href="#AB">Algorytm AlphaBeta</a>
## Opis:
- Gra, która posłuży do implementacji algorytmów oraz badań to Fanarona: 
    - <a href="https://boardgamegeek.com/boardgame/4386/fanorona">Opis gry Fanarona - boardgamegeek.com</a>
- Projekt został wykonany w języku Python oraz przy wykorzystaniu dodatkowych bibliotek:
  * NumPy
  * statistics 
  * typing
  * time
 
<div style="page-break-after: always; visibility: hidden"> 
</div>

<div id="ZG"></div>

# Złożność gry Fanarona

## Branching Factor:

 Przy 5 tysiącach rozgrywek średnia możliwa ilość ruchów w danym momencie wynosi:

### `b = 5.49`

## Depth:

 W trakcie rozgrywanych tur średnia ilość ruchów podczas całej gry wynosi 

### `d = 68.82`

## Złożoność gry wynosi:


### `𝑏^𝑑 = 5.4968.82 ≈ 1.2162576𝑒+51`

<div id="AMM"></div>

# Algorytm MinMax

Algorytm MinMax zaimplementowano w taki sposób, aby kierować ruchem tylko jednego z dwóch graczy. Celem wyżej  wymienionego algorytmu jest doprowadzenie do przegranej swojego przeciwnika (obecnie jest to gracz losowy).  

## Funkcja kosztu
>Z racji, że w grze Fanorona każdy pion ma tą samą wartość, a wygrana jest uzależniona tylko od momentu, gdy przeciwnik
>nie posiada już pionów, w funkcji kosztu uwzględniliśmy tylko ilość pionów przeciwnika. Funkcja kosztu sprawdza ilość 
>pionków danego gracza i odejmując tą ilość od ilości pionków przeciwnika wyznacza przewagę.
>
Wykonano po 500 rozgrywek dla każdej głębokości algorytmu:

Liczba wygranych gier  | Głębokość 
------------ | -------------
463 (92,6 %)  | 1
500 (100 %)  | 2

`Powyższa funkcja już przy głębokości 2 jest w stanie wygrać 100% gier z przeciwnikiem losowym.`
<div id="AB"></div>

# Algorytm AlphaBeta

Algorytm AlphaBeta zaimplementowano w taki sposób, aby kierować ruchem tylko jednego z dwóch graczy. Celem wyżej  wymienionego algorytmu jest doprowadzenie do przegranej swojego przeciwnika (obecnie jest to gracz losowy).  



Wykonano po 100 rozgrywek dla każdego z algorytmów przy głębokości 3:

Alogrytm  | Średni czas pojedynczego ruchu | Średni czas całej rozgrywki
------------ | ------------- | -------------
MinMax  | 0.41520 | 7.2629
AlphaBeta  | 0.1736 | 2.9398

`Powyższa funkcja już przy głębokości 2 jest w stanie wygrać 100% gier z przeciwnikiem losowym, lecz aby zobaczyć większe różnice czasowe zastosowano głębokość 3`



