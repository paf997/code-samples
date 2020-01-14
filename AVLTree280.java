package lib280.tree;

/*
 *Paolo Fenu, 10281648, paf997
 * Cmpt 280, Assignment 4, U of S
 */

import lib280.exception.ContainerEmpty280Exception;
import lib280.exception.NoCurrentItem280Exception;

public class AVLTree280 <I extends Comparable<? super I>> extends OrderedSimpleTree280<I>{

    /** Constructor */
    public AVLTree280(){ super(); }

    /**
     *
     * @param item    The item to be placed in the new node
     * @return NodeAVL<I></I>
     */
    public NodeAVL<I> createNewNode(I item)
    {
        return new NodeAVL<I>(item);
    }

    /**
     * @override - typecast the rootNode
     * @return - typcast rootNode
     */
    public NodeAVL<I> rootNode() {
        return (NodeAVL<I>)super.rootNode();
    }

    /**
     * @pre - no duplicate items allowed. This is handled by the helper function below
     * @param x - the item to be inserted
     * @post - new item should be added to the tree while maintaining AVL prperties
     */
    public void insert(I x ){
        rootNode = insertR(x,rootNode());
    }

    /**
     * @pre - no duplicate items allowed
     * @param x - the item to be added
     * @param currentRoot - the rootNode
     * recursively traverses the tree and adds item to it if it is not already present
     * @return - NodeAVL<I>
     */
    public NodeAVL<I> insertR(I x, NodeAVL<I> currentRoot){
            NodeAVL<I> newNode = currentRoot;
            //Establish rootNode
            if (this.isEmpty()) {
                rootNode = createNewNode(x);
                newNode = rootNode();

            //create new node if no duplicate are found
            }else if(currentRoot == null)  {
                newNode = createNewNode(x);

            //check for duplicates
            }else if(x.compareTo(currentRoot.item()) == 0){
                System.out.println("Item already present");
                return currentRoot;
            }

            //keep traversing left or right based on item value
            else if (x.compareTo(currentRoot.item()) < 0)
            {
                currentRoot.setLeftNode(insertR(x, currentRoot.leftNode));
                //adjust height for inserted node
                currentRoot.setLeftHeight(currentRoot.leftNode().maxHeight() + 1);
            }else {
               // System.out.println("Going right: " + x);
                currentRoot.setRightNode(insertR(x, currentRoot.rightNode));
                currentRoot.setRightHeight(currentRoot.rightNode().maxHeight() + 1);
            }

            //Check balance
            newNode = balance(x, newNode);
            return newNode;
    }

    /**
     * @pre - cannot be empty
     * @param x the value tht will be searched for and possibly removed
     * recursively traverses the tree with the help of a helper function to possibly remove the item and
     * restore the AVL propertis
     * @post - item is removed and AVL properties are restore if need be
     */
    public void delete (I x) throws ContainerEmpty280Exception{
        if(isEmpty()){
            throw new ContainerEmpty280Exception("The tree is empty");
        }else {
            rootNode = deleteI(x, rootNode());
        }
    }

    /**
     * @pre - cannot be empty
     * @param x the value tht will be searched for and possibly removed
     * recursively traverses the tree with the help of a helper function to possibly remove the item and
     * restore the AVL propertis
     * @post - item is removed and AVL properties are restore if need be
     * @return - NodeAVL<I>
     */
    private NodeAVL<I> deleteI(I x, NodeAVL currentRoot) throws NoCurrentItem280Exception
    {
        boolean itemFound = false;
        NodeAVL<I> node = currentRoot;

        //if item isn't found...
        if (node == null) {
            return null;

        //traverse the tree until item is found
        }else if (x.compareTo(node.item()) < 0){
            node.leftNode = deleteI(x, node.leftNode());
            checkLeftHeight(node);
            checkRightHeight(node);
        }else if (x.compareTo(node.item()) > 0){
            node.setRightNode(deleteI(x, node.rightNode()));
            checkRightHeight(node);
            checkLeftHeight(node);

        // Item is found so the method needs to know how many children the node has
        }else{
            itemFound = true;
        }
        //Check if children heights have changed
        node = balanceDel(x, node);
        //Replace the current item by its inorder successor and then delete the
        // inorder successor from its original place.

        // the node has zero children
        if(itemFound && (node.rightNode() == null && node.leftNode() == null)) {
            node = null;

            // the node has a right child
        }else if(itemFound && (node.leftNode() == null && node.rightNode() != null)) {
            node = node.rightNode();

            // the node has a left child
        }else if(itemFound && (node.leftNode() != null && node.rightNode() == null)) {
            node = node.leftNode();

            // the node has two children. Find inorder successor beginning with the node's right child
        }else if(itemFound && (node.leftNode() != null && node.rightNode() != null )){
            NodeAVL<I> successorRight = node.rightNode();
            NodeAVL<I> successorLeft = successorRight.leftNode();

            //no need to continue further left
            if(successorLeft == null) {
                node.setItem(successorRight.item());
                node.setRightNode(successorRight.rightNode);
                checkRightHeight(node);
                checkLeftHeight(node);

            //traverse all the way left
            }else{
                successorRight.leftNode = successor(node, successorLeft);
                checkRightHeight(successorRight);
                checkLeftHeight(successorRight);
                checkRightHeight(node);
                checkLeftHeight(node);
            }
        }else{ }
        return node;
    }

