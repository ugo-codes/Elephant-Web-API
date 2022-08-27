import requests


def get_by_name(name: str) -> list:
    """
    This method calls the elephant api responsible for searching a list of elephants by their name
    :param name: (str) the name of the elephant
    :return: (list) a list of elephant with that name
    """

    # make a get request to the elephant api
    response = requests.get(url=f"https://elephant-api.herokuapp.com/elephants/name/{name.lower()}")
    # if there is an error raise it
    response.raise_for_status()
    try:
        # return a list of the result if everything goes well
        return [response.json()]
    except:
        # return an empty list if there is any error
        return []


def get_by_sex(sex: str) -> list:
    """
    This method calls the elephant api responsible for searching a list of elephants by their sex
    :param sex: (str) the sex of the elephant
    :return: (list) a list of elephant with that sex
    """

    # make a get request to the elephant api
    response = requests.get(url=f"https://elephant-api.herokuapp.com/elephants/sex/{sex.lower()}")
    # if there is an error raise it
    response.raise_for_status()
    try:
        # return a list of the result if everything goes well
        return response.json()
    except:
        # return an empty list if there is any error
        return []
