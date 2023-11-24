import requests
import time


def struct_proxy(proxy):
    return {
        'http': proxy
    }


def get_proxy_server_and_authentication(proxy):
    if '@' in proxy:
        return True, proxy.split('@')[-1]
    return False, proxy.split('//')[-1]


def get_accounts(filename: str):
    with open(filename, 'r') as file:
        accounts = file.readlines()
        accounts = [account.replace('\n', '') for account in accounts]
        return accounts


def delete_account(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        file.writelines(lines[1:])


def update_proxy_ip(update_url: str):
    requests.get(update_url)
    time.sleep(1)
