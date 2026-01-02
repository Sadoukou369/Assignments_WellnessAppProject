from datetime import date

# INTEGER VALIDATION

def get_int(num):
    try:
        return int(num)
    except:
        return None


def get_int_range(num, low, high):
    value = get_int(num)

    if value is None:
        return None

    if value < low or value > high:
        return None

    return value


# DATE VALIDATION

def get_date(str_date):
    # Format check: MM/DD/YYYY -> must be length 10 & slashes at 2 and 5
    if len(str_date) != 10 or str_date[2] != "/" or str_date[5] != "/":
        return None

    parts = str_date.split("/")

    if len(parts) != 3:
        return None

    month = get_int(parts[0])
    day = get_int(parts[1])
    year = get_int(parts[2])

    if month is None or day is None or year is None:
        return None

    try:
        return date(year, month, day)
    except:
        return None


if __name__ == "__main__":
    pass
