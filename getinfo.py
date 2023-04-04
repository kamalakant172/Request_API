import platform
import psutil
import socket
import os
import requests


def bytes_to_MB(bytes):
    mb = bytes/(1024*1024)
    mb = round(mb, 2)
    return mb

def get_url():

    physical_memory = psutil.virtual_memory()
    disk_partitions1 = psutil.disk_partitions()
    load1, load5, load30 = os.getloadavg()
    load_1= round(load1, 2)
    load_5= round(load5, 2)
    load_30= round(load30, 2)

    for partition in disk_partitions1:
        disk_info1 = psutil.disk_usage(partition.mountpoint)
        bytes_to_MB(disk_info1.total)
        bytes_to_MB(disk_info1.used) 

    url_enpoint="http://stage.linqer.in/"
    mydict = {
        'technology': 'python2', 'technology_version': platform.python_version(), 'da_version': 0.1,'da_app_name': 'python_app',
        'os_name': platform.system(), 'os_version': platform.version(), 'os_arch': platform.architecture(),
        'avg_load_1_min': load_1, 'avg_load_5_min': load_5, 'avg_load_30_min': load_30, 'client_ip': socket.gethostbyname(socket.gethostname()),
        'total_memory_mb': bytes_to_MB(physical_memory.total), 'used_memory_mb': bytes_to_MB(physical_memory.used),
        'user_name': (os.environ.get('USERNAME')), "request_method": "GET", "request_encoding": "gzip, deflate", 'request_content_type': 'text/html', 'meta': '%7B%7D', 'response_headers': '%7B%7D', 'response_code': 23, 'response_length_byte': 45, 'user_email': 'a@gmail.com', 'user_phone': +91-1234567890, 'user_country': 'India', 'user_city': 'Delhi', 'user_state': 'Delhi', 'user_zipcode': 201301, 'user_address_1': 'delhi', 'user_address_2': 'delhi', 'user_image': 'image', 'response_time': 0.1, 'request_cookies': 'cookies', 'request_content_params': 'params', 'request_body': 'body', 'request_path': 'path', 'request_path_info': 'pathinfo', 'url_scheme': 'url', 'request_date': 'date', 'query_string': 'string', 'server_timezone': 'server', 'tracking_id': 'track', 'created_at': 'date', 'geo_country': 'India', 'geo_city': 'Delhi', 'total_disk_mb': bytes_to_MB(disk_info1.total), 'used_disk_mb': bytes_to_MB(disk_info1.used), 'os_agent': 'ubuntu'
    }
    url_resp= requests.get(url_enpoint, params=mydict)
    # print(url_resp.url)
    return url_resp.url

get_url()