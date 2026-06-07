import os

def handler():
    secret = os.getenv("SECRET_KEY", "not_set")
    print("App running")
    print("Secret:", secret)
    
    API_KEY = "sk_live_123456789"

if __name__ == "__main__":
    handler()
