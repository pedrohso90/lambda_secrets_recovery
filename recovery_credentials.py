import json, os, requests

def lambda_handler(event, context):
    headers =
    secrets_extensions_endpoint = "http://localhost:" + \
    "2773" + \
    "secretsmanager/get/secretId=" + \
    os.environ.get("ARN")

    r = requests.get(secrets_extensions_endpoint, headers=headers)

    secret = json.loads(r.text)["SecretsString"]

    return {
        'statusCode' : 200,
        'body' : json.dumps('Secret: ' + secret)
    }