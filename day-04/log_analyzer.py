import json

def analyze_logs():
    counts ={
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    try:
        with open("app.log", "r") as file:
            lines = file.readlines()

            if not lines:
                print("log file is empty.")
                return
            
            for line in lines:
                line = line.upper()

                if "INFO" in line:
                    counts["INFO"] += 1
                elif "WARNING" in line:
                    counts["WARNING"] += 1
                elif "ERROR" in line:
                    counts["ERROR"] += 1
                
        return counts
    
    except FileNotFoundError:
        print("ERROR: Log File not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def print_summary(counts):
    print("log summary")
    print(f'INFO : {counts["INFO"]}')
    print(f'WARNING : {counts["WARNING"]}')
    print(f'ERROR : {counts["ERROR"]}')

def log_summary(counts):
    try:
        with open("log_summary.json", 'w+') as file:
            json.dump(counts, file, indent=4)
        print(f"Summary saved to log_summary.json")
    except Exception as e:
        print(f'Failed to write file: {e}')

counts = analyze_logs()
print_summary(counts)
log_summary(counts)