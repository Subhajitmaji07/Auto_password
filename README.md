# Password Generator

## Overview

The Password Generator is a simple Python script that generates a random password based on user-defined length and allows the user to save the generated password to a text file along with the associated website name.

## Features

- **Random Password Generation**: Generates a secure password using lowercase letters, uppercase letters, digits, and special symbols.
- **Save Password**: Option to save the generated password to a text file along with the website name.

## Technologies Used

- Python
- Standard Libraries: ```
  random
  ```

  , ```
  string
  ```

## Installation

To run this script locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   
   ```
2. Ensure you have Python installed on your machine. This script is compatible with Python 3.x.
3. Run the script:

   ```
   python password_generator.py
   
   ```

## Usage

1. **Enter Password Length**: When prompted, enter the desired length of the password.
2. **Generated Password**: The script will generate a random password and display it.
3. **Save Password**: You will be prompted to save the password to a file. Enter ```
   y
   ```

    to save or ```
   n
   ```

    to discard.
4. **Website Name**: If you choose to save the password, enter the name of the website associated with the password.
5. **Check Saved Passwords**: The generated password will be saved in a file named ```
   password.txt
   ```

    in the same directory as the script.

## Code Structure

- **Password Generation**: The script uses the ```
  random.sample()
  ```

   function to create a password from a combination of lowercase letters, uppercase letters, digits, and symbols.
- **File Handling**: The script appends the generated password and website name to a text file named ```
  password.txt
  ```

  .

## Example

```
Enter the length of the password: 12
Generated Password: aB3$dEfG!hJk
Save password to file?(y/n): y
Enter the website name: example.com
Password saved to 'password.txt' file
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## Acknowledgments

- Thanks to the Python community for their support and resources.
- Special thanks to the developers of the Python Standard Library for providing useful modules for randomization and string manipulation.
