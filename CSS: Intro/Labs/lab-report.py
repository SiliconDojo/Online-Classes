with open('student.csv', 'r') as file:
    file = file.readlines()

with open('report.html', 'w') as report:
    report.write('<table>')

    for line in file[1:]:
        record = line.split(',')

        if record[4].strip() == 'Pollen':
            color = 'yellow'
        else:
            color = ''
        report.write(f'<tr style="background-color:{color}">')

        for value in record:
            report.write(f'<td>{value}</td>')

        report.write('</tr>')

    report.write('</table>')

    
