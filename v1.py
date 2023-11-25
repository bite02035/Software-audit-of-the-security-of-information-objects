import os
import platform
import subprocess
import sys
import json
from datetime import datetime


# Функция для сбора информации об ОС
def get_os_info():
    os_info = {}
    os_info['name'] = platform.system()
    os_info['version'] = platform.release()
    return os_info


# Функция для сбора информации об аппаратуре
def get_hardware_info():
    hardware_info = {}
    # напишите код для сбора информации об аппаратуре
    return hardware_info


# Функция для сбора информации о программном обеспечении
def get_software_info():
    software_info = {}
    # напишите код для сбора информации о программном обеспечении
    return software_info


# Функция для сохранения отчета в файл
def save_report(report):
    filename = f'report_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.json'
    with open(filename, 'w') as file:
        json.dump(report, file, indent=4)


# Функция для экспорта отчета в форматы .html, .pdf, .doc, .xml
def export_report(report):
    # напишите код для экспорта отчета в различные форматы
    pass


# Функция для запуска инвентаризации на каждой АРМ
def run_local_inventory():
    os_info = get_os_info()
    hardware_info = get_hardware_info()
    software_info = get_software_info()

    report = {}
    report['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report['os_info'] = os_info
    report['hardware_info'] = hardware_info
    report['software_info'] = software_info

    save_report(report)
    export_report(report)


# Функция для запуска сетевой инвентаризации
def run_network_inventory():
    # напишите код для запуска сетевой инвентаризации
    pass


# Главная функция
def main():
    if platform.system() != 'Linux':
        print("Программа поддерживает только Linux.")
        sys.exit()

    print("1 - локальная инвентаризация")
    print("2 - сетевая инвентаризация")
    choice = input("Выберите вариант (1/2): ")

    if choice == '1':
        run_local_inventory()
    elif choice == '2':
        run_network_inventory()
    else:
        print("Неверный выбор.")


if __name__ == "main":
    main()