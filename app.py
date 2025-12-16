def greet(name):
    """Returns a greeting for the given name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # The name we want to greet
    user_name = "World"
    
    # Print the greeting
    print(greet(user_name))