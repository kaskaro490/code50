import emoji

def main():
    user = input('Input: ', language='alias')
    print(emoji.emojize(f'Output: {user}'))


main()
