from datetime import date


def format_date_with_time(obj):
    if (obj != None and obj):
        return obj.strftime("%d/%m/%Y %H:%M")


def format_date(obj):
    if (obj != None and obj):
        return obj.strftime("%d/%m/%Y")


def isValueExistInDb(modelToCheck, filter_to_arg=dict) -> bool:
    """ Checks if a value exists in the database 
    Args:
        modelToCheck: The model to check
        filter_to_arg: a dict with a key and value to check if exist in the DDBB

    Returns:
        A boolean indicating if the value exists in the DDBB
    """

    return modelToCheck.objects.filter(**filter_to_arg).exists()


def isGreaterThanMaximumLength(length=int, toCheck=str) -> bool:
    """Validate the contraint of maximun length of a value
    Args:
        length: a int value of a lengt to compare
        toCheck: a string to evaluate its length

    Returns:
        A boolean indicating if string length is under de maximun

    """


def isLessThanMinimumLength(length=int, toCheck=str) -> bool:
    """Validate the contraint of minimun length of a value

    Args:
        length: a int value of a lengt to compare
        toCheck: a string to evaluate its length

    Returns:
        A boolean indicating if string length is up of the minimum

    """

    return len(toCheck) < length


def isDateFuture(date_to_check=date) -> bool:
    """Validate that a date is not future of today

    Args:
        date_to_check: a date value to compare with the today date

    Returns:
        A boolean indicating if the date is future of today
    """

    return date_to_check > (date.today().strftime("%d/%m/%Y"))


def isDatePast(date_to_check=date) -> bool:
    """Validate that a date is not today or the future

    Args:
        date_to_check: a date value to compare with the today date

    Returns:
        A boolean indicating if the date is future of today"""

    return date_to_check > (date.today().strftime("%d/%m/%Y"))
