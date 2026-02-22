from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allow all origins or specify a list of allowed origins
    allow_credentials=True,
    allow_methods=['*'],  # Allow all methods or specify a list of allowed methods
    allow_headers=['*'],  # Allow all headers or specify a list of allowed headers
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
