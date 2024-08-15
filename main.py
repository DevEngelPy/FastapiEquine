from fastapi import FastAPI
import uvicorn
from routes import Product
aplication_Equine = FastAPI()
aplication_Equine.include_router(Product.router)

if __name__ == '__main__':
    uvicorn.run('main:aplication_Equine', port=8000, reload=True)