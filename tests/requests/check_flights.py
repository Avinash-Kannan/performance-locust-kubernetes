def check_flight_request(testdata):
    cities = testdata.pop()
    data = {
        "fromPort": cities["departure"],
        "toPort": cities["destination"]
    }
    testdata.insert(0,cities)
    return data