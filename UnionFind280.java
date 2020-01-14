

import lib280.graph.Edge280;
import lib280.graph.GraphAdjListRep280;
import lib280.graph.Vertex280;

/*
 * Paolo A Fenu, 10281648, paf997
 * U of S, Cmpt 280, Assignment 8
 */



public class UnionFind280 {
	GraphAdjListRep280<Vertex280, Edge280<Vertex280>> G;
	
	/**
	 * Create a new union-find structure.
	 * 
	 * @param numElements Number of elements (numbered 1 through numElements, inclusive) in the set.
	 * @postcond The structure is initialized such that each element is in its own subset.
	 */
	public UnionFind280(int numElements) {
		G = new GraphAdjListRep280<Vertex280, Edge280<Vertex280>>(numElements, true);
		G.ensureVertices(numElements);		
	}
	
	/**
	 * Return the representative element (equivalence class) of a given element.
	 * @param id The elements whose equivalence class we wish to find.
	 * @return The representative element (equivalence class) of the element 'id'.
	 */
	public int find(int id) {

		// TODO - Write this method

		//used to iterate graph node
		int findIdx = id;
		G.goIndex(id);

		G.eGoFirst(G.item());

		//iterate graph nodes until there are no more outgoing noes
		while(G.eItemExists()){
			findIdx = G.eItem().secondItem().index();
			G.eGoFirst(G.item());
			G.goIndex(findIdx);
		}
		return findIdx;
	}
	
	/**
	 * Merge the subsets containing two items, id1 and id2, making them, and all of the other elemnets in both sets, "equivalent".
	 * @param id1 First element.
	 * @param id2 Second element.
	 */
	public void union(int id1, int id2) {

		//no need to add outgoing edge if the two arguments are the same
		if (find(id1) == find(id2)){
			throw new IllegalArgumentException("The two nodes are the same");
		}else{
			G.addEdge(find(id1), find(id2));
		}
		
	}
	public static void main(String args[]){
		UnionFind280 graph = new UnionFind280(5);

	}

}
