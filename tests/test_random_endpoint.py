from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.api.random_endpoint import lambda_handler, random_item


class Test(TestCase):

    @patch("boto3.resource")
    def test_random_item_with_no_items(self, mock_boto3):
        # Create a mock dynamodb table with no items
        mock_table = MagicMock()
        mock_table.scan.return_value = {'Items': []}

        # Mock the boto3 resource and return the mock table
        mock_dynamodb = MagicMock()
        mock_dynamodb.Table.return_value = mock_table
        mock_boto3.return_value = mock_dynamodb

        # Ensure random_item and lambda_handler return the correct result when no items are found
        self.assertEqual(random_item(), {'message': 'No keys found in the table'})
        self.assertEqual(lambda_handler(None, None), {'message': 'No keys found in the table'})

    @patch("boto3.resource")
    def test_random_item(self, mock_boto3):
        # Create a mock dynamodb table
        mock_table = MagicMock()
        mock_table.scan.return_value = {'Items': [{'BeverageID': '1'}]}
        mock_table.get_item.return_value = {'Item': {'BeverageID': '1', 'Name': 'Coffee'}}

        # Mock the boto3 resource and return the mock table
        mock_dynamodb = MagicMock()
        mock_dynamodb.Table.return_value = mock_table
        mock_boto3.return_value = mock_dynamodb

        self.assertEqual(random_item(), {'BeverageID': '1', 'Name': 'Coffee'})
