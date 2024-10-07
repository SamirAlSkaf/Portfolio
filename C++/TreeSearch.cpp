#include <iostream>
#include <vector>

//Struktur
typedef struct Node {
    int value;
    std::vector<Node*> children;
    
    Node(int val) : value(val) {}
} Node;

//Funktion zur Suche
void depthFirstSearch(Node* node) {
    if (node == nullptr) return;
    
    std::cout << node->value << " ";
    
    //Rekursion für alle Kinder-Knoten
    for (Node* child : node->children) {
        depthFirstSearch(child);
    }
}

//Funktion zur Erstellung von Beispieldaten
Node* createExampleTree() {
    Node* root = new Node(1);
    root->children.push_back(new Node(2));
    root->children.push_back(new Node(3));
    root->children[0]->children.push_back(new Node(4));
    root->children[0]->children.push_back(new Node(5));
    root->children[1]->children.push_back(new Node(6));
    root->children[1]->children.push_back(new Node(7));
    return root;
}

//Funktion zum Löschen des Baums
void deleteTree(Node* node) {
    if (node == nullptr) return;
    for (Node* child : node->children) {
        deleteTree(child);
    }
    delete node;
}

int main() {
    Node* root = createExampleTree();

    //Tiefensuche 
    std::cout << "DFS Ergebnis: ";
    depthFirstSearch(root);

    
    std::cout << std::endl;

    //Speicher freigeben
    deleteTree(root);

    return 0;
}