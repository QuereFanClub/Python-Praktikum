# Zusammenarbeit mit Philip Langenbrink

from datetime import datetime
import time
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


freeID = 1000


def createID():
    global freeID
    id = freeID
    freeID += 1
    return id


def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%d.%m.%Y - %H:%M:%S')


def createEmail(email):
    mailbox_id = connection.execute(f'SELECT id FROM mailbox WHERE name="{email.mailbox}"').fetchone()[0]
    sender_id = connection.execute(f'SELECT id FROM contact WHERE name="{email.sender}"').fetchone()[0]

    timestamp = int(time.mktime(datetime.strptime(email.timestamp, '%d.%m.%Y %H:%M:%S').timetuple()))

    id = createID()
    connection.execute(
        f"""INSERT INTO email (id, mailbox, sender, subject, body, timestamp)
            VALUES ({id}, {mailbox_id}, {sender_id}, "{email.subject}", "{email.content}", {timestamp});""")
    connection.commit()
    return id


def listEmails(mailboxName):
    result = connection.execute(
        f"""SELECT e.id, m.name AS mailbox, c.name AS sender, e.subject, e.body, e.timestamp
            FROM email e
            JOIN mailbox m ON e.mailbox = m.id
            JOIN contact c ON e.sender = c.id
            WHERE m.name="{mailboxName}"
            ORDER BY e.timestamp DESC;""").fetchall()

    emails_dict = {}
    for email_info in result:
        email_id = email_info[0]
        email_data = Email(email_info[1], email_info[2], email_info[3], email_info[4], format_timestamp(email_info[5]))
        emails_dict[email_id] = email_data

    return emails_dict
