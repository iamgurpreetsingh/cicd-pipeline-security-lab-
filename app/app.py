import os

def handler():
    secret = os.getenv("SECRET_KEY", "not_set")
    print("App running")
    print("Secret:", secret)

if __name__ == "__main__":
    handler()
