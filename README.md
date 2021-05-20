# image-tag
An image object detection serverless app using aws

## Usage

### Run SAM locally:
1. Install AWS Serverless Application Model (SAM) by following through https://aws.amazon.com/serverless/sam/
2. Configure your SAM 
3. Deploy the service on to the AWS

### Run SAM on aws cloud9:

SAM has been pre-installed on cloud9, you can check it by:
```
sam --version
```

Build the template and download the dependency. You'll notice there will be a new template.yaml file been created in the .aws-sam/build folder:
```
sam build --template lambda-dependency-sam.yaml --manifest ./lambdacode/requirements.txt
```

After successful build, invoke the function locally:
```
sam local invoke --event ./lambdacode/test1.json
```

Package:
```
sam package --template-file .aws-sam/build/template.yaml --s3-bucket demo-warren-s3-bucket-2021 --output-template-file packaged-lambda-dependency.yaml
```

Deploy:
```
sam deploy --stack-name lambdadepen --template-file packaged-lambda-dependency.yaml --s3-bucket demo-warren-s3-bucket-2021 --capabilities CAPABILITY_IAM --region ap-southeast-2
```