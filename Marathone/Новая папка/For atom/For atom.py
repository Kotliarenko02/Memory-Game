# def presentaion():
#     print("What is your name?")
#     name = input()
#     print("What is your age?")
#     age = input()
#     print(f"Your name is {name}, your age is{age}")
# presentaion()
path = input ("Print path to the directory:")
ask = input("If you want to create DIR type / if you want to delete DIR type N:")
if ask == "Y":
    os.mkdir(path)
else:
    os.rmdir(path)  
