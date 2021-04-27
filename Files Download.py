from urllib import request

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1557813176&period2=1589435576&interval=1d&events=history'
# Line 3 what to download

def download_stats(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
# Line 6, 7, 8 is connect to internet

    csv_str = str(csv)
    lines = csv_str.split("\\n")
# Line 11, 12 - Save it as string

    dest_url = r'goog.csv'
    fw = open(dest_url, 'w')
# Line 15, 16 - Make the file in our computer
    for line in lines:
        fw.write(line + '\n')
    fw.close()
# Line 18, 19, 20 - Write to the file

download_stats(goog_url)
