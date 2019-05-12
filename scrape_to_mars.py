
#%%
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd


#%%
def init_browser():
    #executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", #executable_path,
     headless=False)


#%%
def collect_info():
    browser = init_browser()

#%%
    # url 1:
    url1="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url1)
    html1=browser.html
    soup1=bs(html1,'lxml')
    # NASA Mars News
    n_title=soup1.find("div", class_="content_title").text
    n_para=soup1.find("div",class_="article_teaser_body").text  

    url1_b="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url1_b)
    html1_b=browser.html
    soup1_b=bs(html1_b,'lxml')
    # JPL Mars Space Images-Featured Image
    src1_b=soup1_b.find("a", class_="fancybox")['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov' + src1_b



#%% [markdown]
    # url 2: Mars Weather
    url2="https://twitter.com/marswxreport?lang=en"
    browser.visit(url2)
    html2=browser.html
    soup2=bs(html2,'lxml')
    mars_weather1=soup2.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_weather=mars_weather1[8:-30]

#%% 
    # url 3: Mars Facts
    url3="https://space-facts.com/mars/"
    table=pd.read_html(url3)
    df=table[0]
    #type(df)
    d = pd.DataFrame()
    d['Type'] = df[0]
    d['Value'] = df[1]
    d = d.set_index('Type')
    html_table=d.to_html()
    html_table

#%% 
    # url 4: Mars hemispheres
    def title(url):
        browser.visit(url)
        html=browser.html
        soup=bs(html,'lxml')
        src_=soup.find("img", class_="wide-image")['src']
        img_url = 'https://astrogeology.usgs.gov' + src_
        title=soup.find("h2", class_="title").text
        return title, img_url

    url4a="https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    url4b="https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    url4c="https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    url4d="https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"

    hemi_urls=[]
    title4a,img_url4a=title(url4a)
    hemi_urls.append({ "title":title4a, "img_url":img_url4a})
    title4b,img_url4b=title(url4b)
    hemi_urls.append({ "title":title4b, "img_url":img_url4b})
    title4c,img_url4c=title(url4c)
    hemi_urls.append({ "title":title4c, "img_url":img_url4c})
    title4d,img_url4d=title(url4d)
    hemi_urls.append({ "title":title4d, "img_url":img_url4d})

    hemi_urls


    #collect the scrapes
    scrape_mars={ 
        "title":n_title,
        "para":n_para,
        "n_link":featured_image_url,
        "mars_weather":mars_weather,
        "mars_fact":html_table,
       "mars_hemi": hemi_urls
    }
    return scrape_mars