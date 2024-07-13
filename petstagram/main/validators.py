from django.core.exceptions import ValidationError


# def always_valid(chars):
#     def validator(value):
#         pass
#     return validator


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            # Invalid case
            raise ValidationError('Value must contain only letters')
    # valid case
    # if not all(ch.isalpha() for ch in value):
    #     raise ValidationError('Value must contain only letters')


def validate_file_max_size(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(max_size))

    return validate
