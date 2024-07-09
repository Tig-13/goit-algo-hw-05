import sys

def parse_log_line(line: str) -> dict:
    parts = line.split(maxsplit=3)
    return {'date': parts[0], 'time': parts[1], 'level': parts[2], 'message': parts[3]}

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    levels = ['INFO', 'ERROR', 'DEBUG', 'WARNING']
    counts = {level: 0 for level in levels}
    for log in logs:
        if log['level'] in counts:
            counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:15} | {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [log_level]")
    else:
        file_path = sys.argv[1]
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        
        if len(sys.argv) == 3:
            level = sys.argv[2].upper()
            filtered_logs = filter_logs_by_level(logs, level)
            print(f"\nДеталі логів для рівня '{level}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")