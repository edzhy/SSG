def extract_title(markdown):
    md_blocks = markdown.split('\n')
    for md_block in md_blocks:
        if md_block.startswith('# '):
            without_md = md_block.removeprefix('# ')
            stripped_header = without_md.strip()
            return stripped_header
    raise Exception('There is no h1 header in the provided markdown')