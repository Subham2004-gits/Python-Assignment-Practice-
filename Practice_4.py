
with open(r'C:\Users\subha\OneDrive\Desktop\AIML\Python Practice and APIs\AIML.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)
f.close()


with open(r'C:\Users\subha\OneDrive\Desktop\AIML\Python Practice and APIs\AIML.txt', 'w', encoding='utf-8') as f:
    f.write("Hello Subham!\nThis is a Python file write example.\nWelcome to AIML practice session.")

print("✅ File written successfully!")

with open(r'C:\Users\subha\OneDrive\Desktop\AIML\Python Practice and APIs\AIML.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print("\n📘 File Content:\n")
    print(text)

