from datetime import date

def parse_iso(iso):
    iso = map(lambda x: int(x), iso.split('-'))
    return date(*iso)
