import schedule
import time
from datetime import datetime

def print_current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Current time: {current_time}")

# Настроим вывод времени каждую минуту
schedule.every(1).minute.do(print_current_time)

# Запускаем цикл для выполнения задачи
while True:
    schedule.run_pending()
    time.sleep(1)
