import argparse
from DariasSerializer153501.serialiser_fabric import Serializer_fabric

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My serializer for xml, json")
    parser.add_argument("file_from", type=str, help="file from which you load data")
    parser.add_argument("file_to", type=str, help="file to which you save serialized data")
    parser.add_argument("format_from", type=str, help="format from which you serialize data," + \
                                                      "can be any of json/xml")
    parser.add_argument("format_to", type=str, help="format to which you serialize data," + \
                                                    "can be any of json/xml")

    args = parser.parse_args()

    from_serializer = Serializer_fabric.create_serializer(args.format_from)
    to_serializer = Serializer_fabric.create_serializer(args.format_to)


    with open(args.file_from) as f_file:
        obj = from_serializer.load(f_file)

    print(type(obj), obj)

    with open(args.file_to, "w") as t_file:
        to_serializer.dump(obj, t_file)