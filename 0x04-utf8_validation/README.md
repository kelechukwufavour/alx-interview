0x04. UTF-8 Validation
### UTF-8 Validation

This project, "0x04. UTF-8 Validation," requires you to utilize your knowledge of bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding. Here are the key concepts and resources that will aid you in completing this project:

#### Concepts Needed:
1. **Bitwise Operations in Python**:
   - Understanding how to manipulate bits in Python using operations like AND (&), OR (|), XOR (^), NOT (~), shifts (<<, >>).
   - Familiarity with Python Bitwise Operators.

2. **UTF-8 Encoding Scheme**:
   - Understanding the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
   - Recognizing the patterns that signify a valid UTF-8 encoded character.
   - Resources: 
     - [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
     - [Characters, Symbols, and the Unicode Miracle](http://www.joelonsoftware.com/articles/Unicode.html)
     - [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](http://www.joelonsoftware.com/articles/Unicode.html)

3. **Data Representation**:
   - Knowledge of representing and working with data at the byte level.
   - Understanding how to handle the least significant bits (LSB) of integers to simulate byte data.

4. **List Manipulation in Python**:
   - Iterating through lists, accessing list elements, and understanding list comprehensions.
   - Familiarity with Python Lists.

5. **Boolean Logic**:
   - Applying logical operations to make decisions within the program.

By studying these concepts and utilizing the provided resources, you will be prepared to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

#### Additional Resource:
- [Mock Technical Interview](link_to_mock_interview)

### Requirements
#### General
- **Allowed editors**: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

### Tasks
#### 0. UTF-8 Validation
**mandatory**

Write a method that determines if a given data set represents a valid UTF-8 encoding.
- **Prototype**: `def validUTF8(data)`
- **Return**: True if data is a valid UTF-8 encoding, else return False
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.