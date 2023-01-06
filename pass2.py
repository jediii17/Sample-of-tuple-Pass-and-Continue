# Create an array of names
names = ["Alice", "Bob", "Charlie", "Dave"]
print("Names:\n", names)
# Ask the user which name they want to delete
name_to_delete = input("\nEnter the name you want to delete: ")

print("\nUpdated list of Names:")
for i in range(len(names)):
    # Check if the current name is the one we want to delete
    if names[i] == name_to_delete:
        # Delete the name using the pass statement (do nothing)
        pass
    else:
        # If the name is not the one we want to delete, keep it
        print(names[i])
