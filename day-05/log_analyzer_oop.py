import json

class LogAnalyzer:
    def __init__(self,log_file,output_file):
        self.log_file = log_file
        self.output_file = output_file
        self.counts ={
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }

    def analyze_logs(self):
        try:
            with open(self.log_file, "r") as file:
                lines = file.readlines()

                if not lines:
                    print("log file is empty.")
                    return
                
                for line in lines:
                    line = line.upper()

                    if "INFO" in line:
                        self.counts["INFO"] += 1
                    elif "WARNING" in line:
                        self.counts["WARNING"] += 1
                    elif "ERROR" in line:
                        self.counts["ERROR"] += 1
                    
        
        except FileNotFoundError:
            print("ERROR: Log File not found.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        self.print_summary()

    def print_summary(self):
        print("\nlog summary")
        print(f'INFO : {self.counts["INFO"]}')
        print(f'WARNING : {self.counts["WARNING"]}')
        print(f'ERROR : {self.counts["ERROR"]}')
        self.log_summary()

    def log_summary(self):
        try:
            with open(self.output_file, 'w+') as file:
                json.dump(self.counts, file, indent=4)
            print(f"Summary saved to {self.output_file}")
        except Exception as e:
            print(f'Failed to write file: {e}')

    
if __name__ == "__main__":
    log = LogAnalyzer("app.log","log_summary.json")
    log.analyze_logs()