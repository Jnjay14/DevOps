# test_parse_articles.py

import unittest
from parse_articles import parse_article


class TestArticleParsing(unittest.TestCase):

    def test_simple_article(self):
        raw = "Breaking News\n\nThis is the article body."
        result = parse_article(raw)
        self.assertEqual(result["title"], "Breaking News")
        self.assertEqual(result["body"], "This is the article body.")

    def test_article_without_body(self):
        raw = "Only Title"
        result = parse_article(raw)
        self.assertEqual(result["title"], "Only Title")
        self.assertEqual(result["body"], "")  # body should be empty


if __name__ == "__main__":
    unittest.main()
