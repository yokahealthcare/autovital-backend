from datetime import datetime
import os

import MySQLdb
import sqlalchemy as db
import uuid
import bcrypt
from dotenv import load_dotenv

# load env variables
load_dotenv()

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


def list_all_car():
    """
    loaded all car available on the database
    Returns:
        JSON containing car data
    """

    # define table
    table_name = "car"
    table = db.Table(table_name, metadata, autoload_with=engine)

    # select all data from database
    query = db.select(table)

    try:
        # execute query
        result = connection.execute(query).fetchall()
        # change to dictionary structure
        ad = {key: (brand, model, thumbnail) for key, brand, model, thumbnail in result}

        responses['is_success'] = True
        responses['info'] = f"Success to load car from database"
        responses['data'] = ad

        return responses
    except MySQLdb.IntegrityError:
        # send response to main module
        responses['is_success'] = False
        responses['info'] = f"Failed to load car from database"

        return responses


def add_car(ncar: dict):
    """
    add new car to database
    Returns:
        JSON containing success status
    """

    # define table
    table_name = ["automotive", "oil", "oil_filter", "fuel_filter", "air_filter", "breakpad"]
    table_connection = []
    for table in table_name:
        temp = db.Table(table, metadata, autoload_with=engine)
        table_connection.append(temp)
    # make table connection convenient with dictionary
    table = {key: val for key, val in zip(table_name, table_connection)}

    # separate the 'data' key
    values_dict = {key: val for key, val in ncar.items() if key != "data"}

    # write to 'car' table
    # generate a UUID for car id
    # ex. 6e621909-a8c4-48ff-8ec8-b2eec48c49bd
    unique_id = str(uuid.uuid4())
    # inserting unique id to 'data' list to first index (front of list)
    values_dict['aid'] = unique_id

    query = db.insert(table["automotive"]).values(values_dict)

    try:
        # execute the query + commit (must present for inserting data)
        connection.execute(query)
        connection.commit()

        # insert all component
        id_name = ["oid", "ofid", "ffid", "afid", "bpid"]
        for idx, cname in enumerate(table_name[1:]):
            add_component(table[cname], unique_id, ncar['data'][cname], id_name[idx])

        # send response to main module
        responses['is_success'] = True
        responses['info'] = f"Success inserting new car data"

        return responses

    except MySQLdb.IntegrityError:
        # send response to main module
        responses['is_success'] = False
        responses['info'] = f"Failed inserting new data to database 'car'"

        return responses


def add_component(table: db.Table, aid: str, data: dict, id_name: str):
    """
    insert component to database
    Returns:
        JSON containing success status
    """

    # write to 'oil' table
    # generate a UUID for user id
    # ex. 6e621909-a8c4-48ff-8ec8-b2eec48c49bd
    unique_id = str(uuid.uuid4())
    # inserting unique id to 'data' list to first index (front of list)
    data[id_name] = unique_id

    # add column aid
    data['aid'] = aid
    # convert string to datetime object
    data["last_change"] = datetime.strptime(data["last_change"], "%d/%m/%Y")
    query = db.insert(table).values(data)

    # execute
    connection.execute(query)
    connection.commit()


def load_car(automotive_id: str):
    """
    load selected automotive id
    Returns:
        JSON containing automotive data
    """

    # define table
    table_name = ["automotive", "oil", "oil_filter", "fuel_filter", "air_filter", "breakpad"]
    table_connection = []
    for table in table_name:
        temp = db.Table(table, metadata, autoload_with=engine)
        table_connection.append(temp)
    # make table connection convenient with dictionary
    table = {key: val for key, val in zip(table_name, table_connection)}

    # select all data from database
    query = db.select(table["automotive"])

    try:
        # execute query
        result = connection.execute(query).fetchall()
        # make dictionary same as the request add new car structure
        result = {key: value for key, value in zip(table["automotive"].columns.keys(), result[0])}

        # load components
        # Define the components and their corresponding table names
        component_tables = {
            "oil": table["oil"],
            "oil_filter": table["oil_filter"],
            "fuel_filter": table["fuel_filter"],
            "air_filter": table["air_filter"],
            "breakpad": table["breakpad"]
        }

        # Define keys used for all components
        keys = ["compid", "name", "last_change"]

        # Load each component and create a dictionary for each
        components_data = {}
        for component_name, component_table in component_tables.items():
            component_data = load_component(component_table, result["aid"])[0][:-1]
            components_data[component_name] = {key: value for key, value in zip(keys, component_data)}

        # Append the dictionary of components to the 'result' variable
        result["data"] = components_data

        responses['is_success'] = True
        responses['info'] = f"Success to load car from database"
        responses['data'] = result

        return responses
    except MySQLdb.IntegrityError:
        # send response to main module
        responses['is_success'] = False
        responses['info'] = f"Failed to load car from database"

        return responses


def load_component(table: db.Table, automotive_id: str):
    """
    insert component to database
    Returns:
        JSON containing success status
    """

    # select all component from table
    query = db.select(table).where(table.c.aid == automotive_id)

    # execute
    return connection.execute(query).fetchall()


def delete_car(automotive_id: str):
    """
    delete car from database
    Returns:
        JSON containing success status
    """

    # define table
    table_name = ["automotive", "oil", "oil_filter", "fuel_filter", "air_filter", "breakpad"]
    table_connection = []
    for table in table_name:
        temp = db.Table(table, metadata, autoload_with=engine)
        table_connection.append(temp)
    # make table connection convenient with dictionary
    table = {key: val for key, val in zip(table_name, table_connection)}

    try:

        # delete all component - first
        for idx, cname in enumerate(table_name[1:]):
            delete_component(table[cname], automotive_id)

        # delete the automotive data - second
        query = db.delete(table["automotive"]).where(table["automotive"].c.aid == automotive_id)
        # execute the query + commit (must present for inserting data)
        connection.execute(query)
        connection.commit()

        # send response to main module
        responses['is_success'] = True
        responses['info'] = f"Success delete automotive data"

        return responses

    except MySQLdb.IntegrityError:
        # send response to main module
        responses['is_success'] = False
        responses['info'] = f"Failed delete automotive data"

        return responses


def delete_component(table: db.Table, automotive_id: str):
    """
        delete component to database
        Returns:
            JSON containing success status
        """

    # delete component from table certain aid
    query = db.delete(table).where(table.c.aid == automotive_id)

    # execute
    connection.execute(query)


if __name__ == "__main__":
    pass
