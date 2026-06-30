# protobuf-implementation

A small Python project for practicing Protocol Buffers serialization.

The project defines a `Person` message and a `PersonList` message in `person.proto`, generates Python protobuf classes, creates sample people, serializes them, and writes the serialized output to `person_list.bin`.

## Project Structure

```text
.
|-- main.py          # Generates protobuf code and writes person_list.bin
|-- person.proto     # Protobuf schema
|-- person.py        # Helpers for creating and parsing Person messages
|-- person_list.py   # Helper for creating serialized PersonList data
|-- person_pb2.py    # Generated protobuf Python module
`-- person_list.bin  # Serialized PersonList binary output
```

## Requirements

- Python 3.10 or newer
- `grpcio-tools`

Install the protobuf compiler tools:

```bash
pip install grpcio-tools
```

## Usage

Run the main script:

```bash
python main.py
```

The script will:

1. Generate `person_pb2.py` from `person.proto`.
2. Create two sample `Person` objects.
3. Add them to a `PersonList`.
4. Serialize the list to binary.
5. Save the output to `person_list.bin`.

## Regenerating Protobuf Code Manually

You can also generate `person_pb2.py` directly:

```bash
python -m grpc_tools.protoc -I. --python_out=. person.proto
```

## Example Schema

```proto
syntax = "proto3";

package mypackage;

message Person {
  int32 id = 4;
  string name = 2;
  string email = 3;
  repeated string phone_numbers = 1;
}

message PersonList {
  repeated Person people = 1;
}
```

## Notes

- `person_list.bin` is binary protobuf data, so it is not meant to be read directly as plain text.
- If you update `person.proto`, regenerate `person_pb2.py` before running code that imports it.
