using System;

public class TreeSearch
{
    private class TreeNode
    {
        public int Value;
        public TreeNode Left;
        public TreeNode Right;

        public TreeNode(int value)
        {
            Value = value;
            Left = Right = null;
        }
    }

    private TreeNode root;

    public TreeSearch()
    {
        root = null;
    }

    //Einfügen in den Baum
    public void Insert(int value)
    {
        if (root == null)
        {
            root = new TreeNode(value);
        }
        else
        {
            InsertRec(root, value);
        }
    }

    private void InsertRec(TreeNode node, int value)
    {
        if (value < node.Value)
        {
            if (node.Left == null)
                node.Left = new TreeNode(value);
            else
                InsertRec(node.Left, value);
        }
        else
        {
            if (node.Right == null)
                node.Right = new TreeNode(value);
            else
                InsertRec(node.Right, value);
        }
    }

    //Suchen im Baum
    public bool Search(int value)
    {
        return SearchRec(root, value);
    }

    private bool SearchRec(TreeNode node, int value)
    {
        if (node == null) return false;
        if (node.Value == value) return true;
        return value < node.Value ? SearchRec(node.Left, value) : SearchRec(node.Right, value);
    }

    public static void Main(string[] args)
    {
        TreeSearch tree = new TreeSearch();
        tree.Insert(10);
        tree.Insert(5);
        tree.Insert(15);
        tree.Insert(3);
        tree.Insert(7);

        Console.WriteLine("Suche 5: " + tree.Search(5));   
        Console.WriteLine("Suche 7: " + tree.Search(7));   
        Console.WriteLine("Suche 20: " + tree.Search(20));  
        Console.WriteLine("Suche 10: " + tree.Search(10));  
        Console.WriteLine("Suche 3: " + tree.Search(3));   
    }
}
