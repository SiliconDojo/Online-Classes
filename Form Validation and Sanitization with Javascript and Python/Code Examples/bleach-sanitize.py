import bleach

def sanitize_with_bleach(input_string):
    return bleach.clean(input_string, tags=[], attributes={}, strip=True)

unsafe_string = '<a href="http://example.com">Click Here</a><script>alert("XSS")</script>'
safe_string = sanitize_with_bleach(unsafe_string)
print()
print(unsafe_string)
print()
print(safe_string)
