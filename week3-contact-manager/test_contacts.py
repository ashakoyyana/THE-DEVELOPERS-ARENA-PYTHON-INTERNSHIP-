from contacts_manager import validate_phone, validate_email

def test_phone():
    print(validate_phone("9876543210"))
    print(validate_phone("123"))

def test_email():
    print(validate_email("test@gmail.com"))
    print(validate_email("wrongemail"))

test_phone()
test_email()

