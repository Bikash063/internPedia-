import string

def count_words(text):
    # Remove punctuation and convert text to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Count the number of words
    word_count = len(words)
    
    return word_count

def process_text_input():
    while True:
        print("\nEnter '1' to input text manually, '2' to input from a file, or 'q' to quit.")
        choice = input("Your choice: ").strip()

        if choice == '1':
            text = input("Enter your text: ")
            if not text.strip():
                print("Empty input! Please enter some text.")
            else:
                word_count = count_words(text)
                print(f"The number of words in the input text: {word_count}")
        
        elif choice == '2':
            file_path = input("Enter the file path: ").strip()
            try:
                with open(file_path, 'r') as file:
                    text = file.read()
                    if not text.strip():
                        print("The file is empty. Please provide a file with some text.")
                    else:
                        word_count = count_words(text)
                        print(f"The number of words in the file: {word_count}")
            except FileNotFoundError:
                print("File not found! Please check the file path and try again.")
            except Exception as e:
                print(f"An error occurred while reading the file: {e}")
        
        elif choice == 'q':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter '1', '2', or 'q'.")

if __name__ == "__main__":
    print("Welcome to the Word Counter Program!")
    process_text_input()
