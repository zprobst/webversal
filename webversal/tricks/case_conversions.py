import re

def camel_to_snake_case(subject, lower=True):
    subject = re.sub(r'(?<!^)(?=[A-Z])', '_', subject)
    return subject.lower() if lower else subject.upper()
