![Continuous Integration](https://github.com/dashmug/us-covid-stats/workflows/Continuous%20Integration/badge.svg) 
![CodeQL](https://github.com/dashmug/us-covid-stats/workflows/CodeQL/badge.svg)

US COVID Stats
==============

This project is an entry for [#CloudGuruChallenge](https://acloudguru.com/blog/news/introducing-the-cloudguruchallenge) ([Event-Driven Python in AWS](https://acloudguru.com/blog/engineering/cloudguruchallenge-python-aws-etl)) organized by [A Cloud Guru](https://acloudguru.com/).


Challenge
---------

[Event-Driven Python in AWS](https://acloudguru.com/blog/engineering/cloudguruchallenge-python-aws-etl)


Outcome
-------

https://d21xiw2qs8azw2.cloudfront.net/

| Project  | Deployment Status |
|----------|-------------------|
| backend  | ![Build Status](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZGZHNUNDS0JqSnNVSlhyU21zdDB1VnNETVlSVDl6NlV3R3FadHB3TkhYMm1aZlpJNTE5R1NqYUJsOGxrMWgxdkJzQ0w1Y09ibU5TRm5ZYnM4NXR3Mk93PSIsIml2UGFyYW1ldGVyU3BlYyI6IjFkaHQvNkJBR05WK1ZJZWkiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)|
| frontend | ![Build Status](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiRjZFajBNNFlBcEpVall4VXgxTUY3SHFaR1hvcUtwd25lcjBqM21DQ0s2QU9RUityRDBNZXVjcnlpQ0N6SWl0dDdJSGRZRklmVXgwM1pKaDQ0a3M5NWtFPSIsIml2UGFyYW1ldGVyU3BlYyI6InF6aWtXVjJLc25HRklIY0UiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)|

Tech Stack
----------
* Frontend
  * React in Typescript
  * Bulma CSS
  * Apex Charts
  * Hosted on S3 with a CloudFront CDN.
* REST API Backend
  * REST API on API Gateway
  * Lambda Functions in Python
  * Database using DynamoDB
  * S3 for file storage
* ETL Workflow
  * ETL Lambda Functions in Python (using Pandas for Data Processing)
  * Schedule Triggered via CloudWatch/EventBridge Scheduled Event
* Notifications
  * Email notifications provided by SNS
  * Triggered via Lambda Destinations in the ETL workflow
  
   
