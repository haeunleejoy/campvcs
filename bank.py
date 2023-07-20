greeting = input("Greeting: ")

def bank(string):
   if greeting == "hello":
      print("$0")
   elif greeting == "h":
      print("$20")
   else:
      print("$100")

bank(greeting)