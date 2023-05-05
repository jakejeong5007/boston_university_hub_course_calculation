from bs4 import BeautifulSoup
import requests


def update_all_classes(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    cont = doc.select("div.cf-course-card")

    with open('course.txt', 'a') as f:
        for j in cont:
            hub = ""
            course_num = j.select_one("span.cf-course-id").text
            course_title = j.select_one("h3.bu_collapsible").text
            course_hub = j.select_one("ul.cf-hub-offerings")
            try:
                course_pre = j.select_one("span.cf-course-prereqs").text
            except:
                course_pre = None
            school = course_num.split()
            if school[0] == "CAS":
                for i in course_hub:
                    hub += ('@ ' + str(i.text))
                if course_pre != "":
                    line = course_num + '@' + course_title + hub + course_pre + '\n'
                    f.write(line)
                else:
                    line = course_num+'@' + course_title + hub + '\n'
                    f.write(line)


url1 = "https://www.bu.edu/hub/hub-courses/philosophical-aesthetic-and-historical-interpretation/"
url2 = "https://www.bu.edu/hub/hub-courses/diversity-civic-engagement-and-global-citizenship/"
url3 = "https://www.bu.edu/hub/hub-courses/scientific-and-social-inquiry/"
url4 = "https://www.bu.edu/hub/hub-courses/quantitative-reasoning/"
url5 = "https://www.bu.edu/hub/hub-courses/diversity-civic-engagement-and-global-citizenship/"
url6 = "https://www.bu.edu/hub/hub-courses/communication/"
url7 = "https://www.bu.edu/hub/hub-courses/intellectual-toolkit/"


update_all_classes(url1)
update_all_classes(url2)
update_all_classes(url3)
update_all_classes(url4)
update_all_classes(url5)
update_all_classes(url6)
update_all_classes(url7)
