from datetime import datetime

def parse_datetime(value):
    try:
        return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
    except (ValueError, TypeError):
        return None
