# Klasa kompozicija sa svim potrebnim atributima
class Kompozicija:
    def __init__(self, kompozitor, naziv, godina, trajanje):
        self.kompozitor = kompozitor
        self.naziv = naziv
        self.godina = godina
        self.trajanje = trajanje

    def __repr__(self):
        return self.naziv
    
    def __str__(self) -> str:
        return self.naziv

# Klasa node koja predstavlja cvor liste, i koja zajedno sa kompozicijom ima pokazivace next i prev
class Node:
    def __init__(self, data, next, prev) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return self.data
    
    def __str__(self) -> str:
        return str(self.data)

# Klasa dvostruko olancane liste, sa pokazivacima head i tail
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # Metoda koja stampa listu
    def print_list(self):
        node = self.head
        s = ""
        while node != None:
            s += str(node) + " <-> "
            node = node.next
        print(s)

    # Metoda kojom se cvor dodaje na pocetak liste
    def add_to_start(self, kompozicija):
        node = Node(kompozicija, self.head, None)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            self.head = node
    
    # Metoda kojom se cvor dodaje na kraj liste
    def add_to_end(self, kompozicija):
        node = Node(kompozicija, None, self.tail)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # Metoda kojom se kompozicije filtriraju po godini i duzini trajanja
    def filter_list(self, duration, year):
        node = self.head
        while node != None:
            if node.data.trajanje > duration and node.data.godina > year:
                print(node)
            node = node.next
    
    # Metoda koja stampa kompoziciju sa najduzim trajanjem
    def max_of_the_list(self):
        node = self.head
        max_node = self.head
        while node != None:
            if node.data.trajanje > max_node.data.trajanje:
                max_node = node
            node = node.next
        print("Kompozicija sa najduzim trajanjem: " + max_node.data.naziv + " , kompozitora: " + max_node.data.kompozitor)

    # Metoda koja stampa listu od poslednjeg clana
    def reverse_print(self):
        node = self.tail
        s = ""
        while node != None:
            s += str(node) + " <-> "
            node = node.prev
        print(s)

    # Metoda koja kreira novu listu u kojoj su na pocetku liste kompozicije nastale prije navedene godine, a na kraju iste ili posle te godine
    def transform_list(self, year):
        transformed = LinkedList()
        node = self.head
        while node != None:
            if node.data.godina < year:
                transformed.add_to_start(node.data)
            else:
                transformed.add_to_end(node.data)
            node = node.next
        return transformed

# Inicijalizacija kompozicija
kompozicija1 = Kompozicija("Pyotr Ilyich Tchaikovsky", "1812 Overture", 1880, 15)
kompozicija2 = Kompozicija("Ludwig van Beethoven", "No. 5", 1808, 15)
kompozicija3 = Kompozicija("Wolfgang Amadeus Mozart", "Eine kleine Nachtmusik", 1787, 20)
kompozicija4 = Kompozicija("Johann Sebastian Bach", "Toccata and Fugue in D minor", 1704, 10)
kompozicija5 = Kompozicija("Frederic Chopin", "Nocturne in E-flat major, Op. 9, No. 2", 1832, 5)

# Inicijalizacija liste
linked_list = LinkedList()

# Dodavanje kompozicija u listu
linked_list.add_to_end(kompozicija1)
linked_list.add_to_end(kompozicija2)
linked_list.add_to_end(kompozicija3)
linked_list.add_to_end(kompozicija4)
linked_list.add_to_end(kompozicija5)

# Testiranje metoda
linked_list.filter_list(10, 1800)
linked_list.max_of_the_list()
linked_list.print_list()
linked_list.reverse_print()

transformed = linked_list.transform_list(1800)
transformed.print_list()



