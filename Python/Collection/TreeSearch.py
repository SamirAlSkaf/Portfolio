class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binärer Suchbaum
class TreeSearch:
    def __init__(self):
        self.root = None

    # Wert hinzufügen
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_rec(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_rec(node.right, value)

    # Wert suchen
    def search(self, value):
        return self._search_rec(self.root, value)

    def _search_rec(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        return self._search_rec(node.left, value) if value < node.value else self._search_rec(node.right, value)

# Beispielnutzung
if __name__ == "__main__":
    tree = TreeSearch()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)

    print("Suche 5:", tree.search(5))  # Ausgabe: True
    print("Suche 7:", tree.search(7))  # Ausgabe: True
    print("Suche 20:", tree.search(20)) # Ausgabe: False
    print("Suche 10:", tree.search(10)) # Ausgabe: True
    print("Suche 3:", tree.search(3))  # Ausgabe: True
