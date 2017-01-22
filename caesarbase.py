import string

# helpers -- support functions for various encryption algorithms

length_of_alphabet  = 26

ORD_lowercase_a = ord(string.ascii_lowercase[0])  # 97
ORD_UPPERCASE_A = ord(string.ascii_uppercase[0])  # 65


def alphabet_position(letter):
    # extra level of paranoia
    if not letter.isalpha():
        return -1

    char_lowercase = letter.lower()
    position = ord(char_lowercase) - ORD_lowercase_a
    return position


def case_sensitive_new_char(old_char, new_pos):
    # extra level of paranoia
    if not old_char.isalpha():
        return ""

    # FIXME: currently assumes ASCII, English alpha characters
    if old_char == old_char.lower():
        return chr(ORD_lowercase_a + new_pos)
    else:
        return chr(ORD_UPPERCASE_A + new_pos)
     

def rotate_character(char, rot):
    if char.isalpha():
        pos = alphabet_position(char)
        # FIXME:  currently assumes ASCII, English alpha characters
        new_pos = (pos + rot) % length_of_alphabet
        return case_sensitive_new_char(char, new_pos) 
    else:
        # for non-alphas, return character as-is
        return char


#    caesar -- Use "Caesar cipher" (right-shift each alpha character
#       by n chars within alphabet) to encrypt message


def encrypt(text, rot):
    msg_encrypted = ""
    for char in text:
        msg_encrypted += rotate_character(char, rot)
    return msg_encrypted


# def user_input_is_valid(cl_args):
#     if len(cl_args) > 1:
#         if cl_args[1].isdigit():
#             return True
# 
#     # no "else", so fallthrough from above can also work
#     return False

#  Usage (in stand-alone mode):
#   $ python3 caesar.py
#   Type a message:
#   Hello, World!
#   Rotate by:
#   5
#   Mjqqt, Btwqi!
