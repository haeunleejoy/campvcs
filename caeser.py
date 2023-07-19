# print(ord('y'))
# print(chr(121))

key = int(input("key: "))
plaintext = input("plaintext: ")

  # change I to the number format : ord
    # add the key
    # convert back to a character : chr
for i in plaintext:
    print(chr(ord(i)+key),end = " ")
for i in plaintext: 
    print(chr((ord(1)+key) % 26) + 65)

  