from agent import SimpleAgent


def quick_tests():
    ag = SimpleAgent()
    print('Calculator test:', ag.handle('calc: 2 + 3 * 4'))
    print('Calculator test 2:', ag.handle('7*6-5'))
    print('Weather test (example):', ag.handle('weather: London'))
    print('Word count test:', ag.handle('wordcount: hello world python agent'))
    print('Character count test:', ag.handle('charcount: agent'))
    print('Reverse text test:', ag.handle('reverse: hello'))
    print('JSON validate test:', ag.handle('validate: {"name": "agent", "version": 1}'))
    print('JSON format test:', ag.handle('format: {"a":1,"b":2}'))
    print('JSON minify test:', ag.handle('minify: { "name" : "agent" }'))


if __name__ == '__main__':
    quick_tests()
