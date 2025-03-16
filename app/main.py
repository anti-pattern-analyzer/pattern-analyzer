from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.db.neo4j_connection import neo4j_conn
from app.routes.graph import router as graph_router
from app.routes.patterns import router as patterns_router

app = FastAPI(title="Microservice Anti-Pattern Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(graph_router, prefix="/api/graph")
app.include_router(patterns_router, prefix="/api/anti-patterns")


@app.on_event("startup")
async def startup():
    print("🔄 Initializing database connections...")
    try:
        neo4j_conn.connect()
        print("✅ Databases connected successfully!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        raise e


@app.on_event("shutdown")
async def shutdown():
    print("🛑 Closing database connections...")
    neo4j_conn.close()
    print("✅ Databases closed successfully!")


@app.get("/")
async def root():
    return {"message": "Anti-Pattern Analyzer API is running!"}
