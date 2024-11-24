class Band:
    bands = []

    def __init__(self, name):
        self.name = name

    def __str__(self):
        band_list = ', '.join(str(i) for i in self.bands)
        return f"{self.name}({band_list})"

    def add(self, band):
        self.bands.append(band)