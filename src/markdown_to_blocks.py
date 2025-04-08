def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    result = []
    for block in blocks:
        if len(block) == 0:
            continue
        result.append(block.lstrip('\n ').rstrip(' \n'))

    return result

