# ini buat fungsi dari (+ , - , * , / ) 
def add (x,  y):
   return  x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    return x / y

print ('selamat datang di kalkulator mini ') #starter thingy 
print ('pilih operasi')
print("1.+")
print("2.-")
print("3.X")
print("4./")


# while function 
while True:
    # Take input from the user
    choice = input("Masukan pilihan (1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'): #buat detect choice mana yang dipilih 
        num1 = float(input("Masukan angka pertama: "))
        num2 = float(input("Masukan angka kedua : "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")


         
            # notes for cycom members
            # silahkan copas 
