import request
import boto3


def main():
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(Bucket='example-bucket')

    for content in response['Contents']:
        print(content['Key'])

    print('this is a % test'.format)

    a = 'abc'
    b = 'bcd'
    if a <> b:
        print ('not equal')

def foo():
    print(
                "Hello"
        "World"
        )


if __name__ == '__main__':
    main()