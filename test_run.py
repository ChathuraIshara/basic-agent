from agent import SimpleAgent


def quick_tests():
    ag = SimpleAgent()
    print('Calculator test:', ag.handle('calc: 2 + 3 * 4'))
    print('Calculator test 2:', ag.handle('7*6-5'))
    print('Weather test (example):', ag.handle('weather: London'))


if __name__ == '__main__':
    quick_tests()
