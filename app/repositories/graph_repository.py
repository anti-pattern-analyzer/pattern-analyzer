from app.db.neo4j_connection import neo4j_conn

def fetch_graph_data():
    query = """
    MATCH (s:Service)-[r:CALLS]->(d:Service)
    WHERE s.name IS NOT NULL AND d.name IS NOT NULL 
          AND r.calls IS NOT NULL AND r.method IS NOT NULL
          AND r.type IS NOT NULL AND r.avg_duration IS NOT NULL
    RETURN 
        s.name AS source, 
        d.name AS destination, 
        r.method AS method, 
        r.type AS type, 
        r.calls AS calls, 
        r.avg_duration AS avg_duration, 
        r.calls AS weight
    """

    try:
        result = neo4j_conn.query(query)

        nodes = set()
        links = []

        for record in result:
            nodes.add(record["source"])
            nodes.add(record["destination"])
            links.append({
                "source": record["source"],
                "target": record["destination"],
                "method": record["method"],
                "type": record["type"],
                "calls": record["calls"],
                "avg_duration": record["avg_duration"],
                "weight": record["weight"]
            })

        graph_data = {
            "nodes": [{"id": node} for node in nodes],
            "links": links
        }

        print("DEBUG: Graph Data Fetched:", graph_data)
        return graph_data

    except Exception as e:
        print(f"ERROR: Neo4j Query Failed: {str(e)}")
        return {"status": "error", "message": f"Neo4j query failed: {str(e)}"}
