def tag(tag_name):
    def add_tag(content):
        return "<{0}>{1}</{0}>".format(tag_name, content)
    return add_tag


content = 'Hello'
add_tag = tag('h1')
print(add_tag(content))  # <h1>Hello</h1>
