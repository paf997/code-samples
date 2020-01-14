package lib280.tree;

/* Paolo Fenu, 10281648, paf997
 * Cmpt 280, Assignment 4, U of S
 */
/** Extension of Binarynode to include Height for trees */
public class NodeAVL<I extends Comparable<? super I>>extends BinaryNode280<I> {


    /** The left node. */
    protected NodeAVL<I> leftNode;

    /** The right node. */
    protected NodeAVL<I> rightNode;

        /** The height of left subtree */
        protected int leftHeight;

        /** The height of right subtree */
        protected int rightHeight;


        public NodeAVL(I x){
            super(x);
            leftHeight = 0;
            rightHeight = 0;
        }

    /** Contents of the node.
     *  @timing Time = O(1) */
    public I item()
    {
        return item;
    }

    /** The left node.
     *  @timing Time = O(1) */
    public NodeAVL<I> leftNode()
    {
        return leftNode;
    }

    /** The left node.
     *  @timing Time = O(1) */
    public NodeAVL<I> rightNode()
    {
        return rightNode;
    }

    /**
     * Set the item contained in the node.
     * @param x The new item to store in the node.
     * @timing Time = O(1)
     * */
    public void setItem(I x) {
        this.item = x;
    }

    /**
     * Set the left child of this node
     * @param n The new left child of this node.
     */
    public void setLeftNode(NodeAVL<I> n) {
        this.leftNode = n;
    }

    /**
     * Set the right child of this node.
     * @param n The new right child of this node.
     */
    public void setRightNode(NodeAVL<I> n) {
        this.rightNode = n;
    }

    /**
     * Returns a string representation of the item contained within the node.
     */




        public int getLeftHeight(){
            return leftHeight;
        }

        public int getRightHeight() {
            return rightHeight;
        }

        public void setLeftHeight(int leftHeight) {

            this.leftHeight = leftHeight;

        }

        public void setRightHeight(int rightHeight) {
            this.rightHeight = rightHeight;
        }

        public int maxHeight(){
            return Math.max(getLeftHeight(), getRightHeight());
        }


        public static void main(String [] args){

        }

}
