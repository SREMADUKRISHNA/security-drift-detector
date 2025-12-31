from fastapi import FastAPI
from backend.api.routes.health import router as health_router
from backend.api.routes.drift import router as drift_router
from backend.api.routes.trends import router as trends_router
from backend import storage

app = FastAPI(title="Security Drift Detector")

# Initialize DB on startup (simple way for this requirement)
storage.init_db()

# Register Routers
app.include_router(health_router)
app.include_router(drift_router)
app.include_router(trends_router)

@app.get("/")
def root():
    return {"service": "Security-Drift-Detector", "status": "running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)