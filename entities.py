import logging

logger = logging.getLogger()


class Port:
    def __init__(self, port_name, port_type, temp_val):
        self.__name = port_name
        self.__type = port_type
        self.__value = None
        self.__temp_val = temp_val

    def __str__(self):
        if isinstance(self.__type, str):
            return f"{self.name}: <{self.value}>"
        elif isinstance(self.__type, (list, tuple)):
            str_port_data = self.__stringify_name_value_circular(names=self.__return_struct_names(), values=self.value)
            return f"{self.name}: {str_port_data}"
        else:
            raise ValueError(f"Port type must be one of String, List or Tuple, but {type(self.__type)} was supplied.")

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        if isinstance(self.__type, (list, tuple)):
            return [item.type for item in self.__type]
        return self.__type

    @property
    def value(self):
        return self.__return_value()

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __return_value(self):
        return self.__temp_val

    def __return_struct_names(self):
        if isinstance(self.__type, (list, tuple)):
            return [item.name for item in self.__type]
        else:
            raise ValueError("Unable return list of structure names for non-iterable type.")

    def __stringify_name_value_circular(self, names, values):
        """Returns string representation of structure names and corresponding values in case of nested structures.

        This function become handy when we have a deal with nested Structures e.g.
        names = ["Struct_item_1", ["Struct_item_2", ["Struct_item_2_1", "Struct_item_2_2"]], "Struct_item_3"]
        values = [1, [2, [21, 22]], 3]
        result: "[Struct_item_1: <1>, [Struct_item_2: <2>, [Struct_item_2_1: <21>, Struct_item_2_2: <22>]], Struct_item_3: <3>]"
        """
        result = []
        if not isinstance(names, (list, tuple)) or not isinstance(values, (list, tuple)):
            raise ValueError(
                f"Unable to iterate over not iterable item: names type is '{type(names)}', values type is: '{type(values)}'.")

        for name, value in zip(names, values):
            if isinstance(name, (list, tuple)):
                matched_values = self.__stringify_name_value_circular(name, value)
                result.append(matched_values)
            else:
                result.append(f"{name}: <{value}>")
        return f"[{', '.join(result)}]"


class StructEntity:
    def __init__(self, name, type):
        self.__name = name
        self.__type = type

    @property
    def name(self):
        if isinstance(self.__type, (list, tuple)):
            return [item.name for item in self.__type]
        return self.__name

    @property
    def type(self):
        if isinstance(self.__type, (list, tuple)):
            return [item.type for item in self.__type]
        return self.__type
