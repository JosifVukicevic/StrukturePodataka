# 9c
def parnepar(S1, S2):
    while not S1.is_empty():
        element = S1.pop()
        if element % 2 == 0:
            S1.push(element)
        else:
            S2.push(element)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

S1 = Stack()
S2 = Stack()

elements = [3, 1, 4, 1, 2, 6]
for element in elements:
    S1.push(element)

parnepar(S1, S2)

print("S1 =", tuple(S1.items))
print("S2 =", tuple(S2.items))

########################################
# 9g
""""""
class Station:
    def __init__(self, name):
        self.name = name
        self.passengers = 0
        self.next = None

class CircularTramRoute:
    def __init__(self):
        self.head = None

    def add_station(self, name):
        new_station = Station(name)
        # Ako je ruta prazna, postavi novu stanicu kao glavu i povezi je sa samom sobom
        if not self.head:
            self.head = new_station
            new_station.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_station
            new_station.next = self.head

    def update_passengers(self, station, enter, exit_):
        # Ako vise putnika izlazi nego sto ih je u tramvaju, svi izlaze
        if exit_ > station.passengers:
            station.passengers = 0
        else:
            station.passengers -= exit_
        station.passengers += enter

    # Metoda za ispis rute sa brojem putnika na svakoj stanici
    def print_route(self):
        # Ako ruta nema stanica, vrati se
        if not self.head:
            return
        current = self.head
        while True:
            # Ispis trenutne stanice i broja putnika
            print(f"Stanca: {current.name}, Putnici: {current.passengers}")
            current = current.next
            if current == self.head:
                break

    def run_tram(self):
        # Ako nema stanica u ruti, vrati se
        if not self.head:
            return
        # Pocetak od glave rute
        current = self.head
        while True:
            # Ispis trenutne stanice
            print(f"Trenutna stanica: {current.name}")

            enter = int(input(f"Broj putnika koji ulaze {current.name}: "))
            exit_ = int(input(f"Broj putnika koji izlaze {current.name}: "))

            self.update_passengers(current, enter, exit_)
            self.print_route()

            # Provjera je li ostala samo jedna stanica
            if current.next == current:
                print(f"Poslednja stanica: {current.name}, Svi putnici izlaze.")
                break
            # Prelazak na sledecu stanicu
            current = current.next

# Unos broja stanica
N = int(input("Enter the number of stations: "))
# instanca tramvajske rute
tram_route = CircularTramRoute()

for _ in range(N):
    name = input("Ime stanice: ")
    enter = int(input(f"Broj putnika koji ulaze {name}: "))
    exit_ = int(input(f"Broj putnika koji izlaze {name}: "))
    # Dodavanje stanice u kruznu rutu
    tram_route.add_station(name)  
    #Azuriranje broja putnika na stanici
    tram_route.update_passengers(tram_route.head, enter, exit_)


tram_route.print_route()
tram_route.run_tram()


########################################
# 10b
class Node:
    def __init__(self, naziv):
        self.naziv = naziv
        self.left = None
        self.right = None

def nivo(root, naziv, level=1):
    if root is None:
        return None

    if root.naziv == naziv:
        return level

    left_level = nivo(root.left, naziv, level + 1)
    if left_level:
        return left_level

    right_level = nivo(root.right, naziv, level + 1)
    if right_level:
        return right_level

    return None

"""
          A
        /   \
       B     C
      / \   / \
     D   E F   G
"""
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

naziv = 'F'
n = nivo(root, naziv)
if n:
    print(f"Artikal {naziv} se nalazi na nivou {n}.")
else:
    print(f"Artikal {naziv} nije pronadjen u stablu.")