    /**
     *
     * @param replacement - the node to be replaced by the successor
     * @param N - the node traversing left for the successor
     * @return - NodeAVL<I></I>
     */
    private NodeAVL<I> successor(NodeAVL<I> replacement, NodeAVL<I> N){
        NodeAVL<I> node = N;
        if (N.leftNode() != null){
            node.leftNode = successor(replacement,node.leftNode());
        }else{
            replacement.setItem(node.item());
            return deleteI(node.item(),node);
        }

        //adjust heights after deletion
        checkLeftHeight(node);
        checkRightHeight(node);
        node = balance(rootNode().item(),node);
        return node;
    }

    /**
     *
     * @param x - the value of the item being added
     * @param N - the node that needs it's balace checked
     * checks the balance of the current node and make the required rotations and updates heights
     * @return - NodeAVL<I> the node to be returned after any needed rotations
     */
    private NodeAVL<I> balance (I x,NodeAVL<I> N){
        NodeAVL<I> newNode = N;
        int balance = difference(newNode);

        //Correct any imbalance if needed

        //Left,Left imbalance
        if (balance > 1 && x.compareTo(newNode.leftNode.item())<0){
            System.out.println("Left, Left  imbalance at: " + newNode.item());
            newNode = rotateRight(newNode);
            newNode.rightNode().setLeftHeight(newNode.getRightHeight());
            newNode.setRightHeight(newNode.rightNode().maxHeight() +1 );

        //right, right imbalance
        }else if(balance < -1 && x.compareTo(newNode.rightNode.item())>0 ) {
            System.out.println("Right, Right imbalance " + newNode.item());
            newNode = rotateLeft(newNode);
            newNode.leftNode().setRightHeight(newNode.getLeftHeight());
            newNode.setLeftHeight(newNode.leftNode().maxHeight() +1 );

        //left, right imbalance
        }else if(balance > 1 && x.compareTo(newNode.leftNode.item())>0){
            System.out.println("Left, Right imbalance at: " + newNode.item());
            newNode.leftNode = rotateLeft(newNode.leftNode());
            newNode.leftNode().leftNode().setRightHeight(newNode.leftNode().getLeftHeight());
            newNode.leftNode().setLeftHeight(newNode.leftNode().leftNode().maxHeight() +1);
            newNode = rotateRight(newNode);
            newNode.rightNode().setLeftHeight(newNode.getRightHeight());
            newNode.setRightHeight(newNode.rightNode().maxHeight() +1 );

        //right, left imbalance
        }else if (balance < -1 && x.compareTo(newNode.rightNode.item())<0){
            System.out.println(" Right, Left  imbalance " + newNode.item());
            newNode.rightNode = rotateRight(newNode.rightNode());
            newNode.rightNode().rightNode().setLeftHeight(newNode.rightNode().getRightHeight());
            newNode.rightNode().setRightHeight(newNode.rightNode().rightNode().maxHeight() +1);
            newNode = rotateLeft(newNode);

            newNode.leftNode().setRightHeight(newNode.getLeftHeight());
            newNode.setLeftHeight(newNode.leftNode().maxHeight() +1 );
        }else{
        }
        return newNode;
        }

