#include <iostream>

template<typename T>
class DoubleLinkedNode {

public: 

    typedef DoubleLinkedNode<T> * pType;

    T key;
    pType prev;
    pType next;

public:

    DoubleLinkedNode(T _key)
    {
        key = _key;
        prev = 0;
        next = 0;
    }

    template<typename U>
    friend std::ostream & operator<<(std::ostream &, DoubleLinkedNode<U> &); 
};


template<typename U> 
std::ostream & operator<<(std::ostream &out, DoubleLinkedNode<U>& node)
{
    if (node.prev)
        out << node.prev->key;
    else
        out << "null";
    out << " -> " << node.key << " -> ";
    if (node.next)
        out << node.next->key;
    else
        out << "null";
    out << "\n";
    return out;
}


template<typename T>
class DoubleLinkedList {

public:

    typedef typename DoubleLinkedNode<T>::pType pType;

private:

    pType head;

public:

    DoubleLinkedList()
    {
        head = 0;
    }

    ~DoubleLinkedList()
    {
        pType node = head;
        while(node) 
        {
            pType temp = node;
            node = node->next;
            delete temp;
        }
    }

    pType find(T key)
    {
        pType node = head;
        while(node and node->key != key)
            node = node->next;
        return node;
    }

    void insert(pType node) 
    {
        node->next = head;
        if (head)
            head->prev = node;
        head = node;
        node->prev = 0;
    }

    void remove(pType node)
    {
        if (node->prev)
            node->next->prev = node->prev;
        else
            head = node->next;
        if (node->next)
            node->prev->next = node->next;
        delete node;
    }

    template<typename U>
    friend std::ostream & operator<<(std::ostream &, DoubleLinkedList<U> &);  

};


template<typename U>
std::ostream & operator<<(std::ostream & out, DoubleLinkedList<U> & L)
{
    typename DoubleLinkedList<U>::pType node = L.head;
    while(node)
    {
        out << node->key << std::endl;
        node = node->next;
    }
    return out;
}


int main() 
{
    DoubleLinkedList<int> L;

    L.insert(new DoubleLinkedNode<int>(1));

    L.insert(new DoubleLinkedNode<int>(3));

    L.insert(new DoubleLinkedNode<int>(5));

    std::cout << L;

    std::cout << *(L.find(1));

    return 0;
}

