def shutdown_check():
    user_input = input("Do you want to shut down the system? (yes/no): ").strip().lower()
    
    if user_input == "yes":
        print("Shutting down.")
    else:
        print("Sorry, Shutdown Aborted.")


shutdown_check()
