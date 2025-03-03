from app.db.neo4j_connection import neo4j_conn


def fetch_graph_data():
    query = """
    MATCH (s:Service)-[r:CALLS]->(d:Service)
    RETURN s.name AS source, d.name AS destination, 
           r.method AS method, r.type AS type, 
           r.calls AS calls, r.avg_duration AS avg_duration
    """
    try:
        result = neo4j_conn.query(query)
        return [{"source": record["source"], "destination": record["destination"],
                 "method": record.get("method", "Unknown"), "type": record.get("type", "Unknown"),
                 "calls": record.get("calls", 0), "avg_duration": record.get("avg_duration", 0)}
                for record in result]
    except Exception as e:
        return {"status": "error", "message": f"Neo4j query failed: {str(e)}"}