    /**
     *
     * @param newNode
     * a helper function to the determine the difference between left and right subtree
     * @return int - the difference between left and right subtrees
     */
    private int difference(NodeAVL<I> newNode){
        return (newNode.getLeftHeight() - newNode.getRightHeight());
    }

    /**
     *
     * @param x - the value of the item being deleted
     * @param N - the node that needs it's balance checked
     * checks the balance of the current node and make the required rotations and updates heights
     * @return - NodeAVL<I> the node to be returned after any needed rotations
     */
    private NodeAVL<I> balanceDel (I x,NodeAVL<I> N){
        NodeAVL<I> newNode = N;
        int balance = difference(newNode);

        //Correct any imbalance if needed

        if (balance > 1 && difference(newNode.leftNode())>=0){
            System.out.println("Left imbalance at: " + newNode);
            newNode = rotateRight(newNode);
            newNode.rightNode().setLeftHeight(newNode.getRightHeight());
            newNode.setRightHeight(newNode.rightNode().maxHeight() +1 );

        }else if(balance < -1 && difference(newNode.rightNode())<=0) {
            System.out.println("Right Right imbalance");
            newNode = rotateLeft(newNode);
            newNode.leftNode().setRightHeight(newNode.getLeftHeight());
            newNode.setLeftHeight(newNode.leftNode().maxHeight() +1 );

        }else if(balance > 1 && difference(newNode.leftNode())<0){
            System.out.println("Left, Right imbalance at: " + newNode.item());
            newNode.leftNode = rotateLeft(newNode.leftNode());
            newNode.leftNode().leftNode().setRightHeight(newNode.leftNode().getLeftHeight());
            newNode.leftNode().setLeftHeight(newNode.leftNode().leftNode().maxHeight() +1);
            newNode = rotateRight(newNode);
            newNode.rightNode().setLeftHeight(newNode.getRightHeight());
            newNode.setRightHeight(newNode.rightNode().maxHeight() +1 );


        }else if (balance < -1 && difference(newNode.rightNode())>0){
            System.out.println(" Right, Left  imbalance");
            newNode.rightNode = rotateRight(newNode.rightNode());
            newNode.rightNode().rightNode().setLeftHeight(newNode.rightNode().getRightHeight());
            newNode.rightNode().setRightHeight(newNode.rightNode().rightNode().maxHeight() +1);
            newNode = rotateLeft(newNode);
            newNode.leftNode().setRightHeight(newNode.getLeftHeight());
            newNode.setLeftHeight(newNode.leftNode().maxHeight() +1 );
        }else{ }
        return newNode;
    }

    /**
     *
     * @param criticalN - the node that needs to be rotated
     * @return - NodeAVL<I> the "next " node after rotations
     */
    private NodeAVL<I> rotateRight(NodeAVL<I> criticalN){
        NodeAVL<I> criticalLeft = criticalN.leftNode();
        NodeAVL<I> temp2 =  criticalLeft.rightNode();
        criticalLeft.setRightNode(criticalN);
        criticalN.setLeftNode(temp2);
        return criticalLeft;
    }

    /**
     *
     * @param criticalN - the node that needs to be rotated
     * @return - NodeAVL<I> the "next " node after rotations
     */
    private NodeAVL<I> rotateLeft(NodeAVL<I> criticalN){
        NodeAVL<I> criticalRight = criticalN.rightNode();
        NodeAVL<I> temp2 =  criticalRight.leftNode();
        criticalRight.setLeftNode(criticalN);
        criticalN.setRightNode(temp2);
        return criticalRight;
    }

    /**
     *
     * @param node
     * used to determine new heights after addditions, deletion and rotations
     * @return- NodeAVL<I> with adjusted height
     */
    private NodeAVL<I> checkRightHeight(NodeAVL<I> node){
        if(node.rightNode() != null && node.getRightHeight() != node.rightNode().maxHeight() +1){
            node.setRightHeight(node.getRightHeight() - 1);
        }else if(node.rightNode == null){
            node.setRightHeight(0);
        }
        else{}
        return node;
    }
    /**
     *
     * @param node
     * used to determine new heights after addditions, deletion and rotations
     * @return- NodeAVL<I> with adjusted height
     */
    private NodeAVL<I> checkLeftHeight(NodeAVL<I> node){
        if(node.leftNode() != null && node.getLeftHeight() != node.leftNode().maxHeight()+1) {
            node.setLeftHeight(node.getLeftHeight() - 1);
        }else if(node.leftNode == null){
            System.out.println("Set left height to 0. At " + node.item());
            node.setLeftHeight(0);
        }else{ }
        return node;
    }

