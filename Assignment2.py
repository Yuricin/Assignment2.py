def main():
    num=int(input("Enter an integer:"))
    print(odd_even(num),"\n\n")
    
def main2():
    print(sum())

def odd_even(num):
    if num%2==0:
        return f"The {num} is an even number"
    else:
         return f"The {num} is an odd number"
         
def sum():
         i=0
         sum=0
         while i<=50:
             sum+=i
         return sum
             
if  __name__== "__ main__":
    main()  
    main2()