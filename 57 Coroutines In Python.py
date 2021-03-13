def searcher():
    import time
    # Some 5 sec time consuming code executed
    book = 'Sherry This is a book in which there are lots of stuff'
    time.sleep(5)

    while True:
        text = (yield)
        if text in book:
            print('Your Text is in book')
        else:
            print('I cannot found your text')


#  this is not a function this Coroutines
search = searcher()
next(search)
search.send('Sherry')
input('Press any key')
search.send('Me')
search.close()


# ---------------- Challenge -------------- #
letters = ['Sherry', 'Hamza', 'Asad', 'Furqan', 'Zulqarnain', 'Salman', 'Rafi', 'Ibrar', 'Babar', 'Sagar', 'Uzair']


def challenge():
    print('Started From here')

    while True:
        text = (yield)
        if text in letters:
            print(f'Your name is in letters list on {letters.index(text)} index')
        else:
            print('Name not found')


task = challenge()
next(task)
user = input('Enter Name: ')
task.send(user)
