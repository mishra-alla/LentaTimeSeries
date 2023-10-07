import pandas as pd
import numpy as np
import pandas as pd
import pickle

def forecast(sales: dict, item_info: dict, store_info: dict) -> list:
    """
    Функция для предсказания продажЖ
    :params sales: исторические данные по продажам
    :params item_info: характеристики товара
    :params store_info: характеристики магазина
    """
     
    # Загрузка модели
    try:
        with open('app/pickle_model/model.pcl', 'rb') as fid:
            model = pickle.load(fid)

    
    """
    sales = [el["sales_units"] for el in sales]
    mean_sale = sum(sales) / len(sales)
    return [mean_sale] * 5
