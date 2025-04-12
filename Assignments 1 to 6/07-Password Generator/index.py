import random
import string

try:
    import pyperclip
    clipboard_enabled = True
except ImportError:
    clipboard_enabled = False

def generate_password(length=12):
    if length < 6:
        print("⚠️ Password length should be at least 6 for better security.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Pro Password Generator 🔐")
    print("------------------------------------------")

    try:
        length = int(input("Enter desired password length (minimum 6): "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return

    password = generate_password(length)

    if password:
        print(f"\n✅ Your secure password is: {password}")
        if clipboard_enabled:
            pyperclip.copy(password)
            print("📋 Password copied to clipboard!")
        else:
            print("📋 Install `pyperclip` to enable clipboard support (optional).")

if __name__ == "__main__":
    main()
