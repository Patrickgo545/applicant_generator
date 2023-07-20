import characteristics_generator

def read_query_component(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

intro_block = read_query_component('./query_component_blocks/intro_block.txt')
parameters_block = read_query_component('./query_component_blocks/parameters_block.txt')
instruction_block = read_query_component('./query_component_blocks/instruction_block.txt')
final_instruction = read_query_component('./query_component_blocks/final_instruction.txt')
json_health_equity_questionnaire = \
    read_query_component('./query_component_blocks/json_health_equity_questionnaire.txt')

characteristics_block = ('Here are some characteristics I want you to apply to this individual ' , \
                         characteristics_generator.characteristics_dictionary)

complete_query = [intro_block, parameters_block , instruction_block , characteristics_block , \
                  final_instruction , json_health_equity_questionnaire]

print(complete_query)