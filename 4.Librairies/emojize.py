import emoji

def main():
    user = input('Input: ')
    print(emoji.emojize(f'Output: {user}', language='alias'))


main()
