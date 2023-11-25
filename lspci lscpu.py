import os
import subprocess
import json

# Функция для сбора информации о видеокарте
def gather_gpu_info():
    gpu_info = {}

    # Получение списка видеокарт с помощью lspci
    gpu_list = subprocess.check_output("lspci -vnn | grep -i 'VGA\|3D controller'", shell=True).decode().strip().split('\n')

    gpu_info['gpus'] = []
    for gpu in gpu_list:
        gpu_info['gpus'].append(gpu.strip())

    return gpu_info

# Функция для сбора информации о процессоре
def gather_cpu_info():
    cpu_info = {}

    # Получение информации о процессоре с помощью lscpu
    cpu_output = subprocess.check_output("lscpu", shell=True).decode().strip().split('\n')

    cpu_info['details'] = {}
    for line in cpu_output:
        key, value = line.split(':', 1)
        cpu_info['details'][key.strip()] = value.strip()

    return cpu_info

# Функция для сбора информации о материнской плате
def gather_motherboard_info():
    motherboard_info = {}

    # Получение информации о материнской плате с помощью lspci
    motherboard_output = subprocess.check_output("lspci", shell=True).decode().strip().split('\n')

    motherboard_info['devices'] = []
    for line in motherboard_output:
        if 'Host bridge' in line or 'PCI bridge' in line or 'ISA bridge' in line:
            motherboard_info['devices'].append(line.strip())

    return motherboard_info

# Главная функция
def main():
    gpu_info = gather_gpu_info()
    cpu_info = gather_cpu_info()
    motherboard_info = gather_motherboard_info()

    print("Информация о видеокарте:")
    print(json.dumps(gpu_info, indent=4))
    print("\nИнформация о процессоре:")
    print(json.dumps(cpu_info, indent=4))
    print("\nИнформация о материнской плате:")
    print(json.dumps(motherboard_info, indent=4))

if __name__ == "__main__":
    main()
