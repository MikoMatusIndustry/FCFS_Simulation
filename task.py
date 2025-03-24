
class Task:  # Definiuje klasę Task reprezentującą zadanie
    def __init__(self, name, arrival_time, burst_time):  # Konstruktor klasy Task, przyjmujący nazwę zadania, czas przybycia i czas wykonania
        self.name = name  # Inicjalizuje nazwę zadania
        self.arrival_time = arrival_time  # Inicjalizuje czas przybycia zadania
        self.burst_time = burst_time  # Inicjalizuje czas wykonania zadania
        self.start_time = None
        self.finish_time = None
