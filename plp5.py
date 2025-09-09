with open("data.txt", "r") as file:
    data= file.read();
    print(data)

filename =str(input("name the file you want to open.NB: include the file extension \t"));
data1= input('Please enter data into your file you have recently opened \t');

try:
    #filename =str(input("name the file you want to open.NB: include the file extension\t"));

    with open(filename,'r+') as file1:
        #data1= input('Please enter data into your file you have recently opened')
        file1.write(data1);
except FileNotFoundError:
    print('Oooops, seems we need to change our programmer!!! 😂');


print('Hello World');