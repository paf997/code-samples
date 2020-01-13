/**
 * Paolo Fenu, 10281648, paf997
 * CMPT 306, Individual project, U of S
 * December 2nd, 2019
 *
 * World map PCG. This algorithm is an based on a PCG originially given in class
 * @ aurthor Jason Bowey
 * */

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PCGWorld : MonoBehaviour
{
    // This will store the game tiles (Phenotype)
    private Dictionary<Vector2Int, GameObject> tiles;
    // This will store the underlying data structure (Genotype)
    public Dictionary<Vector2Int, float> data;

    //The various region  and border tile
    [SerializeField]
    GameObject plainsTile;
    [SerializeField]
    GameObject forestTile;
    [SerializeField]
    GameObject oceanTile;
    [SerializeField]
    GameObject dessertTile;
    [SerializeField]
    GameObject mountainsTile;
    [SerializeField]
    GameObject deepOcean;
    [SerializeField]
    GameObject snow;
    [SerializeField]
    GameObject town;
    [SerializeField]
    GameObject border;

    public GameObject player;
    private GameObject p; // instantiated player prefab

    public Vector2[] towns = new Vector2[10]; 
    private int towncount = 10;
    private bool enoughDistance; // used when determining whether a randomly generated town is within the minimum amount of distance 

    // The map deminsions
    private int width = 100;
    private int height = 100;

    // used to generate different perlin noise values and combine them
    public int octave = 3;

    // A value that will increase the number of details based on the number or octaves.
    // The higher the  feature value, the higher the frencuecy produced with each subsequent octave
    private float features= 4.0f;  
    private float featureEffect = .18f;
    private float scale = 22.03f;

    private void Awake()
    {
        towncount = towns.Length;
        // Create the data structures 
        tiles = new Dictionary<Vector2Int, GameObject>();
        data = new Dictionary<Vector2Int, float>();

        data = GenerateModel();
        LoadTiles();
    }

    // Despawns the level and then spawns everything based on the most recent data model
    public void LoadTiles()
    {
        //UnloadTiles();
        GameObject tile;

        // Based on perlin noise values, different region tile will be genereated
        foreach (Vector2Int i in data.Keys)
        {
            if (i.x == 0 || i.y == 0 || i.x == height - 1 || i.y == height - 1)
            {
                // spawn black tile at this location
                tile = Instantiate(border, (Vector2)i, Quaternion.identity) as GameObject;
                if (!tiles.ContainsKey(i))
                    tiles.Add(i, tile);
            }

            else if (data[i] >= .0 && data[i] < .1)
            {
                // spawn black tile at this location
                tile = Instantiate(deepOcean, (Vector2)i, Quaternion.identity) as GameObject;
                if (!tiles.ContainsKey(i))
                    tiles.Add(i, tile);
            }
            else if (data[i] >= .1 && data[i] < .4)
            {
                // spawn black tile at this location
                tile = Instantiate(oceanTile, (Vector2)i, Quaternion.identity) as GameObject;
                if (!tiles.ContainsKey(i))
                    tiles.Add(i, tile);

            }
            else if (data[i] >= .4 && data[i] < .45)
            {
                // Randomly generate towns on plain and coastal regions
                if (Random.RandomRange(0, 100) > 70 && towncount > 0)
                {
                    townGeneration(i);

                    // Check for a minimum distance between town
                    if (enoughDistance)
                    {
                        tile = Instantiate(town, (Vector2)i, Quaternion.identity) as GameObject;
                        if (!tiles.ContainsKey(i))
                            tiles.Add(i, tile);
                        Debug.Log("Adding " + i);
                        towns[towncount - 1] = (Vector2)i;
                        towncount--;
                        enoughDistance = false;
                    }

                    else
                    {
                        // spawn white tile at this location
                        tile = Instantiate(dessertTile, (Vector2)i, Quaternion.identity) as GameObject;
                        if (!tiles.ContainsKey(i))
                            tiles.Add(i, tile);
                    }
                }
                else
                {
                    // spawn white tile at this location
                    tile = Instantiate(dessertTile, (Vector2)i, Quaternion.identity) as GameObject;
                    if (!tiles.ContainsKey(i))
                        tiles.Add(i, tile);
                }
            }

            else if (data[i] >= .45 && data[i] < .7)
            {
                // Randomly generate towns on plain and coastal regions
                if (Random.RandomRange(0, 100) > 70 && towncount > 0)
                {
                    townGeneration(i);

                    // Check for a minimum distance between town
                    if (enoughDistance)
                    {
                        tile = Instantiate(town, (Vector2)i, Quaternion.identity) as GameObject;
                        if (!tiles.ContainsKey(i))
                            tiles.Add(i, tile);
                        Debug.Log("Adding " + i);
                        towns[towncount - 1] = (Vector2)i;
                        towncount--;
                        enoughDistance = false;
                    }

                    else
                    {
                        // spawn white tile at this location
                        tile = Instantiate(plainsTile, (Vector2)i, Quaternion.identity) as GameObject;
                        if (!tiles.ContainsKey(i))
                            tiles.Add(i, tile);
                    }
                }
                else
                {
                    // spawn white tile at this location
                    tile = Instantiate(plainsTile, (Vector2)i, Quaternion.identity) as GameObject;
                    if (!tiles.ContainsKey(i))
                        tiles.Add(i, tile);
                }
            }
            else if (data[i] >= .7 && data[i] < .8)
            {
                // spawn white tile at this location
                tile = Instantiate(forestTile, (Vector2)i, Quaternion.identity) as GameObject;
                if (!tiles.ContainsKey(i))
                    tiles.Add(i, tile);

            }

            else if (data[i] >= .8 && data[i] < .92)
            {
                // spawn black tile at this location
                tile = Instantiate(mountainsTile, (Vector2)i, Quaternion.identity) as GameObject;
                if (!tiles.ContainsKey(i))
                    tiles.Add(i, tile);
            }

            else
            {
                // spawn white tile at this location
                tile = Instantiate(snow, (Vector2)i, Quaternion.identity) as GameObject;
                if (!tiles.ContainsKey(i))
                    tiles.Add(i, tile);
            }
        }

        Vector2 position = towns[9]; // the first town will always be generated
        p = Instantiate(player, position, Quaternion.identity); // the player starts at the first town
    }

    // Despawns the level
    public void UnloadTiles()
    {
        foreach (Vector2Int coord in tiles.Keys)
        {
            GameObject go = tiles[coord];
            Destroy(go);
        }
        tiles.Clear();
    }

    // If model gen is happening in a different script or GameObject, use this to set the model
    public void SetModel(Dictionary<Vector2Int, float> model)
    {
        data = model;
    }

    // Generate a new model for the level

    /**
     * The main algorithm for map generation.  Each coordinate is given a perlin noise value
     * A random seed value is generated to ensure variability
     */

    public Dictionary<Vector2Int, float> GenerateModel()
    {
        Dictionary<Vector2Int, float> tmp_model = new Dictionary<Vector2Int, float>();

        int seed = Random.RandomRange(1, 100000);
        Vector2 offset;
        offset.x = 5;
        offset.y = 3;

        float[,] noiseMap = new float[width, height];

        System.Random prng = new System.Random(seed);
        Vector2[] octaveOffsets = new Vector2[octave];
        for (int i = 0; i < octave; i++)
        {
            float offsetX = prng.Next(-100000, 100000) + offset.x;
            float offsetY = prng.Next(-100000, 100000) + offset.y;
            octaveOffsets[i] = new Vector2(offsetX, offsetY);
        }

        float maxNoiseHeight = float.MinValue;
        float minNoiseHeight = float.MaxValue;

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                // noise along the x axis
                float amplitude = 1.0f;

                // noise along the y axis
                float frequency = 1.0f;

                float noiseHeight = 0;

                for (int i = 0; i < octave; i++)
                {
                    // vary the values bases on current octave
                    float scaledX = x / scale * frequency + octaveOffsets[i].x;
                    float scaledY = y / scale * frequency + octaveOffsets[i].y;

                    float pn = Mathf.PerlinNoise(scaledX, scaledY) * 2 - 1; //get perlin noise value 
                    noiseHeight += pn * amplitude; // multiply value by each subsequent map value from new octave
                    amplitude *= featureEffect; 
                    frequency *= features;
                }

                if (noiseHeight > maxNoiseHeight)
                {
                    maxNoiseHeight = noiseHeight;
                }
                else if (noiseHeight < minNoiseHeight)
                {
                    minNoiseHeight = noiseHeight;
                }
                else { }

                noiseMap[x, y] = noiseHeight;
            }//for 
        }//for y

        // normalize all values 
        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                noiseMap[x, y] = Mathf.InverseLerp(minNoiseHeight, maxNoiseHeight, noiseMap[x, y]);
                //Debug.Log("Let's tyr this" + noiseMap[x, y]);

                Vector2Int coord = new Vector2Int(y, x);

                if (!tmp_model.ContainsKey(coord))
                {
                    tmp_model.Add(coord, noiseMap[x, y]);
                }
            }
        }
        return tmp_model;
    }

    // Allow quick reload of level for testing
    // This should be removed in a real game context
    public void Update()
    {
        if (Input.GetKeyDown(KeyCode.R))
        {
            Destroy(p);
            System.Array.Clear(towns, 0, towns.Length - 1);
            towncount = towns.Length;
            UnloadTiles();
            data = GenerateModel();
            LoadTiles();
        }
    }

    //  Destroy/Reload maps based on the push of a button
    public void MapButton()
    {
        Destroy(p);
        System.Array.Clear(towns, 0, towns.Length - 1);
        towncount = towns.Length;
        UnloadTiles();
        data = GenerateModel();
        LoadTiles();
    }

    // Used to check existing town's positions and whether a new town can be established at current coordinate
    public void townGeneration(Vector2 i)
    {
        int a = towns.Length - 1;
        do
        {
            //Debug.Log("Index yes" + a + " " + towns[a] + " " + "indices " + i + " " +
            // Mathf.Abs(i.x - towns[a].x) + " " + Mathf.Abs(i.y - towns[a].y) + " " + "The length " + towns.Length);

            // Check if each town is a minimum number of tiles away from other towns
            if (Mathf.Abs(i.x - towns[a].x) > 10 && Mathf.Abs(i.y - towns[a].y) > 10)
            {

                enoughDistance = true;
            }
            else
            {
                enoughDistance = false;
            }
            a--;
        } while (enoughDistance && a >= 0);
    }

}
