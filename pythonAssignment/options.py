def main():
    choice = True
    while choice:
        print("Menu: ")
        print("1) Add")
        print("2) View")
        print("3) Delete")
        print("4) Quit")
        option = input("Choose an option.")
            
        if option =='1':
            print("You selected Add.")
        elif option == '2':
            print("You selected View.")
        elif option == '3':
            print("You selected Delete")
        elif option == '4':
            print("You selected Quit")
            choice = False
        else:
            print("Invalid choice. Please choose again.")
        print() 
if __name__ == "__main__":
    main()
