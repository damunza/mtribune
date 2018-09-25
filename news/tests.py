from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):

    def setUp(self):
        self.new_editor = Editor(first_name = 'daniel', last_name = 'mutai', email = 'abc@abc.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_editor,Editor))

    def test_variables(self):
        self.assertEquals(self.new_editor.first_name, 'daniel')
        self.assertEquals(self.new_editor.last_name, 'mutai')
        self.assertEquals(self.new_editor.email, 'abc@abc.com')

    def test_save(self):
        self.new_editor.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        self.james = Editor(first_name='James', last_name='Muriuki', email='james@moringaschool.com')
        self.james.save_editor()
        self.new_article = Article(title='Test Article', post='This is a random test Post', editor=self.james)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
