#This code block is an example of list creation and manipulation using python commands.
#Author: Paul Hill 4/1/2023

#Create a list. Add AWS service items to the list.
aws_serv = []
aws_serv.append('ec2')
aws_serv.append('vpc')
aws_serv.append('s3')
aws_serv.append('dynamodb')
aws_serv.append('lambda')
aws_serv.append('codebuild')
aws_serv.append('codedeploy')
aws_serv.append('iam')
aws_serv.append('codecommit')
aws_serv.append('sqs')
print("This is my list of AWS services:")
print(aws_serv, '\n')
print("The length of my list is a 'len' function. The answer is ", + len(aws_serv), '\n')
#Delete two items from the list. Print the results.
del aws_serv[5:7] #Delete using an splice.
print("I deleted codebuild and codedeploy from my list.")
print("My new list is: ", (aws_serv), '\n')
print("The length of my new list is a 'len' function. The answer is ", + len(aws_serv))

