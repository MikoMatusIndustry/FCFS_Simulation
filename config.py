

import os  # Importuje moduł os do obsługi operacji systemowych

num_sequences = 100  # Ustawia liczbę sekwencji zadań
tasks_per_sequence = 100  # Ustawia liczbę zadań w każdej sekwencji
test_data_directory = 'test_data'  # Ustawia nazwę katalogu do przechowywania danych testowych

# Upewnia się, że katalog istnieje, w razie potrzeby tworzy go
os.makedirs(test_data_directory, exist_ok=True)
