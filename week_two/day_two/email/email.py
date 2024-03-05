# Zusammenarbeit mit Philip Langenbrink

import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE mailbox(id INTEGER PRIMARY KEY, name TEXT);")
connection.execute("CREATE TABLE contact(id INTEGER PRIMARY KEY, address TEXT, name TEXT);")
connection.execute(
    "CREATE TABLE email(id INTEGER PRIMARY KEY, mailbox INT, sender INT, subject TEXT, body TEXT, timestamp TIMESTAMP)")
connection.commit()


class Email:
    def __init__(self, mailbox, sender, subject, content, timestamp):
        self.mailbox = mailbox
        self.sender = sender
        self.subject = subject
        self.content = content
        self.timestamp = timestamp


free_id = 1000


def createID():
    global free_id
    id = free_id
    free_id += 1
    return id


def createEmail(email):
    id = createID()
    connection.execute(
        f"""insert into email (id, mailbox, sender, subject, body, timestamp) values ({id}, {email.mailbox}, {email.sender}, "{email.subject}", "{email.content}", {email.timestamp});""")
    connection.commit()
    return id


def deleteEmail(emailID):
    connection.execute(f"""delete from email where id = {emailID};""")
    connection.commit()


def listEmails(mailboxID):
    result = connection.execute(f"""select id, * from email where mailbox = {mailboxID} order by timestamp desc;""").fetchall()
    emails_dict = {}
    for email_info in result:
        email_id = email_info[0]
        email_data = Email(email_info[2], email_info[3], email_info[4], email_info[5], email_info[6])
        emails_dict[email_id] = email_data
    return emails_dict
