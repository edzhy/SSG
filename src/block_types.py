from enum import Enum

class BlockType(Enum):
    paragraph = 'if none of the conditions below apply, it is just a paragraph'
    heading = '[1-6# ]text for the headings' 
    code = '```some wonderful code here```'
    quote = '[>]quote block line must start with a >'
    unordered_list = '[- ] to keep things...unordered'
    ordered_list = '[#. ]where # any number'

def block_to_block_type(block):
    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.heading
    if block.startswith('```') and block.endswith('```'):
        return BlockType.code  
    if block_line_check(block,'>'):
        return BlockType.quote
    if block_line_check(block,'- '):
        return BlockType.unordered_list
    if is_ordered_list(block):
        return BlockType.ordered_list
    return BlockType.paragraph

def block_line_check(block, check_condition):
    block_lines = block.split('\n')
    for line in block_lines:
        if line.startswith(check_condition):
            continue
        else:
            return False
    return True

def is_ordered_list(block):
    block_lines = block.split('\n')
    expected_number = 1
    for line in block_lines:
        expected_prefix = f'{expected_number}. '
        if not line.startswith(expected_prefix):
            return False
        expected_number += 1
    return True
