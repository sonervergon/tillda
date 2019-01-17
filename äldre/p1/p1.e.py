## LAB1
# Kopiera det här programmet, du kan markera allt med C-a och kopiera med C-c och lägg det i en fil som du döper till p1.a.py och exekvera programmet med python3 p1.a.py


############################################################
#
# Labb 1
#

# global variables

url = "https://cloud.timeedit.net/kth/web/public01/ri177359X80Z0QQ5Z16g3YZ5yQ086Y75Z0QgQY5Q5027o5p4ll55q1W97.html"
file = 'DD1321.htm'

############################################################
#
# imports and defs
#
import re, getopt, sys, urllib.request


class event:
    def __init__(self):
        self.day= ''
        self.week= ''
        self.date= ''
        self.time = ''
        self.event= []

    def __str__(self):
        s = "{ " + self.week + " " + self.day + " " + self.date + " " + self.time
        if len(self.event) > 3:
            s += " : " + self.event[0] + " " + self.event[1] + " " + self.event[2] + " " + self.event[3]
        s += " }"
        return s

    def __contains__(self, x):
        if x in self.week:
            return True

###########################################################################
##
## parse_url_file
##
## IN
##  The contents of a file which contains a table of the schedule.
## OUT
##  A parsed file which contains an array of tags that contains a key to its object/event. So an array of objects.
def parse_url_file(file_content):
    vek = []

    reg_expr_w = re.compile('.*?td +class.*?weekColumn.*?>(v.*?)</td', re.I)
    reg_expr_d = re.compile('.*?td.*?class.*?changeDateLink.*?headline.*?>([F-T][a-zåäög]) *(.+?)</td')
    reg_expr_t = re.compile('.*?td +id="time.*?>(.+?)</td')
    reg_expr_i = re.compile('.*?td.*?class.*?column[0-1].*?>(.*?)</td', re.I)
    week = ''
    day = ''
    newEntry = False
    qq = event()
    for  j,line in enumerate(file_content):
        newEntry = len(qq.event) > 3 and qq.day != '' and qq.date != '' and qq.week != '' and qq.time != ''
        if newEntry:
            newEntry = True

        m = reg_expr_d.match(line)
        if (m != None) :
            qq.day = m.group(1)
            qq.date = m.group(2)
            day = m.group(2)
            next
        else:
            qq.day = day

        m = reg_expr_t.match(line)
        if (m != None) :
            qq.time = m.group(1)
            next

        m = reg_expr_i.match(line)
        if (m != None) :
            qq.event.append(m.group(1))
            if len(qq.event) < 3:
                 qq.event.append('')
            next


        m = reg_expr_w.match(line)
        if (m != None) :
            qq.week = m.group(1)
            week = m.group(1)
            next
        else:
            qq.week = week

        if newEntry:
            vek.append(qq)
            qq = event()
    return vek


###########################################################################
##
## get file content
##
## IN
##  The name of the file to be imported.
## OUT
##  An array of the file's contents, divided by every line.
def get_file_content(file_name):
    infil = ''
    try:
        infil = open(file_name, 'r')
    except:
        print ("No such file", file_name, " please run with --update")
        print ("	python", sys.argv[0], "--update")
        sys.exit()

    file_content = infil.readlines()
    #file_content = infil.read()
    return file_content

###########################################################################
##
## usage
##
## IN
##  No input.
## OUT
##  Instructions on how to use the program.
def usage():
    print ("Usage example:")
    print ("python" , sys.argv[0] ,  "--update ")
    print ("	updates Time Edit schedule")
    print ("python" , sys.argv[0] ,  '--check "v 49"')
    print ("	checks schedule for week 49")
    print ("python" , sys.argv[0])
    print ("	prints previously downloaded schedule")

###########################################################################
##
## parse_command_line_args
##
## IN
##  No input from program, only user input from terminal.
## OUT
##  Take action after input in command line.
def parse_command_line_args():
    try:
        opts, rest = getopt.getopt(sys.argv[1:], "hc:u", ["help", "check=", "update"])
    except getopt.GetoptError:
        # print help information and exit:
        print ("Unknown option")
        usage()
        sys.exit(2)

    todo = {}
    for option, value in opts:
        if option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ('--check', '-c'):
            todo["check"]=value
        elif option in ('--update', '-u'):
            todo["update"] = value
    return todo

###########################################################################
##
## print_schedule
##
## IN
##  The array of events.
## OUT
##  Prints the events in the terminal.
def print_schedule(data):
    print ("----------- Schedule -------------")
    for item in data:
        print (item)

###########################################################################
##
## search_data
##
## IN
##  What you're searching for and the dataset you're searching in.
## OUT
##  Either you found what you're searching for or no match was found.
def search_data(what, dataset):
    found = False
    for item in dataset:
        if (what in item):
            found = True
            print (item)
    if (found == False):
        print ("Nothing happens", what)

###########################################################################
##
## main
##
## IN
##  No input.
## OUT
##  This runs the whole program.
def main():

    global url, file

    # get command line options
    todo = parse_command_line_args()

    # update time edit file
    if 'update' in todo:
        print ("fetching url ...")
        urllib.request.urlretrieve(url, "DD1321.htm")
        print ("         done")

    # Get schedule from disc
    filedata  = get_file_content(file)
    sched = parse_url_file(filedata)

    # Do something
    if 'check' in todo:
        search_data(todo["check"], sched)
    else:
        print_schedule(sched)


###########################################################################

if __name__ == "__main__":
    main()
