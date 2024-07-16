with open('student.csv', 'r') as file:
    file = file.readlines()

with open('page.html', 'w') as web_page:
    web_page.write('<table>')

    header = file[0].split(',')
    web_page.write('<tr>')
    for value in header:
        web_page.write(f'<th>{value}</th>')
    web_page.write('</tr>')

    #Print All Records
    for line in file[1:]:
        web_page.write('<tr>')
        record = line.split(',')
        for value in record:
            web_page.write(f'<td>{value}</td>')
        web_page.write('</tr>')

    # #Print Records Based on Value
    # for line in file[1:]:
    #     line = line.replace('\n','')
    #     record = line.split(',')
    #     if record[4] == 'Pollen':
    #         web_page.write('<tr>')
    #         for value in record:
    #             web_page.write(f'<td>{value}</td>')
    #     web_page.write('</tr>')

    web_page.write('<table>')
