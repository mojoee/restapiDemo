from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    }
}


def read_all():
    return list(PEOPLE.values())


def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE.get(lname)
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )

def create(person):
    fname = person.get("fname")
    lname = person.get("lname")
    timestamp = get_timestamp()
    if lname and lname not in PEOPLE:
        PEOPLE[fname] = {
            "fname": fname,
            "lname": lname,
            "timestamp": timestamp,
        }
        return PEOPLE[fname]
    else:
        abort(
            406, 
            f"Person with last name {lname} already exists"
        )

def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )

def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )