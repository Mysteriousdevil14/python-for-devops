# Log Analyzer CLI Tool - Design


## 1. What is the problem?

System logs contain important information such as INFO, WARNING, and ERROR messages.
Manually reading logs to understand system health is time-consuming.
This CLI tool automates the rocess of analyzing log files and summarizing log levels.



## 2. What input does it need?

This script requires the following inputs:

1. --file (required)
  Path to the log file (e.g., app.log)

2. --out (optional)
  Path to save the summary output (e.g., summary.json)

3. --level (optional)
  Filter logs by a specific level:
  - INFO
  - WARNING
  - ERROR



## 3. What output should it give?

1. Terminal Output:
    Count of each log level (INFO, WARNING, ERROR)

2. File Output (optional):
   JSON file containing log summary
   Example:
   {
       "INFO": 10,
       "WARNING": 3,
       "ERROR": 1
   }



## 4.  What steps are involved?

1. Parse command-line arguments
   Read --file, --out, --level

2. Validate input
   Check if the log file exists

3. Read log file
   Open the file and read all lines

4. Process logs
   Convert each line to uppercase
   If --level is provided:
    Count only that specific level
   Else:
    Count INFO, WARNING, and ERROR occurrences

5. Print summary
   Display counts in terminal

6. Save summary (optional)
   If --out is provided:
    Write results to a JSON file
