from django.test import TestCase
from django.utils import timezone
from .models import AccountInfo, ExpenseInfo

class BackendTests(TestCase):
    def setUp(self):
        # Create a sample account for testing
        self.account = AccountInfo.objects.create(username='testuser', password='testpassword', user_budget=100)

    def tearDown(self):
        # Clean up any created test data
        AccountInfo.objects.all().delete()

    def test_account_info(self):
        self.assertEqual(self.account.username, 'testuser')
        self.assertEqual(self.account.password, 'testpassword')
        self.assertEqual(self.account.user_budget, 100)

    def test_expense_info(self):
        expense = ExpenseInfo.objects.create(expense_name='Test Expense', expense_amount=50, expense_date=timezone.now(),
                                             expense_category='TestCategory', expense_description='Test Description',
                                             expense_location='Test Location', user=self.account)
        self.assertEqual(expense.expense_name, 'Test Expense')
        self.assertEqual(expense.expense_amount, 50)
        # Add more assertions as needed

    # Add more test methods for other functionalities if required
