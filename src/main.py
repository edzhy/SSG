from textnode import *
def main():
    dummy = TextNode('this is some anchor text for the link', TextType.LINK, 'https://www.boot.dev')
    print(dummy.__repr__())
if __name__ == "__main__":
    main()