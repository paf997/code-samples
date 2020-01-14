 package lib280.graph;
/*
* Paolo A Fenu, 10281648, paf997
* U of S, Cmpt 280, Assignment 8
 */

 //Make sure to adjust path if needed!!

//import java.io.File;
//import java.io.IOException;
//import java.util.Scanner;

 import lib280.base.Pair280;
 import lib280.exception.InvalidArgument280Exception;

 import java.util.InputMismatchException;
 import java.util.NoSuchElementException;
 import java.util.Scanner;


 public class NonNegativeWeightedGraphAdjListRep280<V extends Vertex280> extends
         WeightedGraphAdjListRep280<V> {

     public NonNegativeWeightedGraphAdjListRep280(int cap, boolean d,
                                                  String vertexTypeName) {
         super(cap, d, vertexTypeName);
     }

     public NonNegativeWeightedGraphAdjListRep280(int cap, boolean d) {
         super(cap, d);
     }

     /**
      * Replaces the current graph with a graph read from a data file.
      *
      * File format is a sequence of integers. The first integer is the total
      * number of nodes which will be numbered between 1 and n.
      *
      * Remaining integers are treated as ordered pairs of (source, destination)
      * indicies defining graph edges.
      *
      * @param fileName
      *            Name of the file from which to read the graph.
      * @precond The weights on the edges in the data file fileName are non negative.
      * @throws RuntimeException
      *             if the file format is incorrect, or an edge appears more than
      *             once in the input.
      */


     @Override
     public void setEdgeWeight(V v1, V v2, double weight) {
         // Overriding this method to throw an exception if a weight is negative will cause
         // super.initGraphFromFile to throw an exception when it tries to set a weight to
         // something negative.

         // Verify that the weight is non-negative
         if(weight < 0) throw new InvalidArgument280Exception("Specified weight is negative.");

         // If it is, then just set the edge weight using the superclass method.
         super.setEdgeWeight(v1, v2, weight);
     }

     @Override
     public void setEdgeWeight(int srcIdx, int dstIdx, double weight) {
         // Get the vetex objects associated with each index and pass off to the
         // version of setEdgeWEight that accepts vertex objects.
         this.setEdgeWeight(this.vertex(srcIdx), this.vertex(dstIdx), weight);
     }


     /**
      * Implementation of Dijkstra's algorithm.
      * @param startVertex Start vertex for the single-source shortest paths.
      * @return An array of size G.numVertices()+1 in which offset k contains the shortest
      *         path from startVertex to k.  Offset 0 is unused since vertex indices start
      *         at 1.
      */
     public Pair280<double[], int[]> shortestPathDijkstra(int startVertex) {

         // TODO Implement this method
         //move cursor before first vertex
         this.goBefore();

         //instantiate required arrays and add required values
         boolean visited [] = new boolean[this.numVertices+1];
         double distance [] = new double [this.numVertices+1];
         int pred [] = new int[this.numVertices+1];
         visited[0] = true;
         for (int i = 0; i <= numVertices(); i++){
             distance[i] = Double.POSITIVE_INFINITY;
             this.goForth();
         }

         //counter used for counting the number of vertices visited
         int count = numVertices()-1;
            //a special case outside oof main loop for the start vertex
             if(visited[startVertex] == false) {
                 visited[startVertex] = true;
                 distance[startVertex] = 0;
             }
         //used to traverse vertices
         int cur = startVertex;

             //start traversing vertices and their edges
             while(count > 0) {
                 this.goIndex(cur);
                 this.eGoFirst(this.item());

                 //used to determine if the algorithm needs to back track
                 boolean doNotGoBack = false;

                 //the previous node
                 int pre = cur;

                 //check if there are edges for the current vertex
                 while (this.eItemExists()) {
                     //check if the vertex has been visited
                     if(visited[eItem().secondItem().index()] == false) {
                         //check weight
                         if (distance[cur] + this.eItem().weight <= distance[this.eItem().secondItem().index()]) {
                             distance[this.eItem.secondItem().index()] = eItem().getWeight() + distance[pre];
                             pred[this.eItem().secondItem().index()] = pre;
                             doNotGoBack = true;
                             cur = this.eItem().secondItem().index();
                         }
                     }
                     //go to the next edge
                     this.eGoForth();
                 }
                 //start back tracking
                 if(!doNotGoBack) {
                     cur = pred[cur];
                 }else{
                     count--;
                     visited[cur] = true;
                 }
             }

         // Remove this return statement when you're ready -- it's a placeholder to prevent a compiler error.
         return new Pair280<double[], int[]>(distance, pred);
     }

     /**
      *
      * Given a predecessors array output from this.shortestPathDijkatra, return a string
      * that represents a path from the start node to the given destination vertex 'destVertex'.
      * @param predecessors
      * @param destVertex
      * @return an concatenated string representing a path from ith node to destination node
      */

     private static String extractPath(int[] predecessors, int destVertex) {
         // TODO Implement this method

         //used to traverse the predecessors array
         int cur = destVertex;

         //returned string that will be appended
         String path = "";

         //begin traversing array unless the predecessor is 0
         if(predecessors[cur] == 0){
             return "Not reachable";
         }else {
             while (predecessors[cur] > 0) {
                 String num = "" + predecessors[cur] + ",";
                 path = num.concat(path);
                 cur = predecessors[cur];
             }
         }
         return "The path is " + path +destVertex;  // Remove this when you're ready -- this is a placeholder to prevent a compiler error.
     }

     // Regression Test
     public static void main(String args[]) {
         NonNegativeWeightedGraphAdjListRep280<Vertex280> G = new NonNegativeWeightedGraphAdjListRep280<Vertex280>(1, false);

         if( args.length == 0)
             //Make sure to adjust path if needed!!
             G.initGraphFromFile("lib280/graph/weightedtestgraph.gra");
         else
             G.initGraphFromFile(args[0]);

         System.out.println("Enter the number of the start vertex: ");
         Scanner in = new Scanner(System.in);
         int startVertex;
         try {
             startVertex = in.nextInt();
         }
         catch(InputMismatchException e) {
             in.close();
             System.out.println("That's not an integer!");
             return;
         }

         if( startVertex < 1 || startVertex > G.numVertices() ) {
             in.close();
             System.out.println("That's not a valid vertex number for this graph.");
             return;
         }
         in.close();


         Pair280<double[], int[]> dijkstraResult = G.shortestPathDijkstra(startVertex);
         double[] finalDistances = dijkstraResult.firstItem();
         double correctDistances[] = {-1, 0.0, 1.0, 3.0, 23.0, 7.0, 16.0, 42.0, 31.0, 36.0};
         int[] predecessors = dijkstraResult.secondItem();

         for(int i=1; i < G.numVertices() +1; i++) {
             System.out.println("The length of the shortest path from vertex " + startVertex + " to vertex " + i + " is: " + finalDistances[i]);
 		if( correctDistances[i] != finalDistances[i] )
 				System.out.println("Length of path from to vertex " + i + " is incorrect; should be " + correctDistances[i] + ".");
 			else {
                 System.out.println(extractPath(predecessors, i));
 			}
         }
     }

 }
