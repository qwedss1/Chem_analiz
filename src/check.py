import sqlite3 as sq
def check(self,R):
    state = True
    conn = sq.connect('db.db')
    cur = conn.cursor()
    for n in range(0,len(R["R"])):
        a = "SELECT Tmax FROM therdb WHERE formula='"+ str(R["R"][n][0]) + "'"
        cur.execute(a)
        b = int(cur.fetchone()[0])
        if b < R["T"]:
            state = False
            break
    for n in range(0,len(R["P"])):
        a = "SELECT Tmax FROM therdb WHERE formula='"+ str(R["P"][n][0]) + "'"
        cur.execute(a)
        b = int(cur.fetchone()[0])
        if b < R["T"]:
            state = False
            break
    return state
