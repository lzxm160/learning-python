import urllib2
from bs4 import BeautifulSoup

def run_main():
    html = urllib2.urlopen("https://www.amazon.cn/gp/bestsellers/books/ref=br_bsl_smr/456-4063020-4086765?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-bestsellers-2&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_t=36701&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_i=desktop")
    bs_obj = BeautifulSoup(html,"lxml")

    nav = bs_obj.find("span", {"class" : "nav-a-content"})
    print nav.get_text()

def run_main1():
    html = urllib2.urlopen("https://www.amazon.cn/gp/bestsellers/books/ref=br_bsl_smr/456-4063020-4086765?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-bestsellers-2&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_t=36701&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_i=desktop")
    bs_obj = BeautifulSoup(html)

    nav_list = bs_obj.findAll("span", {"class" : "nav-a-content"})
    for nav in nav_list:
        print nav.get_text()

if __name__ == '__main__':
    run_main()
    run_main1()

