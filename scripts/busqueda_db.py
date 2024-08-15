def busquedaDB(db, data_1, data_2):
    return [product for product in db if product[f'{data_1}'] == data_2]