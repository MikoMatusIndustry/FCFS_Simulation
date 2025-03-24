import os  # Importuje moduł os - umożliwia operacje na systemie operacyjnym.
import subprocess  # Importuje moduł subprocess - umożliwia wywoływanie poleceń systemowych.
import csv  # Importuje moduł csv - umożliwia manipulację plikami CSV.
from schedule import Schedule  # Importuje klasy Schedule z modułu schedule.
from utils import generate_task_sequence, write_task_sequence_to_file, read_tasks_from_file  # Importuje funkcje z modułu utils.
from config import num_sequences, tasks_per_sequence, test_data_directory  # Importuje zmienne konfiguracyjne z modułu config.


schedule = Schedule()  # Utworzy instancje klasy Schedule.

fcfs_avg_waiting_times = []  # Inicjalizzuje pustą listę dla średnich czasów oczekiwania w FCFS.
fcfs_avg_turnaround_times = []  # Inicjalizuje pustą listę dla średnich czasów cyklu przetwarzania w FCFS.
sjf_avg_waiting_times = []  # Inicjalizuje pustą listę dla średnich czasów oczekiwania w SJF.
sjf_avg_turnaround_times = []  # Inicjalizuje pustą listę dla średnich czasów cyklu przetwarzania w SJF.

# Generowanie i zapisywanie sekwencji zadań
for i in range(num_sequences):  # Pętla iterująca po liczbie sekwencji zadań.
    tasks_example = generate_task_sequence(tasks_per_sequence)  # Generuje sekwencje zadań.
    file_path = os.path.join(test_data_directory, f'test_sequence_{i+1}.txt')  # Tworzeny ścieżki do pliku z sekwencją zadań.
    write_task_sequence_to_file(tasks_example, file_path)  # Zapisuje sekwencje zadań do pliku.

    # Wczytuje zadania z pliku (symulacja użycia w prawdziwym środowisku)
    tasks_from_file = read_tasks_from_file(file_path)  # Wczytuje zadania z pliku tekstowego.

    # Symulacja FCFS
    schedule.fcfs(tasks_from_file)  # Uruchamia algorytm FCFS na wczytanych zadaniach.
    avg_waiting_time, avg_turnaround_time = schedule.get_average_waiting_and_turnaround_times()  # Oblicza średnią czasów dla FCFS.
    fcfs_avg_waiting_times.append(avg_waiting_time)  # Dodaje średni czas oczekiwania do listy.
    fcfs_avg_turnaround_times.append(avg_turnaround_time)  # Dodaje średni czas cyklu przetwarzania do listy.

    # Symulacja SJF
    tasks_from_file = read_tasks_from_file(file_path)  # Ponowie wczytuje zadania, aby zresetować ich stany.
    schedule.sjf(tasks_from_file)  # Uruchamia algorytm SJF na wczytanych zadaniach.
    avg_waiting_time, avg_turnaround_time = schedule.get_average_waiting_and_turnaround_times()  # Oblicza średnie czasy dla SJF.
    sjf_avg_waiting_times.append(avg_waiting_time)  # Dodaje średni czas oczekiwania do listy.
    sjf_avg_turnaround_times.append(avg_turnaround_time)  # Dodaje średni czas cyklu przetwarzania do listy.

# Obliczanie średnich czasów dla obu algorytmów
fcfs_avg_waiting_time_overall = sum(fcfs_avg_waiting_times) / num_sequences  # Oblicza średni czas oczekiwania ogólnego dla FCFS.
fcfs_avg_turnaround_time_overall = sum(fcfs_avg_turnaround_times) / num_sequences  # Oblicza średni czas cyklu przetwarzania ogólnego dla FCFS.
sjf_avg_waiting_time_overall = sum(sjf_avg_waiting_times) / num_sequences  # Oblicza średni czas oczekiwania ogólnego dla SJF.
sjf_avg_turnaround_time_overall = sum(sjf_avg_turnaround_times) / num_sequences  # Oblicza średni czas cyklu przetwarzania ogólnego dla SJF.

# Zapisywanie wyników do pliku CSV
results_file_path = os.path.join(os.getcwd(), 'wyniki_eksperymentow.csv')  # Ścieżka do pliku wynikowego CSV.
with open(results_file_path, 'w', newline='') as csvfile:  # Otwiera plik CSV do zapisu.
    writer = csv.writer(csvfile, delimiter=';')  # Inicjalizuje obiekt writer do zapisu CSV.
    writer.writerow(["Seq", "FCFS Waiting Time", "SJF Waiting Time", "FCFS Turnaround Time", "SJF Turnaround Time"])  # Nagłówki kolumn w pliku CSV.
    for i in range(num_sequences):  # Pętla iteruje po liczbie sekwencji zadań.
        writer.writerow([f"Seq{i+1}", fcfs_avg_waiting_times[i], sjf_avg_waiting_times[i], fcfs_avg_turnaround_times[i], sjf_avg_turnaround_times[i]])  # Zapisanie wyników dla każdej sekwencji.

    writer.writerow([])  # Pusta linia w pliku CSV.
    writer.writerow(["Overall Averages"])  # Nagłówek dla średnich czasów ogólnych.
    writer.writerow(["FCFS Average Waiting Time", fcfs_avg_waiting_time_overall])  # Zapisanie średniego czasu oczekiwania ogólnego dla FCFS.
    writer.writerow(["FCFS Average Turnaround Time", fcfs_avg_turnaround_time_overall])  # Zapisanie średniego czasu cyklu przetwarzania ogólnego dla FCFS.
    writer.writerow(["SJF Average Waiting Time", sjf_avg_waiting_time_overall])  # Zapisanie średniego czasu oczekiwania ogólnego dla SJF.
    writer.writerow(["SJF Average Turnaround Time", sjf_avg_turnaround_time_overall])  # Zapisanie średniego czasu cyklu przetwarzania ogólnego dla SJF.

# Otwieranie pliku wynikowego
directory = os.getcwd()  # Pobiera aktualny katalog roboczy.
print(directory)  # Wyświetla ścieżkę do katalogu roboczego.
subprocess.Popen(['explorer', results_file_path])  # Otwiera eksploratora plików z wynikami.
subprocess.Popen(f'explorer "{directory}\\test_data"')  # Otwiera eksploratora plików z katalogiem test_data.

# Czeka na naciśnięcie klawisza Q do zakończenia programu
print("Naciśnij klawisz Q, aby zamknąć program.")  # Wyświetla komunikat.

while True:  # Pętla nieskończona.
    key_press = input().upper()  # Oczekuje na wciśnięcie klawisza i konwersja na małe litery.
    if key_press == 'Q':  # Sprawdza czy wciśnięto klawisz Q.
        try:
            os.system(f'TASKKILL /F /IM excel.exe')  # Zakończenie procesu Excela.
        except Exception as e:
            print(f'Wystąpił błąd podczas zamykania pliku wynikowego: {e}')  # Obsługa błędu.
        break  # Zakończenie pętli while.
