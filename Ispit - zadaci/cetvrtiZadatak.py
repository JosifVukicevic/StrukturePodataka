class Node:
    # Inicijalizacija za cvor
    def __init__(self, name, visitors):
        self.name = name
        self.visitors = visitors
        self.left = None
        self.right = None
    
    def __repr__(self):
        return self.name

# Funkcija za dodavanje cvorova po pravilima binarnog stabla
def add(root, name, visitors):
    if root == None:
        return Node(name, visitors)
    if visitors < root.visitors:
        root.left = add(root.left, name, visitors)
    else:
        root.right = add(root.right, name, visitors)
    return root
    
# Funkcija koja trazi destinaciju sa najmanje posjetilaca, tako sto ide do najlevljeg cvora
def min_visitors(root):
    current = root
    while current.left != None:
        current = current.left
    return current.name

# Funkcija filtrira stablo po cvorovima i filtrirane cvorove smjesta u listu
def filter_by_visitors(root, min_visitors):
    if root == None:
        return []
    
    filtered = []
    if root.visitors > min_visitors:
        filtered.append(root)
    
    filtered += filter_by_visitors(root.left, min_visitors)
    filtered += filter_by_visitors(root.right, min_visitors)
    
    return filtered
    
# Funkcija vrace ukupan broj posjetilaca svih cvorova u stablu
def num_visitors(root):
    if root == None:
        return 0
    return root.visitors + num_visitors(root.left) + num_visitors(root.right)

# Funkcija vrace broj cvorova (destinacija)
def num_destinations(root):
    if root == None:
        return 0
    return 1 + num_destinations(root.left) + num_destinations(root.right)

# Funkcija vrace destinacije sa brojem posjetilaca vecim od prosjeka. Funkcionise tako sto poziva funkciju filter_by_visitors sa prosjekom dobijenim formulom (broj posjetilaca/broj destinacija)
def filter_by_average_visitors(root):
    return filter_by_visitors(root, num_visitors(root) / num_destinations(root))
  
# Funkcija koja vrace destinacije sa brojem posjetilaca manjim od root cvora. Poziva funkciju num_visitors s tim sto pocinje od prvog lijevog cvora 
def dests_smaller_than_root(root):
    if root == None:
        return 0
    return num_visitors(root.left)

# Funkcija stampa sve cvorove na odredjenom nivou
def levelorder(root, level):
    if root is None:
        return 0
    if level == 1:
        print(root.name, root.visitors)
        return 1
    else:
        return levelorder(root.left, level - 1) + levelorder(root.right, level - 1)

# Funkcija koja stampa cvorove prema postorder principu 
def preorder(root):
    if root is None:
        return
    print(root.name, root.visitors)
    preorder(root.left)
    preorder(root.right)

# Kreiranje cvorova    
root = None
root = add(root, "Podgorica", 1000)
root = add(root, "Niksic", 500)
root = add(root, "Danilovgrad", 10)
root = add(root, "Spuz", 25)
root = add(root, "Budva", 1000)

# Testiranje funkcija
print(min_visitors(root))
print(filter_by_visitors(root, 400))
print(num_visitors(root))
print(num_destinations(root))
print(filter_by_average_visitors(root))
print(dests_smaller_than_root(root))
print()
levelorder(root, 2)
print()
preorder(root)