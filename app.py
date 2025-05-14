from auth import register, login
import requests

def get_crypto_price(symbol="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    res = requests.get(url).json()
    return res.get(symbol, {}).get("usd", "Not found")

def main():
    print("Welcome to Crypto Tracker!")
    choice = input("Login or Register? (l/r): ").lower()
    username = input("Username: ")
    password = input("Password: ")

    if choice == 'r':
        success, msg = register(username, password)
        print(msg)
        if not success:
            return

    if not login(username, password):
        print("Login failed.")
        return

    print(f"\nHello, {username}! Current BTC price: ${get_crypto_price('bitcoin')}")
    # Bisa dikembangkan untuk menyimpan portofolio nanti

if __name__ == "__main__":
    main()
