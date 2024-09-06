"""Prvi zadatak pod A"""
def are_all_characters_present(S, P):
    # Ukoliko je string S prazan svi karakteri su prisutni
    if not S:
        return True

    # Ukoliko prvi karakter stringa S ne postoji u string P onda funkcija vrace False
    if S[0] not in P:
        return False

    # Funkcija poziva samu sebe bez prvog karaktera stringa S
    return are_all_characters_present(S[1:], P)

# Test funkcije
S = "abc"
P = "aabbcc"
print(are_all_characters_present(S, P))

S = "abc"
P = "ac"
print(are_all_characters_present(S, P))

"""Prvi zadatak pod B"""
# Funkcija se poziva samo sa listom torki koje predstavljaju minimalnu i maksimalnu temperaturu, ostale pomocne varijable inicijalizuje funkcija
def average_temperature_difference(pairs, index=0, min_sum=0, max_sum=0):

    # Ukoliko je pomocna varijabla index jednaka duzini niza funkcija vrace razliku izmedju prosjeka maksimalne i minimalne temperature
    if index == len(pairs):
        return max_sum / index - min_sum / index
    
    # Pri svakom pozivu funkcije se varijable min_sum i max_sum povecavaju za temperature iz trenutnog para
    min_sum += pairs[index][0]
    max_sum += pairs[index][1]

    return average_temperature_difference(pairs, index + 1, min_sum, max_sum)

# Test funkcije
temperature_pairs = [(10, 20), (12, 22), (8, 18)]
print(average_temperature_difference(temperature_pairs))