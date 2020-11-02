![Continuous Integration](https://github.com/dashmug/us-covid-stats/workflows/Continuous%20Integration/badge.svg) 
![CodeQL](https://github.com/dashmug/us-covid-stats/workflows/CodeQL/badge.svg) 

[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=dashmug_us-covid-stats&metric=code_smells)](https://sonarcloud.io/dashboard?id=dashmug_us-covid-stats) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=dashmug_us-covid-stats&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=dashmug_us-covid-stats) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dashmug_us-covid-stats&metric=alert_status)](https://sonarcloud.io/dashboard?id=dashmug_us-covid-stats) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=dashmug_us-covid-stats&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=dashmug_us-covid-stats) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=dashmug_us-covid-stats&metric=security_rating)](https://sonarcloud.io/dashboard?id=dashmug_us-covid-stats)

[![Maintainability](https://api.codeclimate.com/v1/badges/699f980e3c6ae9612991/maintainability)](https://codeclimate.com/github/dashmug/us-covid-stats/maintainability)

US COVID Stats
==============

This project is an entry for [#CloudGuruChallenge](https://acloudguru.com/blog/news/introducing-the-cloudguruchallenge) ([Event-Driven Python in AWS](https://acloudguru.com/blog/engineering/cloudguruchallenge-python-aws-etl)) organized by [A Cloud Guru](https://acloudguru.com/).


Challenge
---------

[Event-Driven Python in AWS](https://acloudguru.com/blog/engineering/cloudguruchallenge-python-aws-etl)



Outcome
-------

[Live demo](https://d21xiw2qs8azw2.cloudfront.net/)

[Read my blog article about this project.](https://dev.to/dashmug/event-driven-python-in-aws-cloudguruchallenge-20la)

|   | deployment status |
|----------|-------------------|
| Backend  | ![Build Status](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZGZHNUNDS0JqSnNVSlhyU21zdDB1VnNETVlSVDl6NlV3R3FadHB3TkhYMm1aZlpJNTE5R1NqYUJsOGxrMWgxdkJzQ0w1Y09ibU5TRm5ZYnM4NXR3Mk93PSIsIml2UGFyYW1ldGVyU3BlYyI6IjFkaHQvNkJBR05WK1ZJZWkiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)|
| Frontend | ![Build Status](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiRjZFajBNNFlBcEpVall4VXgxTUY3SHFaR1hvcUtwd25lcjBqM21DQ0s2QU9RUityRDBNZXVjcnlpQ0N6SWl0dDdJSGRZRklmVXgwM1pKaDQ0a3M5NWtFPSIsIml2UGFyYW1ldGVyU3BlYyI6InF6aWtXVjJLc25HRklIY0UiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)|

[![Challenge Outcome](images/preview.png?raw=true "Challenge Outcome")](https://d21xiw2qs8azw2.cloudfront.net/)


Tech Stack
----------
* Frontend
  * React in Typescript
  * Bulma CSS
  * Apex Charts
  * Hosted on S3 with a CloudFront CDN.
  ![Frontend](images/Frontend.png?raw=true "Frontend")
* REST API Backend
  * REST API on API Gateway
  * Lambda Functions in Python
  * Database using DynamoDB
  * S3 for file storage
* ETL Workflow
  * ETL Lambda Functions in Python (using Pandas for Data Processing)
  * Workflow Triggered via CloudWatch/EventBridge Scheduled Event and via CodeBuild "Build Successful" event below.
  ![ETL](images/ETL.png?raw=true "ETL")
* Notifications
  * Email notifications provided by SNS
  * Triggered via Lambda Destinations in the ETL workflow
* Deployment Pipeline
  * Separate CodeBuild Projects for frontend/backend. Both triggered via GitHub changes.  
   
