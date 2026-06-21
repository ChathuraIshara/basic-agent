from agent import SimpleAgent


def quick_tests():
    ag = SimpleAgent()
    print('Calculator test:', ag.handle('calc: 2 + 3 * 4'))
    print('Calculator test 2:', ag.handle('7*6-5'))
    print('Weather test (example):', ag.handle('weather: London'))
    print('Word count test:', ag.handle('wordcount: hello world python agent'))
    print('Character count test:', ag.handle('charcount: agent'))
    print('Reverse text test:', ag.handle('reverse: hello'))
    print('URL encode test:', ag.handle('encode: hello world'))
    print('URL decode test:', ag.handle('decode: hello%20world'))
    print('URL info test:', ag.handle('info: https://github.com/user/repo?id=123'))


if __name__ == '__main__':
    quick_tests()
