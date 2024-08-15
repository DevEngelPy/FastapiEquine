from fastapi import APIRouter, Path
from schemas.Buys.product import Product_purchase
from schemas.Buys.validation_values.product import Product_validate
from scripts.busqueda_db import busquedaDB
router = APIRouter(
    prefix='/Product',
    tags=['Products']
)
'''
DATA 
'''
data_storach = [
    {
        'id':1,
        'name':'Corazon',
        'price':'100',
        'acount':'100',
        'total':'100'
    },
     {
        'id':2,
        'name':'Medula',
        'price':'100',
        'acount':'100',
        'total':'100'
    },

]
'''
GETS
trabajando con los filtrados
'''
@router.get('/get_product/{id}')
async def get_one_product(id:int = Path(ge=0, le=1000)):#path es un validador por url
    try:
        return busquedaDB(data_storach, 'id',id)
    except Exception as e:
        return {'Error':e}


@router.get('/get_product_name/{name}')
async def get_name_product(name:Product_validate):
    return busquedaDB(data_storach,'name',name)

@router.get('/get_product')
async def get_products():
    return data_storach

'''
POST
'''
@router.post('/create_product')
async def created_Products(product:Product_purchase):
   new_product = product.dict()
   value_exist = busquedaDB(data_storach,'id',new_product['id'])
   if value_exist:
       return {'error':'este reguistro ya existe'}
   else:
        data_storach.append(new_product)
        return {'creado':new_product}