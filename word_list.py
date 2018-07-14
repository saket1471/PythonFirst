from urllib.request import urlopen


def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            # line_words = line.split()    # print bytes like -> b'test'
            line_words = line.decode('utf-8').split()  # test
            for word in line_words:
                story_words.append(word)

    print(story_words)

# fetch_words()  # if we use function as is, when used with import it gets executes once, when module is loaded first


if __name__ == '__main__':
    fetch_words()

