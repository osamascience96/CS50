answer = lambda x: x * 7
print(answer(5))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("Osama", "Ahmed"))

scifi_authors = ["Issac Asimov", "Ray hansal Braduray", "Robert Heinlein", "Frank Herbert", "Douglas Adams", "Osama Ahmed"]

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())

print(scifi_authors)