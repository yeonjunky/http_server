class HTTPRequest:
    def parse(self, data):
        header_dict = {}
        data = data.split("\r\n")

        first = data.pop(0).split(" ")

        header_dict["method"] = first[0]
        header_dict[""]
        header_dict["version"] = first[2]

        for i in data:
            if not i:
                continue

            key, val = i.split(": ")
            header_dict[key] = val

        return header_dict
