import lib280.graph.Edge280;
import lib280.graph.Vertex280;
import lib280.graph.WeightedEdge280;
import lib280.graph.WeightedGraphAdjListRep280;
import lib280.tree.ArrayedMinHeap280;

/*
 * Paolo A Fenu, 10281648, paf997
 * U of S, Cmpt 280, Assignment 8
 */

//Make sure to adjust path if needed!!

public class Kruskal {
	
	public static WeightedGraphAdjListRep280<Vertex280> minSpanningTree(WeightedGraphAdjListRep280<Vertex280> G) {

		// TODO -- Complete this method.
		//Construct heap and add items
		ArrayedMinHeap280 <WeightedEdge280<Vertex280>> heap = new ArrayedMinHeap280((G.numEdges()*G.numVertices()));
		G.goBefore();
		for(int i = 1; i <= G.numVertices(); i++){
			G.goForth();
			G.eGoFirst(G.item());
			while(!G.eAfter()){
				//This ensures that the "inverse" edges are added ie 7->1 , 1-> 7
				if(Integer.parseInt(G.eItem().firstItem().toString())< Integer.parseInt(G.eItem().secondItem().toString())) {
					heap.insert(G.eItem());
				}
				G.eGoForth();
			}
		}

		//create the graph to be returned
		WeightedGraphAdjListRep280<Vertex280> rGraph = new WeightedGraphAdjListRep280<Vertex280>(G.numVertices(),false);
		for(int i = 1; i <= G.numVertices(); i++){
			rGraph.addVertex(i);
		}

		//create the union find object
		UnionFind280 uf = new UnionFind280(G.numVertices());

		//begin removing order edges from heap and connecting edges
		while(!heap.isEmpty()){
			Edge280 edge = heap.item();

			//convert the edge indexes to integers
			int v1 = Integer.parseInt(edge.firstItem().toString());
			int v2 = Integer.parseInt(edge.secondItem().toString());

			//check if vertices are connected
			if (uf.find(v1) != uf.find(v2)){
				if(uf.find(v2) != uf.find(v1)) {
					uf.union(v1, v2);

					//connect edges in the graph being returned
					rGraph.addEdge(v1, v2);
					rGraph.setEdgeWeight(v1, v2, ((WeightedEdge280) edge).getWeight());
				}
			}
			heap.deleteItem();
		}
		return rGraph;  // Remove this when you're ready -- it is just a placeholder to prevent a compiler error.
	}
	
	public static void main(String args[]) {
		WeightedGraphAdjListRep280<Vertex280> G = new WeightedGraphAdjListRep280<Vertex280>(1, false);
		// If you get a file not found error here and you're using eclipse just remove the 
		// 'Kruskal-template/' part from the path string.
		G.initGraphFromFile("Kruskal-template/mst.graph");

		System.out.println("The graph before Kruskal's algorithm");
		System.out.println(G);
		System.out.println();

		System.out.println("Kruskal's algorithm");
		System.out.println();
		WeightedGraphAdjListRep280<Vertex280> minST = minSpanningTree(G);
		
		System.out.println(minST);


	}
}


