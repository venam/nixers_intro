import random


def randomList(a):
    b = []
    for i in range(len(a)):
        element = random.choice(a)
        a.remove(element)
        b.append(element)
    return b


def parse_file(location):
    f = open("intro_thread.dump")
    content = randomList(f.readlines())

    for line in content:
        divide = line.split("\t")
        tid = divide[0]
        username = divide[1]
        title = divide[2]
        content = divide[3].replace("\\n","<br/>")
        created_content = create_content(tid,username,title, content)
        open(location,'a').write(created_content)


def create_content(tid, username, title, content):
    return ('<div class="header">\n'+
        username + '\n' +
        '</div>\n'+
        '<p>\n'+
        title + '<a href="http://nixers.net/showthread.php?tid='+ tid +'">Thread</a>\n'+
        '</p>\n'+
        '<div class="code">\n'+
        '<p>\n'+
        content + '\n' +
        '</p>\n'+
        '</div>\n'+
        '<hr>\n')


parse_file("test.html")


