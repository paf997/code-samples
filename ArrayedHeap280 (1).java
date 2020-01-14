package lib280.tree;

/*
 *Paolo Fenu, 10281648, paf997
 * Cmpt 280, Assignment 4, U of S
 */

import lib280.base.Dispenser280;
import lib280.exception.ContainerFull280Exception;
import lib280.exception.DuplicateItems280Exception;
import lib280.exception.NoCurrentItem280Exception;

public class ArrayedHeap280 <I extends Comparable<? super I>> extends ArrayedBinaryTree280<I>
        implements Dispenser280<I> {
    /**
     *
     * @param cap - the maximum size of the heap
     * @ override - typecast comparable array
     */
    public ArrayedHeap280(int cap){
        super(cap);
        items = (I[]) new Comparable[capacity+1];
    }

    /**
     * pre - the heap cannot be full
     * @param x item to be inserted into the data structure
     * @throws ContainerFull280Exception
     * @throws DuplicateItems280Exception
     * Inserts new item and maintains heap properties
     * post - count is increased by 1
     *
     */
    public void insert(I x) throws ContainerFull280Exception, DuplicateItems280Exception{
        if(isFull()){
            throw new ContainerFull280Exception("The heap is full");
        }
        count ++;
        this.items[count] = x;
        currentNode = count;
        while(currentNode!= 1 && items[currentNode].compareTo(items[findParent(currentNode)]) > 0){
            currentNode =  swap(currentNode, findParent(currentNode));
        }
    }

    /**
     *
     * @param node - the index of the currentNode
     * a helper function that searches for the biggest value sibling if there is one
     * @return int - the new index for the cursor as we restore the heap properties
     */
    private int bigSibling(int node){
        int index = node;
        if(findLeftChild(node) <= count){
            if(items[node].compareTo(items[findLeftChild(node)]) <= 0){
                index = findLeftChild(node);
            }
        }
        if(findRightChild(node) <= count){
            if(items[index].compareTo(items[findRightChild(node)]) <= 0){
                index = findRightChild(node);
            }
        }
        return index;
    }

    /**
     * pre - heap cannnot be empty
     * @throws NoCurrentItem280Exception
     * post - item is removed and count is reduce by one
     */
    public void deleteItem() throws NoCurrentItem280Exception{
        if(isEmpty()){
            throw new NoCurrentItem280Exception("Heap is empty");
        }
        items[1] = items[count];
        items[count] = null;
        count --;
        if(isEmpty()){
            currentNode =0;
        }
        while (currentNode != 0 && currentNode != bigSibling(currentNode)){
            currentNode = swap(currentNode, bigSibling(currentNode));
        }

        if(count != 0) {
            currentNode = 1;
        }else{
            currentNode = 0;
        }
    }

    /**
     *
     * @param x - index of currentNode
     * @param y - the index we want the currentNode to be
     * @return - the new index of the currentNode
     */
    private int swap(int x, int y){
        I z = items[x];
        items[x] = items[y];
        items[y] = z;
        return y;
    }

    /**
     * Helper for the regression test.  Verifies the heap property for all nodes.
     */
    private boolean hasHeapProperty() {
        for(int i=1; i <= count; i++) {
            if( findRightChild(i) <= count ) {  // if i Has two children...
                // ... and i is smaller than either of them, , then the heap property is violated.
                if( items[i].compareTo(items[findRightChild(i)]) < 0 ) return false;
                if( items[i].compareTo(items[findLeftChild(i)]) < 0 ) return false;
            }
            else if( findLeftChild(i) <= count ) {  // if n has one child...
                // ... and i is smaller than it, then the heap property is violated.
                if( items[i].compareTo(items[findLeftChild(i)]) < 0 ) return false;
            }
            else break;  // Neither child exists.  So we're done.
        }
        return true;
    }
    /**
     * Regression test
     */
    public static void main(String[] args) {

        ArrayedHeap280<Integer> H = new ArrayedHeap280<Integer>(10);

        // Empty heap should have the heap property.
        if(!H.hasHeapProperty()) System.out.println("Does not have heap property.");

        // Insert items 1 through 10, checking after each insertion that
        // the heap property is retained, and that the top of the heap is correctly i.
        for(int i = 1; i <= 10; i++) {
            H.insert(i);
            System.out.println(H.item());
            if(H.item() != i) System.out.println("Expected current item to be " + i + ", got " + H.item());
            if(!H.hasHeapProperty()) System.out.println("Does not have heap property.");
        }

        // Remove the elements 10 through 1 from the heap, chekcing
        // after each deletion that the heap property is retained and that
        // the correct item is at the top of the heap.
        for(int i = 10; i >= 1; i--) {
            // Remove the element i.
            H.deleteItem();
            // If we've removed item 1, the heap should be empty.
            if(i==1) {
                if( !H.isEmpty() ) System.out.println("Expected the heap to be empty, but it wasn't.");
            }
            else {
                // Otherwise, the item left at the top of the heap should be equal to i-1.
                if(H.item() != i-1) System.out.println("Expected current item to be " + i + ", got " + H.item());
                if(!H.hasHeapProperty()) System.out.println("Does not have heap property.");
            }
        }

        System.out.println("Regression Test Complete.");
    }

}
