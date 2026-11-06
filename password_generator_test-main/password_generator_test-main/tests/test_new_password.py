import string
from password.new_password import generate_password

def test_password_characters():
    """Tes untuk memastikan hanya karakter yang diizinkan yang digunakan dalam pembuatan password"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Membuat password yang panjang untuk pengujian yang lebih akurat
    for char in password:
        assert char in valid_characters

def test_password_length_panjang():
    """tes untuk memastikan panjang password sesuai dengan yang diminta"""
    password = generate_password(23)
    assert len(password) == 23

def test_beda_passwords():
    """tes untuk memastikan dua password yang dibuat berurutan tidak sama"""
    password1 = generate_password(23)
    password2 = generate_password(23)
    assert password1 != password2
