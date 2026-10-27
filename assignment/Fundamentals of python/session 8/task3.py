def reverse_message(message):
    result = ""

    for char in message:
        result = char + result

    return result


print(reverse_message("Hello WhatsApp"))