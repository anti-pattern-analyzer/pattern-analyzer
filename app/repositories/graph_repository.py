from app.db.neo4j_connection import neo4j_conn


def fetch_graph_data():
    """Fetch detailed service-to-service interactions with method-level details."""
    query = """
    MATCH (s:Service)-[r:CALLS]->(d:Service)
    RETURN s.name AS source, d.name AS destination, 
           r.method AS method, r.type AS type, 
           r.calls AS calls, r.avg_duration AS avg_duration
    """
    try:
        result = neo4j_conn.query(query)
        return [{"source": record["source"], "destination": record["destination"],
                 "method": record["method"], "type": record["type"],
                 "calls": record["calls"], "avg_duration": record["avg_duration"]}
                for record in result]
    except Exception as e:
        return {"status": "error", "message": f"Neo4j query failed: {str(e)}"}


def fetch_graph_summary():
    """Fetch high-level system overview for React-D3 graph."""
    query = """
    MATCH (s:Service)-[r:CALLS]->(d:Service)
    RETURN s.name AS source, d.name AS destination, r.calls AS weight
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
                "weight": record["weight"]
            })

        return {
            "nodes": [{"id": node} for node in nodes],
            "links": links
        }
    except Exception as e:
        return {"status": "error", "message": f"Neo4j query failed: {str(e)}"}
