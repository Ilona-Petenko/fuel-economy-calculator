print("Привіт! Я допоможу розрахувати вартість поїздки. Для цього мені потрібно знати деякі дані.")

global fuelСonsumption90
global fuelСonsumption110
global tripDistance
global tripTime
global fluelPrice

try:
    fuelСonsumption90 = 0.01 * float(input("Який розхід палива у твого автомобіля при швидкості 90 км/год (л/км * 100): "))
    fuelСonsumption110 = 0.01 * float(input("Який розхід палива у твого автомобіля при швидкості 110 км/год (л/км * 100): "))
    tripDistance = float(input("Яка відстань твоєї поїздки (км): "))
    tripTime = float(input("За скільки часу проїхав цю відстань(год): "))
    fluelPrice = float(input("Вартісь палива: "))
except:
    print("Пишіть, будь ласка, число")
    exit()


averageSpeed = tripDistance / tripTime

fuelConsumption = fuelСonsumption90 + ((averageSpeed - 90) / 20 * (fuelСonsumption110 - fuelСonsumption90))

overallFuelConsumption = fuelConsumption * tripDistance

tripPrice = round(overallFuelConsumption * fluelPrice, 2)

print("Загальна вартість твоєї поїздки становить: " + str(tripPrice))

if averageSpeed <= 90:
    print("Молодець! Твоя витрата палива оптимальна!")
else:
    tripPrice90 = round(fuelСonsumption90 * tripDistance * fluelPrice, 2)

    print("Ви могли б зекономити " + str(tripPrice - tripPrice90) + ", якщо б їхали зі швидкістю 90 км/год.")