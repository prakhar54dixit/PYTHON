import requests

def free_api_username():
    url="https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response=requests.get(url)
    info=response.json()

    status_code=info["statusCode"]
    current_page_items=info['data']["currentPageItems"]

    return status_code,current_page_items


def main():
    info1,info2=free_api_username()
    print(info1,info2)

if __name__=='__main__':
    main()

