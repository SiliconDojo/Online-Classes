from bottle import run, route
import os
import requests
import sqlite3

command = 'arp -a'
database = 'arp.db'

def db_create():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS arp(mac,vendor)')
    conn.commit()
    conn.close()

def db_find(mac):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    try:
        query = cursor.execute('SELECT * FROM arp where mac = ?',(mac,)) 
        query = query.fetchone()
        print(query)
    except:
        query = ''
    finally:
        conn.close()

    return query

def db_find_all():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    try:
        query = cursor.execute('SELECT * FROM arp') 
        query = query.fetchall()
    except:
        query = ''
    finally:
        conn.close()

    return query

def db_insert(mac, vendor):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    try:
        cursor.execute('UPDATE arp SET vendor = ? where mac = ?',(vendor, mac,))
        if cursor.rowcount == 0:
            cursor.execute('INSERT INTO arp(mac,vendor) values(?,?)',(mac, vendor,))
    except:
        print('database problem')
    finally:
        conn.commit()
        conn.close()

@route('/')
def index():
    page='<table>'
    response = os.popen(command).readlines()

    for line in response:
        if ':' in line:
            record ={'ip':'','mac':'','vendor':''} #Create a Dictionary for Host Values
            line = line.split(' ')
            for value in line:
                if '.' in value:
                    value = value.replace('(', '').replace(')','')
                    record['ip'] = value
                elif ':' in value:
                    record['mac'] = value
            try:
                response_mac = requests.get(f'https://api.maclookup.app/v2/macs/{record['mac']}').json()
                record['vendor'] = response_mac['company']
                if response_mac['company'] == '':
                    record['vendor'] = ''
            except:
                record['vendor'] = ''

            page = f'''
                    {page}
                    <tr>
                        <td>{record['ip']}</td>
                        <td>{record['mac']}</td>
                        <td>{record['vendor']}</td>
                    </tr>
                    '''
            response_query = db_find(record['mac'])
            if response_query == None or response_query[1] == '':
                db_insert(record['mac'],record['vendor'])

    page = f'{page}</table>'

    response_all = db_find_all()
    table_db = '<table>'
    for record in response_all:
        table_db = f'''
                    {table_db}
                    <tr>
                        <td>{record[0]}</td>
                        <td>{record[1]}</td>
                    </tr>
                    '''
    table_db = f'{table_db} </table>'

    page = f'''
            <h1>Latest Response</h1>
            {page}
            <h1>Database Records</h1>
            {table_db}
            '''
    return(page)

db_create()

run(host='127.0.0.1', port=8080)