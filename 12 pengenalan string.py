data = "ini adalah string"
print(data)
print(type(data))
print('')

# 1. cara membuat string 
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = "string dgn double quote"
print(data)
data = 'string dgn single qoute'
print(data)
print("'halo, apa kabar?'")
print('"halo, apa kabar?"')
print("ini adalah hari jum'at.")
print('')


# 2. menggunakan tanda \
# membuat tanda ' menjadi string
print('mari kita salat jum\'at')
print('it\'s a g\'day, isn\'t it?')

# penggunaan backslash
print("c:\\user\\ucup")

# penggunaan tab
print("ucup\tbudi, berjauhan")

# backspace
print("ucup \bbudi, berdekatan")

# newline
print("baris pertama\nbaris kedua") # LF -> Line Feed (unix, linux, macos)
print("baris pertama\rbaris kedua") # CR -> Carriage Return (commodore, acorn, lisp)
print("baris pertama\r\nbaris kedua") # CRLF -> Line Feed Carriage Return (windows)
print('')


# 3. string literal atau raw
# penggunaan raw string
print(r'c:\user\ucup')
print(r'c:\user\\b"f",\[]\\folder')
print('')

# penggunaan multiline literal string dan raw
print(r"""
nama: iqram
kelas: xii mipa 5 \ smt 1
website: www.iqram.com.id/mantapmania
""")


