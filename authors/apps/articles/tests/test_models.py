from authors.apps.authentication.tests_.test_base_class import BaseTestClass
from authors.apps.articles.models import Article, ArticleRating,ReportArticle
from authors.apps.articles.utils import get_average_value


class ArticleModelTest(BaseTestClass):
    def test_article_representation(self):
        """
         Tests the return datatype of the article elements
         """
        self.assertIsInstance(self.article, dict)

    def test_article_model(self):
        """
        This function validates the internal state of the model to ensure
        it returns the correct values
        """
        self.assertEqual(self.article['title'], "hello worlfd")
        self.assertEqual(self.article['description'], "desctriptuo")
        self.assertEqual(self.article['body'], "boddydydabagd")

    def test_str_returns_correct_string_representation(self):
        """
        Tests that __str__ generates a correct string representation of
        article title
        """
        article = Article(title="Hello today",
                          description="Today is beautiful",
                          body="This is the body")
        self.assertEqual(str(article), "Hello today")
    
    def test_str_returns_correct_article_report_string_representation(self):
        """
        Tests that __str__ generates a correct string representation of
         reported article title
        """
        report = ReportArticle.objects.create(
            reporter=self.test_user,
            reported_article=self.created_article,
            reason="Contains bad language"
        )
        self.assertEqual(f"{self.created_article.title} reported by {self.test_user.username}", str(report))
