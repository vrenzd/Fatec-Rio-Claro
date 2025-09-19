class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaLigada:
    def __init__(self):
        self.head = None
        self.count = 0

    def adicionar(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1

    def buscar(self, valor, atributo=None):
        current = self.head
        while current:
            if atributo:
                if getattr(current.data, atributo) == valor:
                    return current.data
            else:
                if current.data == valor:
                    return current.data
            current = current.next
        return None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return self.count

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

