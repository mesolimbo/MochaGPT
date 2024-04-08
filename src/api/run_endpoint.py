import json
from lambda_function import lambda_handler

if __name__ == "__main__":
    # Create a test event
    test_event = {
        # Add any expected keys/values that your Lambda function uses
    }

    # Invoke your Lambda handler
    response = lambda_handler(test_event, None)
    print(json.dumps(response, indent=4))
