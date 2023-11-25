import os
import subprocess
import json

# Функция для сбора информации о дисках
def gather_disk_info():
    disk_info = {}

    # Получение списка дисков с их разделами
    disks = subprocess.check_output("lsblk -io KNAME,TYPE,FSTYPE,SIZE,MOUNTPOINT -J --bytes", shell=True).decode()
    disks = json.loads(disks)['blockdevices']

    disk_list = []
    system_disk = ""
    total_size = 0

    for disk in disks:
        if disk['type'] == 'disk':
            disk_name = disk['kname']
            disk_size_bytes = int(disk['size'])
            disk_size_gb = round(disk_size_bytes / (1024 ** 3), 2)
            mount_point = disk.get('mountpoint', '')

            disk_info = {
                'name': disk_name,
                'size_gb': disk_size_gb,
                'mount_point': mount_point
            }

            if disk_name.startswith('nvme') or disk_name.startswith('sda'):
                system_disk = disk_name

            disk_list.append(disk_info)
            total_size += disk_size_gb

    disk_info['disks'] = disk_list
    disk_info['system_disk'] = system_disk
    disk_info['total_size_gb'] = total_size

    return disk_info

# Главная функция
def main():
    disk_info = gather_disk_info()

    print("Информация о дисках:")
    print(json.dumps(disk_info, indent=4))

if __name__ == "__main__":
    main()
