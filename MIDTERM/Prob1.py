def is_palindrome(n):
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]

def process_file(filename):
    """Read numbers from a file, compute their sum, and check if it's a palindrome."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        for index, line in enumerate(lines, start=1):
            try:
                numbers = [int(num.strip()) for num in line.split(',') if num.strip()]
                total = sum(numbers)
                result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
                print(f"Line {index}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
            except ValueError:
                print(f"Error: Invalid data on line {index}. Skipping...")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")


file_path = r"MIDTERM/numbers.txt"
process_file(file_path)
