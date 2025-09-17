import requests
import configuration
import data

# Функция для создания заказа
def create_order(order_data):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDERS,  
        json=order_data,  
        headers=data.headers  
    )

# Функция для получения заказа по номеру трекера
def order_by_tracker(tracker_id):
    return requests.get(
        configuration.URL_SERVICE + configuration.ORDER_TRACK,  
        params={"t": tracker_id},  
        headers=data.headers  
    )