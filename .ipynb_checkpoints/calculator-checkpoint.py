import operations
import scientific

def display():
    choice=int(input("1.Add two numbers\n2.Subtract two numbers\n3. Multiplication of two numbers\n\n4. Log of a number\n"))
    return choice

def operate(choice):
    if choice==1:
        number_1=input("\nEnter first number")
        number_2=input("\nEnter second number\n")
        result = 'Sum of '+number_1+' and '+number_2+' is :'+str(operations.add(int(float(number_1)),int(float(number_2))))
    elif choice==2:
        number_1=input("\nEnter first number")
        number_2=input("\nEnter second number\n")
        result = 'Difference of '+number_1+' and '+number_2+' is :'+str(operations.subtract(int(float(number_1)),int(float(number_2))))   
    elif choice==3:
        number_1=input("\nEnter first number")
        number_2=input("\nEnter second number\n")
        result = 'Difference of '+number_1+' and '+number_2+' is :'+str(operations.multiply(int(float(number_1)),int(float(number_2))))   
    else:
        number_1=input("\nEnter the number")
#         number_2=input("\nEnter second number\n")
        result = 'Log of '+number_1+' is :'+str(scientific.log(int(float(number_1))))
    
    return result
        
if __name__=="__main__":
    print('Enter your choice\n')
    choice=display()
    result=operate(choice)
    print('\n',result)