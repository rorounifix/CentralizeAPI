

def response(status=0, msg="null", data="null"):
    res = {
        "status":status,
        "message":msg,
        "data":data
    }
    return res


if __name__ == "__main__":
    response()