    /**
     *
     * @param node
     * used to verify Node heights and proper ordering
     */
        public void inorder(NodeAVL<I> node){
            if(node.leftNode() != null){
                inorder(node.leftNode());
            }
            System.out.println(node.item() + "LH: " + node.getLeftHeight() + " RH: " + node.getRightHeight());
            if(node.rightNode() != null){
                inorder(node.rightNode());
            }
        }

    public static void main(String [] args){
        AVLTree280<Integer> tree = new AVLTree280<>();

        System.out.println("Insert 50,70 then 100 and expect a Right, Right imbalance at 50");
        tree.insert(50);
        tree.insert(70);
        tree.insert(100);
        System.out.println(tree.toStringByLevel());

        System.out.println("Insert 105 then 104 and expect a Right, Left imbalance at 100");
        tree.insert(105);
        tree.insert(104);
        System.out.println(tree.toStringByLevel());

        System.out.println("Insert 40 then 30 and expect a Left, Left imbalance at 50");
        tree.insert(40);
        tree.insert(30);
        System.out.println(tree.toStringByLevel());

        System.out.println("Insert 45 then 48 and expect a Left, Right imbalance at 50 ");
        tree.insert(45);
        tree.insert(48);
        System.out.println(tree.toStringByLevel());

        System.out.println("Continue testing rotations at deeper levels");
        System.out.println("Insert 85 then 86 and expect a left, right imbalance at 100");
        tree.insert(85);
        tree.insert(86);
        System.out.println(tree.toStringByLevel());

        System.out.println("Insert 110 then 120. Expect right, right imbalance at 105");
        tree.insert(110);
        tree.insert(120);
        System.out.println(tree.toStringByLevel());

        System.out.println("Insert 20 then 10. Expect a left, left imbalance at 30");
        tree.insert(20);
        tree.insert(10);
        System.out.println(tree.toStringByLevel());

        System.out.println("Try to insert duplicates. 20 and 85. Expect no changes");
        tree.insert(20);
        tree.insert(85);
        System.out.println(tree.toStringByLevel());

        System.out.println("Check ordering and heights");
        tree.inorder(tree.rootNode());

        System.out.println("Practice deletions.  Delete a node 104 with two children . No imbalance expected. ");
        System.out.println("105 should replace 104 ");
        tree.delete(104);
        System.out.println(tree.toStringByLevel());

        System.out.println("Try deleting a nodes (1, 1000) not present. Should be no change");
        tree.delete(1);
        System.out.println(tree.toStringByLevel());

        System.out.println("Delete a node 86 with two children and finding an inorder successor with " +
                "a right child . No imbalance expected. ");
        System.out.println("100 should replace 86 ");
        tree.delete(86);
        System.out.println(tree.toStringByLevel());

        System.out.println("Delete a nodes 120 and 100. Expect left, left, imbalance at 105");
        tree.delete(120);
        tree.delete(110);
        System.out.println(tree.toStringByLevel());

        System.out.println("Delete node 20 with two children on left side. 30 should replace 20 ");
        tree.delete(20);
        System.out.println(tree.toStringByLevel());

        System.out.println("Delete nodes 30, 20. This should cause a right, right imbalance at 40");
        tree.delete(10);
        tree.delete(30);
        System.out.println(tree.toStringByLevel());

        System.out.println("Delete node 50. This should cause a left, right imbalance at node 48");
        tree.delete(50);
        System.out.println(tree.toStringByLevel());

        System.out.println("Add 86 then delete a node 105. This should cause a right, left imbalance at node 100");
        tree.insert(86);
        System.out.println(tree.toStringByLevel());
        tree.delete(105);
        System.out.println(tree.toStringByLevel());

        System.out.println("Delete root node. Expect new root to be 85");
        tree.delete(70);
        System.out.println(tree.toStringByLevel());

        System.out.println("Delete root node. Expect new root to be 86");
        tree.delete(85);
        System.out.println(tree.toStringByLevel());

        System.out.println("Delete root node. Expect left imbalance and new root to be 45");
        tree.delete(100);
        System.out.println(tree.toStringByLevel());

        System.out.println("Check ordering and heights");
        tree.inorder(tree.rootNode());

    }
}
