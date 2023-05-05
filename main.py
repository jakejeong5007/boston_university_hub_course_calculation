from collections import defaultdict
import pprint

def main(req):
    my_file = "my_course.txt"
    all_file = "course.txt"
    con = True
    cls = read_file(my_file, all_file)
    update(req, cls)
    while con:
        next_act = int(input("\nInput action:\n"
                             "0. Exit\n"
                             "1. Check Status\n"
                             "2. Add my class\n"
                             "3. Add class to database\n"
                             "4. Delete Class\n"
                             "5. Update Hub\n"
                             "6. All Status\n"))
        if next_act == 0:
            con = False
        elif next_act == 1:
            check_status(req)
        elif next_act == 2:
            add_my_class(my_file, all_file)
            cls = read_file(my_file, all_file)
            update(req, cls)
        elif next_act == 3:
            add_class(all_file)
        elif next_act == 4:
            pass
        elif next_act == 5:
            update_hub(req)
        elif next_act == 6:
            all_status()

def update_hub(req):
    up = input("What hub requirement will you update?\n")
    if up in req:
        req[up] = True
        print("Successfully updated")
    elif up == "Writing, Research, and Inquiry" or "Writing-Intensive Course":
        req['Writing, Research, and Inquiry/Writing-Intensive Course'] = True
    else:
        print("No such hub requirement")


def add_class(file):
    add = input("What class do you want to add? Format:\n"
                "Class name, Hub Requirements, Prerequisites\n")
    ecls = add.split('@ ')
    with open(file, 'r') as f:
        cont = f.readlines()
    for line in cont:
        if ecls[0] in line:
            print("\nThe class is already in the list")
            return
    add += "\n"
    with open(file, 'a') as f:
        f.write(add)


def add_my_class(my_file, all_file):
    add = input("What class do you want to add?:\n").upper()
    with open(all_file, 'r') as f:
        cont = f.readlines()

    with open(my_file, 'a') as mf:
        for line in cont:
            lst = line.split('@ ')
            if lst[0] == add:
                add += "\n"
                mf.write(add)


def check_status(req):
    not_done = []
    for key in req.keys():
        if not req[key]:
            not_done.append(key)
    print("Following hub requirements are not completed:")
    for ncls in not_done:
        print(ncls)


def update(req, cls):
    for key in cls.keys():
        for hub in cls[key]["Hub"]:
            h = cls[key]["Hub"][hub]
            if h == "Philosophical Inquiry and Life’s Meanings":
                req["Philosophical Inquiry and Life’s Meanings"] = True

            elif h == "Aesthetic Exploration":
                req["Aesthetic Exploration"] = True

            elif h == "Historical Consciousness":
                req["Historical Consciousness"] = True

            elif h == "Scientific Inquiry I" or h == "Scientific Inquiry II":
                req["Scientific Inquiry"] = True

            elif h == "Social Inquiry II" or h == "Social Inquiry I":
                req["Social Inquiry"] = True

            elif h == "Quantitative Reasoning II":
                req["Quantitative Reasoning"] = True

            elif h == "The Individual in Community":
                req["The Individual in Community"] = True

            elif h == "Global Citizenship and Intercultural Literacy":
                req["Global Citizenship and Intercultural Literacy"] = True

            elif h == "Ethical Reasoning":
                req["Ethical Reasoning"] = True

            elif h == "Writing, Research, and Inquiry" or h == "Writing-Intensive Course":
                req["Writing, Research, and Inquiry/Writing-Intensive Course"] = True

            elif h == "Critical Thinking":
                req["Critical Thinking"] = True

            elif h == "Research and Information Literacy":
                req["Research and Information Literacy"] = True

            elif h == "Teamwork/Collaboration":
                req["Teamwork/Collaboration"] = True

            elif h == "Creativity/Innovation":
                req["Creativity/Innovation"] = True

    return req


def read_file(my_file, all_file):
    classes = {}
    classes = multi_dict(3, str)
    clst = []
    with open(my_file, 'r') as mf:
        mcont = mf.readlines()

    with open(all_file, 'r') as af:
        acont = af.readlines()

    for mline in mcont:
        for aline in acont:
            clst = aline.split("@ ")
            if clst[0] in mline:
                hcount = 0
                for i in range(len(clst) - 1):
                    if i > 1:
                        classes[clst[0]]["Hub"][hcount] = clst[i]
                        hcount += 1
                classes[clst[0]]["Prerequisite"] = clst[-1]

    return classes

def read_all_file(all_file):
    classes = {}
    classes = multi_dict(3, str)
    clst = []
    with open(all_file, 'r') as af:
        acont = af.readlines()
        for aline in acont:
            clst = aline.split("@ ")
            hcount = 0
            for i in range(len(clst) - 1):
                if i > 1:
                    classes[clst[0]]["Hub"][hcount] = clst[i]
                    hcount += 1
            classes[clst[0]]["Prerequisite"] = clst[-1]
    return classes


def multi_dict(K, atype):
    if K == 1:
        return defaultdict(atype)
    else:
        return defaultdict(lambda: multi_dict(K-1, atype))


def all_status():
    pprint.pprint(req)


if __name__ == '__main__':
    req = {
        'Philosophical Inquiry and Life’s Meanings': False,
        'Aesthetic Exploration': False,
        'Historical Consciousness': False,
        'Scientific Inquiry': False,
        'Social Inquiry': False,
        'Quantitative Reasoning': False,
        'The Individual in Community': False,
        'Global Citizenship and Intercultural Literacy': False,
        'Ethical Reasoning': False,
        'Writing, Research, and Inquiry/Writing-Intensive Course': False,
        'Critical Thinking': False,
        'Research and Information Literacy': False,
        'Teamwork/Collaboration': False,
        'Creativity/Innovation': False
    }

    main(req)
