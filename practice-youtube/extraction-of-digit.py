# Counting the number of digits in a given number
n=int(input("Enter a number: "))
num=n
count=0
while num!=0:
    num=num//10
    count+=1

print("Number of digits:",count)

num=n
reverse=0
for i in range(count-1,-1,-1):
    reverse+= (num%10)*(10**i)
    num=num//10

print("Reversed number:",reverse)

if n==reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

num=n 
armstrong=0
for i in range(count-1,-1,-1):
    armstrong+= (num%10)**(count)
    num=num//10

if n==armstrong:
    print ("Armstrong number")
else:
    print("Not an Armstrong Number")