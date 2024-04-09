0x03-log_parsing
### Log Parsing Project

This project involves writing a script in Python that reads input from stdin line by line and computes metrics based on the input data. By studying various Python concepts and utilizing the provided resources, you'll be equipped to effectively handle data streams, parse log entries, and compute metrics.

#### Concepts Needed:
1. **File I/O in Python**:
   - Understanding how to read from `sys.stdin` line by line.
   - Familiarity with Python Input and Output operations.

2. **Signal Handling in Python**:
   - Handling keyboard interruptions (CTRL + C) using signal handling in Python.
   - Knowledge of Python Signal Handling.

3. **Data Processing**:
   - Parsing strings to extract specific data points.
   - Aggregating data to compute summaries.

4. **Regular Expressions**:
   - Using regular expressions to validate the format of each line.
   - Understanding Python Regular Expressions.

5. **Dictionaries in Python**:
   - Utilizing dictionaries to count occurrences of status codes and accumulate file sizes.
   - Understanding Python Dictionaries.

6. **Exception Handling**:
   - Handling possible exceptions that may arise during file reading and data processing.
   - Knowledge of Python Exceptions.

By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.

#### Additional Resources:
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
- The length of your files will be tested using `wc`

### Tasks
#### 0. Log Parsing
**Score**: 0.0% (Checks completed: 0.0%)

Write a script that reads stdin line by line and computes metrics:

- **Input format**: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
  (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
  - Total file size: `File size: <total size>` (where `<total size>` is the sum of all previous `<file size>`)
  - Number of lines by status code:
    - possible status code: 200, 301, 400, 401, 403, 404, 405, and 500
    - if a status code doesn’t appear or is not an integer, don’t print anything for this status code
    - format: `<status code>: <number>`
    - status codes should be printed in ascending order

For more details, refer to the provided example and sample output.