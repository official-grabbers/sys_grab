import platform
import psutil
import socket
import datetime
import subprocess


class SystemConfig:
    @staticmethod
    def get_size(bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    @classmethod
    def get_system_info(cls):
        uname = platform.uname()
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.datetime.fromtimestamp(boot_time_timestamp)

        # CPU info
        cpufreq = psutil.cpu_freq()
        cpu_info = {
            "Physical Cores": psutil.cpu_count(logical=False),
            "Total Cores": psutil.cpu_count(logical=True),
            "Max Frequency": f"{cpufreq.max:.2f}Mhz",
            "Min Frequency": f"{cpufreq.min:.2f}Mhz",
            "Current Frequency": f"{cpufreq.current:.2f}Mhz",
            "CPU Usage Per Core": {f"Core {i}": f"{percentage}%" for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1))},
            "Total CPU Usage": f"{psutil.cpu_percent()}%"
        }

        # Memory info
        svmem = psutil.virtual_memory()
        memory_info = {
            "Total Memory": cls.get_size(svmem.total),
            "Available Memory": cls.get_size(svmem.available),
            "Used Memory": cls.get_size(svmem.used),
            "Memory Percentage": f"{svmem.percent}%"
        }

        # Disk info
        disk_partitions = psutil.disk_partitions()
        disk_info = {}
        for partition in disk_partitions:
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            disk_info[partition.device] = {
                "Total Size": cls.get_size(partition_usage.total),
                "Used": cls.get_size(partition_usage.used),
                "Free": cls.get_size(partition_usage.free),
                "Percentage": f"{partition_usage.percent}%"
            }

        # Network info
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        # Get list of open ports
        open_ports = []
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == psutil.CONN_ESTABLISHED:
                open_ports.append(conn.laddr.port)


        network_info = {
            "Hostname": hostname,
            "IP Address": ip_address,
            "Network Interfaces": {interface_name: {str(address.family): {"IP Address": address.address, "Netmask": address.netmask, "Broadcast IP": address.broadcast}} for interface_name, interface_addresses in psutil.net_if_addrs().items() for address in interface_addresses}
        }
        network_info["Open Ports"] = open_ports

        # Run df -h command and capture output
        try:
            df_output = subprocess.run(["df", "-h"], capture_output=True, text=True, check=True).stdout
        except subprocess.CalledProcessError:
            df_output = "Unable to retrieve df -h output."

        return {
            "System Information": {
                "System": uname.system,
                "Node Name": uname.node,
                "Release": uname.release,
                "Version": uname.version,
                "Machine": uname.machine,
                "Processor": uname.processor,
                "Boot Time": f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"
            },
            "CPU Information": cpu_info,
            "Memory Information": memory_info,
            "Disk Information": disk_info,
            "Network Information": network_info,
            "df -h Output": df_output
        }