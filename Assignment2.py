def main():
    num=int(input("Enter an integer:"))
    print(odd_even(num),"\n\n")
    print(sum())
    
def odd_even(num):
    if num%2==0:
        return f"The number {num} is an even number"
    else:
         return f"The number {num} is an odd number"
         
def sum():
         i=0
         sum=0
         for i in range(0,51):
             sum+=i
         return f"The sum of numbers from 1 to 50 is {sum}"
             
main()  
