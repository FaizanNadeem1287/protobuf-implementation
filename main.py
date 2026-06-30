import subprocess

from person import create_person
from person_list import create_person_list

print("Creating person objects and serializing them to a binary file...")

person_1_obj, _ = create_person(
    id=1,
    name="John Doe",
    email="john.doe@example.com",
    phone_numbers=["123-456-7890", "987-654-3210"]
)

person_2_obj, _ = create_person(
    id=2,
    name="Jane Smith",
    email="jane.smith@example.com",
    phone_numbers=["555-123-4567", "555-987-6543"]
)

binary_serialized = create_person_list(
    person_objects=[person_1_obj, person_2_obj]
)

with open("person_list.bin", "wb") as f:
    f.write(binary_serialized)

print("Binary serialized data written to person_list.bin")