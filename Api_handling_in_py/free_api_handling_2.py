import requests

def user_login():
    url="https://api.freeapi.app/api/v1/users/google"
    response=requests.get(url)
    info=response.json()
    # print(info)
    status_code=info["statusCode"]
    flag=info['success']
    error=info['errors']

    return status_code,flag,error

def main():
    s1,s2,s3=user_login()
    print(s1,s2,s3)
    # user_login()

if __name__=='__main__':
    main()

