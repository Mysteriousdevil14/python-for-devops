import json
import argparse
import os 

class LogAnalyzer:
    def __init__(self,log_file,output_file=None,level=None):
        self.log_file = log_file
        self.output_file = output_file
        self.level = level.upper() if level else None
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

                    if self.level:
                        if self.level in line:
                            self.counts[self.level] +=1
                    else:
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
        for key,value in self.counts.items():
            print(f"{key:8} : {value}")
        
        self.log_summary()

    def log_summary(self):
        try:
            with open(self.output_file, 'w+') as file:
                json.dump(self.counts, file, indent=4)
            print(f"Summary saved to {self.output_file}")
        except Exception as e:
            print(f'Failed to write file: {e}')

def parse_args():
    parser = argparse.ArgumentParser(description="Simple log analyser CLI tool")

    parser.add_argument(
        "--file",
        required=True,
        help="Path to log file"
    )

    parser.add_argument(
        "--out",
        help="Output file path (optional)"
    )

    parser.add_argument(
        "--level",
        choices=["INFO", "WARNING", "ERROR"],
        help="Filter logs by level (optional)"
    )

    return parser.parse_args()

    
if __name__ == "__main__":
    args = parse_args()
    if not os.path.exists(args.file):
        print("ERROR: Provided log file does not exist.")
        exit(1)
    

    log = LogAnalyzer(
        log_file= args.file,
        output_file=args.out,
        level=args.level
        )
    log.analyze_logs()