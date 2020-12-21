import uvicorn

from apps.backend.lambda_function import app


if __name__ == "__main__":
    uvicorn.run("backend:app", host="localhost", port=8000, debug=True, reload=True)
