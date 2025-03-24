

import random  # Importuje moduł random do generowania losowych wartości
from task import Task  # Importuje klasę Task z modułu task.py

def generate_task_sequence(num_tasks):  # Definiuje funkcję do generowania sekwencji zadań
    return [Task(f"T{i+1}", random.randint(0, 99), random.randint(1, 20)) for i in range(num_tasks)]  # Tworzy listę zadań o losowych czasach przybycia i czasach wykonania

def write_task_sequence_to_file(tasks, file_path):  # Definiuje funkcję do zapisywania sekwencji zadań do pliku
    with open(file_path, 'w') as file:  # Otwiera plik do zapisu
        for task in tasks:  # Iteruje przez listę zadań
            file.write(f"{task.name} {task.arrival_time} {task.burst_time}\n")  # Zapisuje szczegóły zadania do pliku

def read_tasks_from_file(file_path):  # Definiuje funkcję do wczytywania zadań z pliku
    tasks = []  # Inicjalizuje pustą listę zadań
    with open(file_path, 'r') as file:  # Otwiera plik do odczytu
        for line in file:  # Iteruje przez linie w pliku
            name, arrival_time, burst_time = line.split()  # Rozdziela linię na nazwę, czas przybycia i czas wykonania
            tasks.append(Task(name, int(arrival_time), int(burst_time)))  # Dodaje zadanie do listy zadań
    return tasks  # Zwraca listę zadań
