FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    dispaly_results(champion_to_count, countries)


def get_records(filename):
    """Get records from file in list of lists form."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(".")
            records.append(parts)
        return records