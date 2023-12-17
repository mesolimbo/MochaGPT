# Starbucks Drinks Catalog - AWS Project Summary

## Project Overview
The goal is to create a serverless Python API using AWS services to serve data from Starbucks drinks CSV files. The API will support REST queries and utilize AWS Lambda, Amazon API Gateway, and DynamoDB.

## Steps Accomplished So Far

### Data Preparation and Loading
1. **CSV File Analysis**: Analyzed and combined two CSV files containing Starbucks drinks data.
2. **Data Cleaning**: Cleaned and merged the data, ensuring consistency across the datasets.
3. **DynamoDB Preparation**:
   - Created table StarbucksDrinksCatalog and CloudWatch dashboard
   - Chose `BeverageID` (a combination of `Beverage` and `Beverage_prep`) as the primary key.
   - Transformed the data into a format suitable for DynamoDB.
4. **Data Loading**:
   - Utilized Boto3 in Python to load the transformed data into DynamoDB.
   - Verified the integrity of the data in the DynamoDB table against the original CSV files.

### AWS Configuration and Monitoring
- Set up AWS credentials for programmatic access using Boto3.
- Configured Amazon CloudWatch for monitoring DynamoDB and Lambda functions.

## Next Steps

### 1. Verify Data Integrity
- Ensure data in DynamoDB matches the original CSV files.

### 2. Develop Serverless API
- Create AWS Lambda functions in Python to handle API requests.
- Implement logic to query DynamoDB and return data.

### 3. Set Up API Endpoints
- Configure endpoints in Amazon API Gateway.
- Connect API Gateway to Lambda functions.

### 4. API Testing and Validation
- Test API functionality and robustness.
- Implement error handling and edge case scenarios.

### 5. Security and Access Control
- Secure the API using IAM roles and policies.
- Implement necessary authentication and authorization.

### 6. Documentation
- Document API endpoints and usage instructions.

### 7. Monitor and Optimize
- Use CloudWatch to monitor performance and costs.
- Optimize Lambda functions for efficiency.

### 8. Future Enhancements
- Consider features like caching and additional AWS integrations.

---

*Note: This document provides a summary of the steps and progress made in the project as of the current date.*
