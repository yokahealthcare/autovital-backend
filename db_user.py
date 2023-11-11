import os

import MySQLdb
import sqlalchemy as db
import uuid
import bcrypt
from dotenv import load_dotenv

# load env variables
load_dotenv()

import smtplib
import ssl
from email.message import EmailMessage

ip_address = "127.0.0.1"
port = "8000"

# define which database that are going to be used
engine = db.create_engine(f"mysql://root:@{ip_address}/autovital2")
# established connection with database
connection = engine.connect()
metadata = db.MetaData()

# template for response
responses = {
    "is_success": False,
    "info": ""
}

# email sender for verification process or others
email_sender = 'erwinwingyonata@gmail.com'


def signup(data: list):
    """

    Args:
        data (list): list containing user data information
                            [username, password, phone, email]

    Returns:
        dictionary of responses
    """

    # define table that we use for register the new user
    table_name = "account"
    table = db.Table(table_name, metadata, autoload_with=engine)

    # checking if the username already taken in database
    query = db.select(db.func.count("*")).select_from(table).where(table.c.username == f"{data[0]}")
    number_of_row = connection.execute(query).scalar()
    if number_of_row > 0:
        # send response to main module
        responses['is_success'] = False
        responses[
            'info'] = f"Failed inserting new data with username '{data[0]}' to database. Username already exist in database"
        return responses

    # generate a UUID for user id
    # ex. 6e621909-a8c4-48ff-8ec8-b2eec48c49bd
    unique_id = str(uuid.uuid4())
    # inserting unique id to 'data' list to first index (front of list)
    data.insert(0, unique_id)

    # hashing the password input
    # generate salt
    salt = bcrypt.gensalt()
    # converting string to bytes
    # hashing password with salt
    hashed = bcrypt.hashpw(data[2].encode('utf-8'), salt)
    # redefine password element on the list with hashed version
    data[2] = hashed

    # get columns of the table
    columns = table.columns.keys()
    # use a dictionary comprehension to create the dictionary
    # reason: we are using dict for easier entry at query statement
    values_dict = {key: value for key, value in zip(columns, data)}

    # SQL query for inserting data
    query = db.insert(table).values(values_dict)

    try:
        # execute the query + commit (must present for inserting data)
        connection.execute(query)
        connection.commit()

        # send email verification
        email_receiver = data[-1]
        # Set the subject and body of the email
        subject = 'AutoVital Accout Verification'
        body = f"Thank You for registering to AutoVital. Verified your account by click this http://{ip_address}:{port}/account/verified?uid={data[0]}"

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()
        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, str(os.getenv("EMAIL_API")))
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        # send response to main module
        responses['is_success'] = True
        responses['info'] = f"Success inserting new data with username '{data[1]}' to database"

        return responses
    except MySQLdb.IntegrityError:
        # send response to main module
        responses['is_success'] = False
        responses['info'] = f"Failed inserting new data with username '{data[1]}' to database"

        return responses


def verified_account(uid: str):
    """

    Args:
        uid: user id that has been registered on database (this will be emailed to user)

    Returns:
        dictionary of response
    """

    # define table that we use for updating verification for user account
    table_name = "account"
    table = db.Table(table_name, metadata, autoload_with=engine)

    # define query for updating verification column on 'account' table
    query = db.update(table).where(table.c.uid == uid).values(verified=1)

    try:
        # execute query
        connection.execute(query)
        connection.commit()

        # send response to main module
        responses['is_success'] = True
        responses['info'] = f"Success updating account verification process"

        return responses
    except MySQLdb.IntegrityError:
        # send response to main module
        responses['is_success'] = False
        responses['info'] = f"Failed updating account verification process"

        return responses


def login(data: list):
    """

    Args:
        data (list): list containing user data information
                            [username, password]

    Returns:
        dictionary of responses
    """

    # define table that we use for login the user
    table_name = "account"
    table = db.Table(table_name, metadata, autoload_with=engine)

    # checking if the username exists in database
    query = db.select(db.func.count("*")).select_from(table).where(table.c.username == f"{data[0]}")
    number_of_row = connection.execute(query).scalar()
    if number_of_row == 0:
        # send response to main module
        responses['is_success'] = False
        responses['info'] = f"Username '{data[0]}' is not exist in database"
        return responses

    # retrieve hashed password information from database
    query = db.select(table.c["password", "verified"]).where(table.c.username == f"{data[0]}")
    hashed_password = connection.execute(query).fetchone()[0]
    # convert user input password & hashed password to bytes type
    hashed_password = hashed_password.encode('utf-8')
    data[1] = data[1].encode('utf-8')
    # checking password
    is_password_correct = bcrypt.checkpw(data[1], hashed_password)

    if not is_password_correct:
        # send response to main module
        responses['is_success'] = False
        responses['info'] = f"Password you entered not correct"
        return responses

    # checking if the account has been verified or not
    account_verified = connection.execute(query).fetchone()[1]
    if not account_verified:
        # send response to main module
        responses['is_success'] = False
        responses['info'] = f"Account you entered has not been verified yet. You must verified first"
        return responses

    # retrieve all user data information from database
    query = db.select(table).where(table.c.username == f"{data[0]}")

    try:
        # execute query
        user_data = connection.execute(query).fetchall()[0]

        # get columns of the table
        columns = table.columns.keys()
        # use a dictionary comprehension to create the dictionary
        # reason: we are using dict for easier entry at query statement
        user_data = {key: value for key, value in zip(columns, user_data)}

        responses['is_success'] = True
        responses['info'] = f"Success to process login operation"
        responses['data'] = user_data

        return responses
    except MySQLdb.IntegrityError:
        # send response to main module
        responses['is_success'] = False
        responses['info'] = f"Failed to process login operation"

        return responses


if __name__ == "__main__":
    pass

