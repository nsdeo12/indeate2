from methods.methods import select_system_boundary, generate_requirements, select_sustainability_definitions, select_sustainability_indicators , select_methods_tc
from methods.save_methods import save_system_boundary, save_generate_requirements
from methods.get_methods  import get_system_boundary, get_generate_requirements

STEPS_NAME = {
    '1': "Select System Boundary",
    '2': "Generate Requirements",
    '3': "Select Sustainability Definitions",
    '4': "Select Sustainability Indicators",
    '5': "Select Methods TC in the task clarification phase",

}

STEPS_METHODS = {
    '1': select_system_boundary,
    '2': generate_requirements,
    '3': select_sustainability_definitions,
    '4': select_sustainability_indicators,
    '5': select_methods_tc
}

SAVE_STEPS_METHODS = {
    1: save_system_boundary,
    2: save_generate_requirements
}

GET_METHODS_DATA = {
    1: get_system_boundary,
    2 : get_generate_requirements
}