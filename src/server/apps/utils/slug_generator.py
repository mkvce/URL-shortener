import random
import string


def generate_slug():
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    slug = "".join([random.choice(letters) for _ in range(8)])
    return slug
