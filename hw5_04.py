def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            if isinstance(e, KeyError):
                return "Enter user name"
            elif isinstance(e, ValueError):
                return "Enter the argument for the command"
            elif isinstance(e, IndexError):
                return "Invalid index"
            
    return wrapper

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contacts(username, new_phone, contacts):
    if username in contacts:
        contacts[username] = new_phone
        return f"Phone number updated successfully for {username}."
    else:
        return f"Error: {username} does not exist in the contacts." 

@input_error
def phone_user(args, contacts):
    name = args[0]
    if name in contacts:
        return f'{name}: {contacts[name]}'
    else:
        return "No user in contacts"
    
@input_error
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts available."
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        return "All contacts displayed."
    
@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:  #1 Завдання
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")  #6 Завдання
        
        elif command == "add":
            print(add_contact(args, contacts))   #2 Завдання
            
        elif command == "change":
            name, new_phone = args
            print(change_contacts(name, new_phone, contacts)) #3 Завдання
         
        elif command == "phone": 
            print(phone_user(args, contacts))   #4
                
        elif command == "all":
            print(show_all_contacts(contacts), "\t")    #5
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()