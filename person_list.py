from generated.protos.person_pb2 import PersonList
from generated.protos.person_pb2 import Person

def create_person_list(person_objects:list[Person]):
    person_list = PersonList(
        people=person_objects
    )

    data = person_list.SerializeToString()

    return data

