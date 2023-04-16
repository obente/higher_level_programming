#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()

    for data in states:
        print(data)

    db.close()
