import request
import boto3
from bottle import route, run, request

@route("/")
def index(q=""):
    a = request.query.get("q")
    return "<h1> Input is {name}<h1>".format(name=a)

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

    print(
                "Hello"
        "World"
        )
    c = index()


if __name__ == '__main__':
    main()