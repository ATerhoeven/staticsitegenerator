import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.LINK, url="https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.LINK, url="https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_neq2(self):
        node = TextNode("This is a text node", TextType.LINK, url="https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.LINK, url="https://www.youtube.com")
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("print('hello world')", TextType.CODE)
        node2 = TextNode("print('hello world')", TextType.CODE)
        self.assertEqual(node, node2)

    def test_neq3(self):
        node = TextNode("Hey, how are you?", TextType.PLAIN)
        node2 = TextNode("Yo, I'm fine.", TextType.PLAIN)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()