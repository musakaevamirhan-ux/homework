def count_words(text):
    words = text.split()
    return len(words)
def count_numbers(text):
    numbers = text.split()
    cnt = 0
    for i in numbers:
        i = i.strip(".,/!")
        if i.isdigit():
            cnt += 1
    return cnt
def repeat_words(text):
    words = text.split()
    repeat_words = []
    for i in words:
        if words.count(i) > 1 and i not in repeat_words:
            repeat_words.append(i)
    print(*repeat_words)