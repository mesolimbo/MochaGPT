# MochaGPT - Starbucks Drinks GPT Action

[![Python application](https://github.com/mesolimbo/MochaGPT/actions/workflows/python-app.yml/badge.svg)](https://github.com/mesolimbo/MochaGPT/actions/workflows/python-app.yml)

## Overview

This serverless Python API uses AWS services to provide data from a Starbucks drinks table to ChatGPT. The API support GET queries and utilize AWS Lambda, Amazon API Gateway, and DynamoDB.

## Project Details

### Data Preparation and Loading

The data for this project came from a kaggle data set:
https://www.kaggle.com/datasets/starbucks/starbucks-menu

1. **CSV File Analysis**: Analyzed and combined two CSV files containing Starbucks drinks data using ChatGPT.
2. **Data Cleaning**: Cleaned and merged the data, ensuring consistency across the datasets.
3. **DynamoDB Preparation**:
   - Created table StarbucksDrinksCatalog and CloudWatch dashboard.
   - Chose `BeverageID` (a combination of `Beverage` and `Beverage_prep`) as the primary key.
   - Transformed the data into a format suitable for DynamoDB.
4. **Data Loading**:
   - Utilized Boto3 in Python to load the transformed data into DynamoDB.
   - Verified the integrity of the data in the DynamoDB table against the original CSV files.

### AWS Configuration and Monitoring
- Set up AWS credentials for programmatic access using Boto3.
- Configured Amazon CloudWatch for monitoring DynamoDB and Lambda functions.

### Lambda Function Development
- Developed an AWS Lambda function in Python to handle API requests.
- The function is capable of querying DynamoDB to retrieve random beverage data.
- Set up necessary permissions for Lambda to access DynamoDB.
- Successfully tested the Lambda function locally.

### Lambda Deployment and API Gateway Integration
- Deployed the Lambda function to AWS.
- Created a Lambda URL for direct invocation of the function.
- Successfully integrated the Lambda function with Amazon API Gateway.
- Set up an API endpoint (`/random`) to access the Lambda function.
- Created an OpenAPI definition for the `/random` endpoint.

## Future Updates

### Monitor and Optimize
- Use CloudWatch to monitor API and Lambda performance.
- Optimize configurations for efficiency and cost-effectiveness.

### Additional Features and Enhancements
- Consider adding more features to the API based on user feedback.
- Explore opportunities for scaling and improving the system architecture.
