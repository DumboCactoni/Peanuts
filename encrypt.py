import sys, base64

sys.stdin = open("main.in")
a = sys.stdin.read().strip().split('\n')

def encrypt(text, key):
    xored = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
    return base64.urlsafe_b64encode(xored.encode('utf-8', 'surrogatepass')).decode()

def decrypt(token, key):
    xored = base64.urlsafe_b64decode(token.encode()).decode('utf-8', 'surrogatepass')
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(xored))

a[0] = a[0].split()
if a[0][0] == "encrypt":
    for i in a[1:]:
        print(encrypt(i, a[0][1]))
else:
    for i in a[1:]:
        print(decrypt(i, a[0][1]))
    