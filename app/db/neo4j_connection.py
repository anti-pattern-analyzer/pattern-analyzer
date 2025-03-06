import os
from neo4j import GraphDatabase


class Neo4jConnection:
    def __init__(self):
        self._uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self._user = os.getenv("NEO4J_USERNAME", "neo4j")
        self._password = os.getenv("NEO4J_PASSWORD", "H7t-YFBxjSBWxIFnhO7OaGAjKwk6c-q5wxq_yP95E1M")
        self._driver = None

    def connect(self):
        if self._driver is None:
            self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password))
            self._driver.verify_connectivity()
            print("✅ Connected to Neo4j!")

    def close(self):
        if self._driver is not None:
            self._driver.close()
            self._driver = None
            print("✅ Closed Neo4j connection!")

    def query(self, query, params={}):
        with self._driver.session() as session:
            return list(session.run(query, params))


neo4j_conn = Neo4jConnection()
