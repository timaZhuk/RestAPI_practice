import uvicorn  #ASGY
from fastapi import FastAPI


# Craete the API object
app = FastAPI()

# index objects opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message':'Hello, stranger'}

# Route with  single parameter, returns the parameter within a message
# Located at http://127.0.0.1:8000/anyName
@app.get('/Welcome')
def get_name(name:str):
    return {'Welcome To Krish YoutubeChannel':f'{name}'}

# HOw to run the server
# Run API with uvicorn
# will run on http://127.0.0.1:8002/
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port =8002)
#uvicorn main:app --reload




