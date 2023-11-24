# Twitter Token Gatherer
## by @fleecybastard

This projects uses selenium to enter twitter accounts which may require email authentication and collects auth token of 
account. If email authentication is required it uses Imap server to find the code, sent by twitter to a specified email 
address

## Installation guide
1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Install <b>chromedriver.exe</b> <a href="https://chromedriver.chromium.org/downloads">here</a>. Install chromedriver of the same version as your chrome browser. If your version is not specified, try searching <a href="https://googlechromelabs.github.io/chrome-for-testing/">here</a>


## Usage guide
1. Add accounts to <b>accounts.txt</b> using the format specified in the file.
2. If you want to use mobile proxy, enter it into <b>config.py</b> and enter ip update url if necessary.
Only http proxies are supported. Proxy format is **http://login:password@ip_address:port**
3. Run
```bash
python main.py
```
4. Auth tokens will appear in **ready_accounts.txt**. Failed accounts will appear in **failed_accounts.txt**
5. Try running failed accounts multiple times. They might fail due to selenium or connections errors.

## If you have any questions, contact me on telegram <a href="https://t.me/fleecybastard">@fleecybastard</a>
