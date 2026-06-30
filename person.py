from generated.protos import person_pb2

def create_person(id:int, name:str, email:str, phone_numbers:list):
    person = person_pb2.Person(
        id=id,
        name=name,
        email=email,
        phone_numbers=phone_numbers
    )

    data = person.SerializeToString()

    return person, data

def parse_person(data):
    person = person_pb2.Person()
    person.ParseFromString(data)

    return person
