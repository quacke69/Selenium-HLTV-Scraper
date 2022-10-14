import time
import csv
from selenium import webdriver

# user inputs link to hltv match history page
print("Enter HLTV matches-url:")
url = input()
print("please wait...")

# init webdriver
DRIVER_PATH = '/Users/ludvig/Documents/GitHub/Selenium-HLTV-Scraper/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# open url
driver.get(url)
time.sleep(1.5)

# disable cookies
driver.find_element_by_id("CybotCookiebotDialogBodyButtonDecline").click()
time.sleep(0.5)

# find tables of matches
table = driver.find_element_by_class_name("stats-table")

# create player stat lists
p = [["", [], []], ["", [], []], ["", [], []], ["", [], []], ["", [], []]]
rnds = []

# get every match
rows = table.find_elements_by_tag_name('tr')

for i in range(1, len(rows)):
    cols = rows[i].find_elements_by_tag_name('td')

    # save team name
    team_name = cols[3].find_element_by_tag_name('a').text

    # open match page
    rows[i].find_element_by_class_name(
        "time").find_element_by_tag_name('a').click()

    rw = 0
    rl = 0

    # find score
    if(driver.find_element_by_class_name("team-left").find_element_by_tag_name('a').text == team_name):
        rw = int(driver.find_element_by_class_name(
            "team-left").find_element_by_class_name("bold").text)
        rl = int(driver.find_element_by_class_name(
            "team-right").find_element_by_class_name("bold").text)
    else:
        rw = int(driver.find_element_by_class_name(
            "team-right").find_element_by_class_name("bold").text)
        rl = int(driver.find_element_by_class_name(
            "team-left").find_element_by_class_name("bold").text)

    totr = rw + rl
    rnds.append(rw - rl)

    # find both stat tables
    st = driver.find_elements_by_class_name("totalstats")

    # find stat table that matches team name
    if st[0].find_element_by_class_name("st-teamname").text == team_name:
        stats = st[0]
    else:
        stats = st[1]

    # find all players
    players = stats.find_elements_by_tag_name('tr')

    # if first run, add player names to player stat lists
    if i == 1:
        p[0][0] = players[1].find_element_by_class_name(
            "st-player").find_element_by_tag_name('a').text
        p[1][0] = players[2].find_element_by_class_name(
            "st-player").find_element_by_tag_name('a').text
        p[2][0] = players[3].find_element_by_class_name(
            "st-player").find_element_by_tag_name('a').text
        p[3][0] = players[4].find_element_by_class_name(
            "st-player").find_element_by_tag_name('a').text
        p[4][0] = players[5].find_element_by_class_name(
            "st-player").find_element_by_tag_name('a').text

    # put kpr and dpr into correct arrays
    for m in range(1, len(players)):
        kpr = float(int(players[m].find_element_by_class_name(
            "st-kills").text[0:2]) / totr)
        dpr = float(
            int(players[m].find_element_by_class_name("st-deaths").text) / totr)
        for k in range(0, len(p)):
            if p[k][0] == players[m].find_element_by_class_name("st-player").find_element_by_tag_name('a').text:
                p[k][1].append(kpr)
                p[k][2].append(dpr)

    # go back to match list
    driver.back()

# close driver
driver.close()

f = open('data/output.csv', 'w', newline='')
writer = csv.writer(f)
header = ['match', 'kpr_' + p[0][0], 'dpr_' + p[0][0], 'kpr_' + p[1][0], 'dpr_' + p[1][0], 'kpr_' + p[2][0],
          'dpr_' + p[2][0], 'kpr_' + p[3][0], 'dpr_' + p[3][0], 'kpr_' + p[4][0], 'dpr_' + p[4][0], 'rdiff']
writer.writerow(header)
for i in range(0, len(p[0][1])):
    csvrow = [i+1, p[0][1][i], p[0][2][i], p[1][1][i], p[1][2][i], p[2][1][i],
              p[2][2][i], p[3][1][i], p[3][2][i], p[4][1][i], p[4][2][i], rnds[i]]
    writer.writerow(csvrow)

f.close()
