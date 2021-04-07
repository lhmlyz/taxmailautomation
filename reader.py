from bs4 import BeautifulSoup
import glob
import pandas as pd
import sqlite3

connection = sqlite3.connect('frame1.db')
c = connection.cursor()
c.execute(
    'CREATE TABLE IF NOT EXISTS mail (doc, documentNumber, documentFrom, documentHeading, documentDate, documentStatus)')
connection.commit()

all_files = glob.glob('.\\temp\\*.html')

for i in range(len(all_files)):
    tables = pd.read_html(all_files[i], flavor='bs4', encoding="utf-8", skiprows=[1])
    for j in range(len(tables)):
        data_frame = tables[j]
        data_frame.rename(columns={
            data_frame.columns[0]: 'doc',
            data_frame.columns[1]: 'documentNumber',
            data_frame.columns[2]: 'documentFrom',
            data_frame.columns[3]: 'documentHeading',
            data_frame.columns[4]: 'documentDate',
            data_frame.columns[5]: 'documentStatus'
        }, inplace=True, errors='raise')
        data_frame.to_sql('mail', connection, schema=None, if_exists='append', index=False)
# if os.path.exists("tax_robot/temp/"):
#     os.remove("tax_robot/temp/result.html")
# else:
#     print("The file or path  does not exits")
