from Validation import Validation

def test_validate_firstname_true():
    """
        Description: 
            In this test case when given a valid first name and iterate through
            list of names should return true.
    """ 
    names = ["Fatha","Sam"]
    for valid_name in names:
        assert Validation.validate_name(valid_name) == True

def test_invalid_firstname_flase():
    """
        Description: 
            In this test case when given a invalid first name and iterate through
            list of names should return false.
    """ 
    names = ["Fa","fatha",""]
    for invalid_name in names:
        assert Validation.validate_name(invalid_name) == False

def test_validate_lastname_true():
    """
        Description: 
            In this test case when given a valid last name and and iterate through
            list of names should return true.
    """ 
    names = ["Smith","Joe"]
    for valid_name in names:
        assert Validation.validate_name(valid_name) == True

def test_invalid_lasttname_flase():
    """
        Description: 
            In this test case when given a valid last name and and iterate through
            list of names should return false.
    """ 
    names = ["Ja","$mith",""]
    for invalid_name in names:
        assert Validation.validate_name(invalid_name) == False

def test_email_id_true():
    """
        Description: 
            In this test case when given a email to iterate through the list of emails
            should return true.
    """ 
    emails = ["mfjkd7795@gmail.com", "abc.xyz@bl.co.in"] 
    for email in emails:
        assert Validation.validate_email(email) == True

def test_email_id_false():
    """
        Description: 
            In this test case when given a email to iterate through the list of emails
            should return false.
    """
    emails = ["mfjkd7795gmail.com", "","FathaJkd"] 
    for email in emails:
        assert Validation.validate_email(email) == False

def test_password_true():
    """
        Description: 
            In this test case when given a password rules and itrate throug the
            list of passwords should return true.
    """
    passwords = ["Fathajkd12@", "mohammadFatha98$"]
    for passwd in passwords:
        assert Validation.validate_passwaord(passwd) == True

def test_password_false():
    """
        Description: 
            In this test case when given a password rules and itrate throug the
            list of passwords should return true.
    """
    passwords = ["Fathajkd12", "mohammadfatha98"]
    for passwd in passwords:
        assert Validation.validate_passwaord(passwd) == False

def test_phonenumber_true():
    """
        Description: 
            In this test case when given a phone number and iterate throgh 
            list of phone numbers should return true.
    """
    numbers = ["91 8217485224", "91 9073623476"]
    for number in numbers:
        assert Validation.validate_phone_number(number) == True

def test_phonenumber_false():
    """
        Description: 
            In this test case when given a phone number and iterate throgh 
            list of phone numbers should return false.
    """
    numbers = ["918217485224", "9073623476", ""]
    for number in numbers:
        assert Validation.validate_phone_number(number) == False
