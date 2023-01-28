def to_camel_case(text):
    if text == "":
        return ""
    text = text.replace("-", "_")
    text = text.split("_")
    for i in range(1, len(text)):
        text[i] = text[i].capitalize()
    if text[0].isupper():
        text[0] = text[0].capitalize()
    return "".join(text)

print(to_camel_case(""))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))