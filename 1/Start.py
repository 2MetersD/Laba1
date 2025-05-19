import subprocess
import time

# Список сервісів для запуску
services = [
    ("facade_service.py", 8000),
    ("logging_service.py", 8001),
    ("messages_service.py", 8002)
]

processes = []

for service, port in services:
    print(f"Запускаємо {service} на порту {port}...")
    process = subprocess.Popen(["python", service])
    processes.append(process)
    time.sleep(1)  # Невелика пауза для стабільності"python", service])