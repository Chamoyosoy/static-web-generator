from textnode import TextNode, TextType


def main():
    test = TextNode("This is a text node", TextType.BOLD, "https://www.hola.com")
    print(test)


main()