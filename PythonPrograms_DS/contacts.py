contacts= {
    "number":4,
    "students":
    [
        {"name": "test1","emailId":"test1@example.com"},
        {"name": "test2","emailId":"test2@example.com"},
        {"name": "test3","emailId":"test3@example.com"},
        {"name": "test4","emailId":"test4@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["emailId"])