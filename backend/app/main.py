from fastapi import FastAPI

app = FastAPI(title='Finance Dashboard API')

@app.get('/')
def root():
    return {'message': 'Backend running'}

