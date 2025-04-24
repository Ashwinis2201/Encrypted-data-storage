emails=['a@a.com','b@b.com','c@gmail.com']
print(emails)
for email in emails:
    print(email)
for item in emails:
    if 'b' in item:
        continue
    print(item)