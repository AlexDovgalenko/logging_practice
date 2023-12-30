# This is a sample Python script.
import logging

import logging_config
from entities import Port, StructEntity
from level_one.level_two.module_2_1 import hello_from_module_2_1, SomeImportantClass

logging_config.configure_logging()

logger = logging.getLogger(name=__name__)
from level_one.module_1_1 import hello_from_module_1_1, circular_action_with_log_supression


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.

def do_some_stuff():
    logger.info("Calling a function from first level...")
    hello_from_module_1_1()
    logger.info("Calling a function from second level...")
    hello_from_module_2_1()
    important_class = SomeImportantClass()
    important_class.hello_from_important_class()
    logger.info("Calling circular function without suppression...")
    circular_action_with_log_supression(iteration_count=3, supress=False)
    logger.info("Calling circular function with suppression...")
    circular_action_with_log_supression(iteration_count=3, supress=True)
    logger.info("End of script!")


class SomeStuff:
    port_1 = Port(port_name="Port_1", port_type="uint8", temp_val=1)
    port_2 = Port(port_name="Port_2",
                  port_type=[StructEntity(name="Struct_item_2_1", type="uint8"),
                             StructEntity(name="Struct_item_2_2", type="uint8")], temp_val=(21, 22))
    port_3 = Port(port_name="Port_3",
                  port_type=[StructEntity(name="Struct_item_3_1", type="uint8"),
                             StructEntity(name="Struct_item_3_2", type=[
                                 StructEntity(name="Struct_item_3_2_1", type="uint8"),
                                 StructEntity(name="Struct_item_2_2_2", type=[
                                     StructEntity(name="Struct_item_3_2_2_1", type="uint8"),
                                     StructEntity(name="Struct_item_3_2_2_2", type="uint8")])]),
                             StructEntity(name="Struct_item_3_3", type="uint8")],
                  temp_val=(31, (32, (321, 322)), 33))

    def __str__(self):
        class_attribs = [getattr(self, attrib) for attrib in dir(self) if
                         not attrib.startswith("__") and not callable(attrib)]
        str_attribs = [str(attrib) for attrib in class_attribs]
        return "\n".join(str_attribs)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stuff = SomeStuff()
    print(stuff)
    # print(stuff.port_3.type)
    # aaa = 111
    #
    # names = ["Struct_item_2_1", ["Struct_item_2_2_1", ["Struct_item_2_2_2_1", "Struct_item_2_2_2_2"]], "Struct_item_2_3"]
    # values = (21, (221, (2221, 2222)), 23)
    #
    #
    # def stringify_nested_name_value(names, values):
    #     result = []
    #     if not isinstance(names, (list, tuple)) or not isinstance(values, (list, tuple)):
    #         raise ValueError(f"Unable to iterate over not iterable item: names type is '{type(names)}', values type is: '{type(values)}'.")
    #
    #     for name, value in zip(names, values):
    #         if isinstance(name, (list, tuple)):
    #             matched_values = stringify_nested_name_value(name, value)
    #             result.append(matched_values)
    #         else:
    #             result.append(f"{name}: <{value}>")
    #     return result
    #
    # print(stringify_nested_name_value(names, values))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
