

class Schedule:  # Definiuje klasę Schedule do obsługi harmonogramowania zadań
    def __init__(self):  # Konstruktor klasy Schedule
        self.schedule = []  # Inicjalizuje pustą listę zadań w harmonogramie
        self.schedule_type = ""  # Inicjalizuje typ harmonogramu jako pusty ciąg znaków
        self.average_waiting_times = []  # Inicjalizuje pustą listę średnich czasów oczekiwania
        self.average_turnaround_times = []  # Inicjalizuje pustą listę średnich czasów cyklu przetwarzania

    def fcfs(self, tasks_list):  # Definiuje metodę do implementacji algorytmu FCFS
        self.schedule = []  # Czyszczenie listy harmonogramu
        time = 0  # Inicjalizuje zmienną "time" jako 0
        for task in sorted(tasks_list, key=lambda x: x.arrival_time):  # Sortuje zadania po czasie przybycia
            if time < task.arrival_time:  # Jeśli obecny czas jest mniejszy niż czas przybycia zadania
                time = task.arrival_time  # Ustawia czas na czas przybycia zadania
            task.start_time = time  # Ustawia czas rozpoczęcia zadania
            time += task.burst_time  # Dodaje czas wykonania zadania do obecnego czasu
            task.finish_time = time  # Ustawia czas zakończenia zadania
            self.schedule.append(task)  # Dodaje zadanie do harmonogramu
        self.schedule_type = "FCFS Schedule"  # Ustawia typ harmonogramu na "FCFS Schedule"

    def sjf(self, tasks_list):  # Definiuje metodę do implementacji algorytmu SJF
        self.schedule = []  # Czyszczenie listy harmonogramu
        time = 0  # Inicjalizuje zmienną time jako 0
        tasks_list = sorted(tasks_list, key=lambda x: (x.arrival_time, x.burst_time))  # Sortuje zadania po czasie przybycia i czasie wykonania
        while tasks_list:  # Dopóki lista zadań nie jest pusta
            available_tasks = [task for task in tasks_list if task.arrival_time <= time]  # Filtruje dostępne zadania
            if available_tasks:  # Jeśli są dostępne zadania
                next_task = min(available_tasks, key=lambda x: x.burst_time)  # Wybiera zadanie o najkrótszym czasie wykonania
                tasks_list.remove(next_task)  # Usuwa wybrane zadanie z listy zadań
            else:  # Jeśli nie ma dostępnych zadań
                next_task = tasks_list.pop(0)  # Pobiera pierwsze zadanie z listy
                time = next_task.arrival_time  # Ustawia czas na czas przybycia zadania
            next_task.start_time = time  # Ustawia czas rozpoczęcia zadania
            time += next_task.burst_time  # Dodaje czas wykonania zadania do obecnego czasu
            next_task.finish_time = time  # Ustawia czas zakończenia zadania
            self.schedule.append(next_task)  # Dodaje zadanie do harmonogramu
        self.schedule_type = "SJF Schedule"  # Ustawia typ harmonogramu na "SJF Schedule"

    def get_average_waiting_and_turnaround_times(self):  # Definiuje metodę do obliczania średnich czasów oczekiwania i cyklu przetwarzania
        total_waiting_time = sum(task.start_time - task.arrival_time for task in self.schedule)  # Oblicza łączny czas oczekiwania
        total_turnaround_time = sum(task.finish_time - task.arrival_time for task in self.schedule)  # Oblicza łączny czas cyklu przetwarzania
        average_waiting_time = total_waiting_time / len(self.schedule)  # Oblicza średni czas oczekiwania
        average_turnaround_time = total_turnaround_time / len(self.schedule)  # Oblicza średni czas cyklu przetwarzania
        self.average_waiting_times.append(average_waiting_time)  # Dodaje średni czas oczekiwania do listy
        self.average_turnaround_times.append(average_turnaround_time)  # Dodaje średni czas cyklu przetwarzania do listy
        return average_waiting_time, average_turnaround_time  # Zwraca średni czas oczekiwania i średni czas cyklu przetwarzania
