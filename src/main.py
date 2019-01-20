from training import *
from Network import *


print("1 - Wytrenowanie nowej sieci i zapis do pliku.")
print("2 - Wczytanie sieci z pliku i przetestowanie jej gotowym zbiorem win.")
print("3 - Wczytanie sieci z pliku i sprawdzenie jakości podanego wina.")

inp = input("Wprowadź liczbę:")
user_input = int(inp)

if user_input < 1 and user_input >3 :
    print("Błędna liczba")
elif user_input == 1:
    print("Wybrano opcję 1.")
    file_name = input("Proszę wprowadzić nazwę pliku wyjściowego: ")
    netw = train_network()
    save_network_to_file(netw,file_name)

elif user_input == 2:
    print("Wybrano opcję 2.")
    file_name = input("Proszę wprowadzić nazwę pliku: ")
    netw = load_network_from_file(file_name)
    test_network_automatically(netw)

elif user_input == 3:
    print("Wybrano opcję 3.")
    file_name = input("Proszę wprowadzić nazwę pliku: ")
    netw = load_network_from_file(file_name)
    test_network_manually(netw)
