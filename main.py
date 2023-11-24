from selenium_login import login
from utils import get_accounts, delete_account, update_proxy_ip
from logger import logger
from config import mobile_proxy, mobile_proxy_update_ip_url


delimiter = ':'


def main():
    input_file = 'accounts.txt'
    accounts = get_accounts(filename=input_file)
    for account in accounts:
        logger.info(f'New account: {account}')
        account_split = account.split(delimiter, maxsplit=4)
        if len(account_split) == 5:
            username, password, mail, mail_pass, proxy = account_split
        else:
            username, password, mail, mail_pass = account_split
            proxy = None
        if proxy is None:
            proxy = mobile_proxy
            if mobile_proxy_update_ip_url:
                update_proxy_ip(mobile_proxy_update_ip_url)
        try:
            token = login(password, proxy, username, mail, mail_pass)
        except:
            logger.error('Login error:', exc_info=True)
            with open('failed_accounts.txt', 'a') as file:
                file.write(account+'\n')
            delete_account(filename=input_file)
            continue
        logger.info('Login successful')
        delete_account(filename=input_file)
        with open('ready_accounts.txt', 'a') as file:
            file.write(delimiter.join([account, token]) + '\n')


if __name__ == '__main__':
    main()
