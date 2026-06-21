from agent import SimpleAgent


def main():
    ag = SimpleAgent()
    print("Simple Agent — type 'exit' to quit.")
    while True:
        try:
            q = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye')
            break
        if not q:
            continue
        if q.lower() in ("exit", "quit"):
            print("Goodbye")
            break
        print(ag.handle(q))


if __name__ == '__main__':
    main()
