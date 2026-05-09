from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="The Builder Forge API", version="0.1.0")


@app.get("/")
def home():
    return {"message": "The Builder Forge is online.",
            "version": "0.1.0"
            }


@app.get("/health")
def health():
    return {"status": "ok",
            "timestamp": datetime.now(timezone.utc).isoformat()
            }


@app.get("/about")
def about():
    return {"project": "The Builder Forge",
            "builder": "Dylan",
            "stack": ["Python", "FastAPI", "Pandas", "Numpy", "Scikit-learn", "Matplotlib", "Seaborn"]
            }
