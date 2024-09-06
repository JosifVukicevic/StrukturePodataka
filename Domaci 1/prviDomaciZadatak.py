
# Prvi domaci zadatak
# 1o, 1p, 1r, 1s, 1n, 1g, 3, 6

# 1o
"""
def broj_neparnih_cifara(broj):
    if broj < 10:
        if broj % 2 != 0:
            return 1
        else:
            return 0
    else:
        zadnja_cifra = broj % 10
        if zadnja_cifra % 2 != 0:
            return 1 + broj_neparnih_cifara(broj // 10)
        else:
            return broj_neparnih_cifara(broj // 10)

print(broj_neparnih_cifara(123))
print(broj_neparnih_cifara(11354))
"""
# 1p
"""
def broj_negativnih_djeljivih_sa_dva(lista):
    if len(lista) == 0:
        return 0
    else:
        if lista[0] < 0 and lista[0] % 2 == 0:
            return 1 + broj_negativnih_djeljivih_sa_dva(lista[1:])
        else:
            return broj_negativnih_djeljivih_sa_dva(lista[1:])

print(broj_negativnih_djeljivih_sa_dva([1, 5, -4, 3, 7, -8]))
print(broj_negativnih_djeljivih_sa_dva([0, -35, 41, 32]))
"""
# 1r
"""
def okreni_string(s):
    if len(s) == 0:
        return ""
    else:
        return okreni_string(s[1:]) + s[0]

print(okreni_string("zdravo"))
"""
# 1s
"""
def sve_cifre_su_djeljive(m, n):
    if m < 10:
        if m % n == 0:
            return "Da"
        else:
            return "Ne"
    else:
        zadnja_cifra = m % 10
        if zadnja_cifra % n != 0:
            return "Ne"
        else:
            return sve_cifre_su_djeljive(m // 10, n)

print(sve_cifre_su_djeljive(223, 12))
print(sve_cifre_su_djeljive(217, 17))
"""
# 1g
"""
def dekadni_u_binarni(broj):
    if broj <= 1:
        return str(broj)
    else:
        return dekadni_u_binarni(broj // 2) + str(broj % 2)

print(dekadni_u_binarni(10))
print(dekadni_u_binarni(27))
"""
# 1n
"""
def stepenovanje(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * stepenovanje(x, n - 1)

print(stepenovanje(3, 3))
"""
# 3
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # a. Funkcija koja stampa dvostruko olancanu listu od kraja
    def print_from_end(self):
        current = self.tail
        while current:
            # STampanje podataka trenutnog cvora, ako postoji,
            # Ako postoji prethodni cvor dodace se '->' posle podataka, ako ne prelazi se u novi red
            print(current.data, end=" -> " if current.prev else "\n")
            current = current.prev

    # b. Dodavanje novog cvora na pocetak dv. olancane liste
    def add_to_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # c. Dodavanje novog cvora na kraj dv. olancane liste
    def add_to_end(self, data):
        new_node = Node(data)
        if self.tail is None: 
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # d. Brisanje prvog cvora iz dv. olancane liste
    def delete_first(self):
        # Ako je lista prazna
        if self.head is None:
            return
        # Ako postoji samo jedan element
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # e. Brisanje poslednjeg cvora iz dv. olancane liste
    def delete_last(self):
        # Ako je lista prazna
        if self.tail is None:
            return
        # Ako postojji samo jedan element
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # f. Brisanje poslednja dva elementa iz dv. olancane liste.
    def delete_last_two(self):
        self.delete_last()
        self.delete_last()

    # g. Dodavanje elementa na odredjenoj poziciji
    def add_at_position(self, data, position):
        if position <= 0:
            self.add_to_start(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    break
                current = current.next
            if current is None:
                self.add_to_end(data)
            else:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                if new_node.next is None:
                    self.tail = new_node

    # h. Brisanje elementa sa zadate pozicije
    def delete_at_position(self, position):
        if position <= 0:
            self.delete_first()
        else:
            current = self.head
            for i in range(position):
                # Ako je current = Non, vracemo se ne preduzimajuci nista
                if current is None:
                    return
                # U suprotnom prelazimo na sljedeci cvor
                current = current.next
            if current is None:
                return
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
            if current == self.head:
                self.head = current.next
            if current == self.tail:
                self.tail = current.prev

    # i. Brisanje elementa cija se vrijednost zadata kao argument funkcije
    def delete_by_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next

    # j. Implementacija metode get_middle_node(self)
    def get_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    # k. Implementacija metode remove_duplicates(self)
    def remove_duplicates(self):
        current = self.head
        seen = set()
        while current:
            if current.data in seen:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
            else:
                seen.add(current.data)
            current = current.next

    # l. Funkciju koja mijenja mjesta najmanjem i najvecem elementu liste
    def swap_min_max(self):
        if self.head is None:
            return
        
        min_node = max_node = self.head
        current = self.head
        while current:
            if current.data < min_node.data:
                min_node = current
            if current.data > max_node.data:
                max_node = current
            current = current.next
        
        # Zamjena podataka za min_node i max_node
        if min_node != max_node:
            min_node.data, max_node.data = max_node.data, min_node.data

dll = DoublyLinkedList()
dll.add_to_end(2)
dll.add_to_end(45)
dll.add_to_end(3)
dll.add_to_end(1)

dll.print_from_end()  # Output: 1 -> 3 -> 45 -> 2

dll.add_to_start(100)
dll.print_from_end()  # Output: 1 -> 3 -> 45 -> 2 -> 100

dll.delete_first()
dll.print_from_end()  # Output: 1 -> 3 -> 45 -> 2

dll.get_middle_node()
"""

# 6
"""
class Student:
    def __init__(self, name, surname, year, avg_grade):
        self.name = name
        self.surname = surname
        self.year = year
        self.avg_grade = avg_grade
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return f'Ime: {self.name} {self.surname}, Godina: {self.year}, Prosjek: {self.avg_grade}'

class StudentLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_student(self, name, surname, year, avg_grade):
        new_student = Student(name, surname, year, avg_grade)
        if self.head is None:
            self.head = new_student
            self.tail = new_student
        else:
            self.tail.next = new_student
            new_student.prev = self.tail
            self.tail = new_student

    def get_better_avg_grade_students(self, grade):
        current = self.head
        result = []
        while current:
            if current.avg_grade > grade:
                result.append(current)
            current = current.next
        return result
    
    def get_students_before_index(self, index):
        current = self.tail
        result = []
        while current and index > 0:
            result.append(current)
            current = current.prev
            index -= 1
        return result

student_list = StudentLinkedList()
student_list.add_student("Marko", "Markovic", 3, 7.8)
student_list.add_student("Pera", "Peric", 2, 6.5)
student_list.add_student("Jovana", "Jovanovic", 3, 8)
student_list.add_student("Petar", "Petrovic", 1, 7.5)
student_list.add_student("Mina", "Minic", 2, 9.5)

grade = 7
filtered1 = student_list.get_better_avg_grade_students(grade)
print(f"Studenti sa boljom ocjenom od {grade}")
for student in filtered1:
    print(student)
print("Ima ih ukupno: ", len(filtered1))

filtered2 = student_list.get_students_before_index(4)
print("\nStudenti prije zadatog indeksa:")
for student in filtered2:
    print(student)
"""