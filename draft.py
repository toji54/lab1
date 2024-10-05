def func(text):
    text = text.lower()
    count = 0
    for let in text:
        if let in 'aeiou':
            count += 1
    return count


assert func("Hello") == 2, "Test case 1 failed"