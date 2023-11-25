import os
import platform
import subprocess
import json

# Функция для сбора информации о системе
def gather_system_info():
    system_info = {}

    # Имя и версия операционной системы
    system_info['os'] = platform.system()
    system_info['os_version'] = platform.release()

    # Имя и версия ядра
    uname = platform.uname()
    system_info['kernel'] = uname[2]
    system_info['kernel_version'] = uname[3]

    # Информация о процессоре
    cpu_info = subprocess.check_output("cat /proc/cpuinfo", shell=True).decode().strip().split('\n')
    cpu_info_dict = {}
    for line in cpu_info:
        if line.strip():
            key, value = line.split(':', 1)
            cpu_info_dict[key.strip()] = value.strip()
    system_info['processor'] = cpu_info_dict

    # Объём оперативной памяти
    memory_info = subprocess.check_output("cat /proc/meminfo", shell=True).decode().strip().split('\n')
    memory_info_dict = {}
    for line in memory_info:
        if line.strip():
            key, value = line.split(':', 1)
            memory_info_dict[key.strip()] = value.strip().split()[0]
    system_info['memory'] = memory_info_dict

    return system_info

# Главная функция
def main():
    system_info = gather_system_info()
    print(json.dumps(system_info, indent=4))

if __name__ == "__main__":
    main()
