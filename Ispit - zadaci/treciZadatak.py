# Inicijalizacija klase za red
class Queue:
    def __init__(self):
        self.rear = -1
        self.queue = []
    
    # Metoda koja stampa sve clanove reda
    def print_queue(self):
        s = ""
        for i in range(self.rear + 1):
            s += self.queue[i] + " "
        print(s)
    
    # Metoda koja dodaje novi elemenat u red
    def enqueue(self, data):
        self.queue.append(data)
        self.rear += 1
    
    # Metoda koja uklanja elemenat iz reda
    def dequeue(self):
        destination = self.queue[0]
        for i in range(self.rear):
            self.queue[i] = self.queue[i + 1]
        self.queue.pop()
        self.rear -= 1
        return destination
    
    # Metoda koja vrace novi red u kojem je uklonjen svaki treci elemenat iz originalnog reda
    def filter_third(self):
        helper = Queue()
        for i in range(self.rear + 1):
            if (i + 1) % 3 != 0:
                helper.enqueue(self.queue[i])
        return helper
        
# Inicijalizacija i dodavanje elemenata u red
p = Queue()
p.enqueue("Podgorica")
p.enqueue("Spuz")
p.enqueue("Danilograd")
p.enqueue("Niksic")
p.enqueue("Trebinje")
p.enqueue("Foca")

# Testiranje metoda
p.print_queue()

new_p = p.filter_third()
new_p.print_queue()
