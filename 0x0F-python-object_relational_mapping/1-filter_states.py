#!/usr/bin/python3
"""
Get list of states that starts letter N
"""


def main():
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], host='localhost', port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%';")
    states = cur.fetchall()

    for data in states:
        print(data)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
