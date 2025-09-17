# 34 когорта Ибриков Илья
import sender_stand_request
import data


def test_create_and_fetch_order():
    # Создание нового заказа
    create_response = sender_stand_request.create_order(data.order_body)

    # Проверяем, что заказ успешно создан
    assert create_response.status_code == 201, (
        f"Ожидался статус 201 при создании заказа, "
        f"получен {create_response.status_code}"
    )

    tracker_id = create_response.json().get("track")
    assert tracker_id is not None, "В ответе на создание заказа отсутствует трек-номер"

    print(f"Заказ успешно создан. Номер трекера: {tracker_id}")

    # Получение информации о заказе по трекеру
    f_response = sender_stand_request.order_by_tracker(tracker_id)

    # Проверяем, что запрос успешен
    assert f_response.ok, (
        f"Ошибка при получении данных заказа: {f_response.status_code}"
    )
    assert f_response.status_code == 200, (
        f"Ожидался статус 200 при получении заказа, "
        f"получен {f_response.status_code}"
    )

    order_details = f_response.json()
    print("Информация о заказе:")
    print(order_details)
