try:
    f = open('resource/demo.txt', 'r', encoding='utf8')
except FileNotFoundError:
    f = open('resource/demo.txt', 'w', encoding='utf8')
    f.write('hello\nworld')
else:
    print(f.read())
finally:
    f.close()
