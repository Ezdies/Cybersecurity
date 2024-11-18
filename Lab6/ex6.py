# import requests
# data = {"username" : "kali", "password" : "toor"}
# session = requests.session()

# session.get("http://127.0.0.1:1105")

# cookies = requests.utils.dict_from_cookiejar(session.cookies)
# print(cookies)

#dokończyć, żeby oprócz cookiesów kolejne requesty dołączały też login i hasło

import requests

# Etap 1: Logowanie do serwera
login_url = "http://127.0.0.1:1105/"
login_data = {"username": "kali", "password": "toor"}
session = requests.Session()
login_response = session.post(login_url, data=login_data)

if login_response.status_code == 200:
    print("Login successful")
    print("Cookies:", session.cookies.get_dict())
else:
    print("Login failed:", login_response.status_code, login_response.text)
    exit()

# Etap 2: Pobranie zawartości strony dashboard
dashboard_url = "http://127.0.0.1:1105/dashboard.php"
dashboard_response = session.get(dashboard_url)

print("Dashboard response:")
print(dashboard_response.text)

# Etap 3: Wylogowanie
logout_url = "http://127.0.0.1:1105/logout.php"
logout_response = session.get(logout_url)

if logout_response.status_code == 200:
    print("Logout successful")
else:
    print("Logout failed:", logout_response.status_code)
