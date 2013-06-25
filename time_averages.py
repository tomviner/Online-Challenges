"""
Total duration: 18:49
"""

def test_example():
    in_time1 = "00:02:20"
    in_time2 = "00:04:40"
    expected = "00:03:30"
    assert average_times(in_time1, in_time2) == expected

def test_edge_cases():
    assert average_times("00:00:00", "00:00:00") == "00:00:00"
    assert average_times("02:02:02", "00:00:00") == "01:01:01"
    # fractions of a hundredth?
    assert average_times("00:00:01", "00:00:00") == "00:00:00" #?

def test_parse_time():
    assert parse_time("15:02:20") == 15*60*100 + 2*100 + 20

def test_generate_time():
    assert generate_time(15*60*100 + 2*100 + 20) == "15:02:20"

def parse_time(in_time):
    """
    convert a "MM:SS:HS" time string to hundredths of seconds
    assumes correct format supplied
    """
    m, s, h = map(int, in_time.split(':'))
    return m*60*100 + s*100 + h

def generate_time(hundredths):
    """
    convert a time in hundredths to "MM:SS:HS" format
    rounding down any fractions of hundredths
    """
    m, rest = divmod(hundredths, 60*100)
    s, rest = divmod(rest, 100)
    h = rest
    return '%02d:%02d:%02d' % (m, s, h)

def average_times(in_time1, in_time2):
    """
    accept two lap times and calculate their average
    """
    hundredths = (parse_time(in_time1) + parse_time(in_time2)) / 2
    return generate_time(hundredths)