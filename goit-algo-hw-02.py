from queue import Queue


# Створити чергу заявок
queue = Queue()

def generate_request():
    user_input = input("Введіть Ваш запит")
    queue.put(user_input)
  

def process_request():
        if not queue.empty():
              request = queue.get()
              print("Оброблено заявку:", request)
        else:
            print("Черга порожня")     

while True:
    # Виклик функції для створення нової заявки
    generate_request()
    # Виклик функції для обробки заявок
    process_request()

    # Перевірка, чи користувач бажає вийти з програми
    user_input = input("Бажаєте вийти з програми? (Так/Ні): ")
    if user_input.lower() == "так":
        print("Дякуємо за використання програми!")
        break