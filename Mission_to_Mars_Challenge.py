{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "respective-alcohol",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoup\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "invisible-raleigh",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 92.0.4515\n",
      "Get LATEST driver version for 92.0.4515\n",
      "Get LATEST driver version for 92.0.4515\n",
      "Trying to download new driver from https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_mac64.zip\n",
      "Driver has been saved in cache [/Users/arnieacevedo/.wdm/drivers/chromedriver/mac64/92.0.4515.107]\n"
     ]
    }
   ],
   "source": [
    "# Setting browser path\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "outdoor-luther",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://redplanetscience.com'\n",
    "browser.visit(url)\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "hidden-granny",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setting up HTML Parser\n",
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('div.list_text')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "fifty-active",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\">Alabama High School Student Names NASA's Mars Helicopter</div>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "slide_elem.find('div', class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "arbitrary-longer",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Alabama High School Student Names NASA's Mars Helicopter\""
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the first `a` tag and save it as `news_title`\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "included-wireless",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Vaneeza Rupani's essay was chosen as the name for the small spacecraft, which will mark NASA's first attempt at powered flight on another planet.\""
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "previous-description",
   "metadata": {},
   "source": [
    "### Featured Images Scrubbing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "swiss-syndicate",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "grave-relative",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "intelligent-seeking",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "selective-metro",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "incomplete-shipping",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://spaceimages-mars.com/image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base URL to create an absolute URL\n",
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "virgin-collaboration",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>description</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 ?? 10^23 kg</td>\n",
       "      <td>5.97 ?? 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 ??C</td>\n",
       "      <td>-88 to 58??C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Mars            Earth\n",
       "description                                              \n",
       "Mars - Earth Comparison             Mars            Earth\n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 ?? 10^23 kg  5.97 ?? 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 ??C      -88 to 58??C"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Added Pandas for .read_html() function\n",
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "df.columns=['description', 'Mars', 'Earth']\n",
    "df.set_index('description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "attempted-instrument",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>description</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Mars - Earth Comparison</th>\\n      <td>Mars</td>\\n      <td>Earth</td>\\n    </tr>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 ?? 10^23 kg</td>\\n      <td>5.97 ?? 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 ??C</td>\\n      <td>-88 to 58??C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.to_html()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "organic-matter",
   "metadata": {},
   "source": [
    "# D1: Scrape High-Resolution Mars??? Hemisphere Images and Titles"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "former-court",
   "metadata": {},
   "source": [
    "### Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "prostate-matthew",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<div class=\"item\">\n",
       " <a class=\"itemLink product-item\" href=\"cerberus.html\"><img alt=\"Cerberus Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png\"/></a>\n",
       " <div class=\"description\">\n",
       " <a class=\"itemLink product-item\" href=\"cerberus.html\">\n",
       " <h3>Cerberus Hemisphere Enhanced</h3>\n",
       " </a>\n",
       " <span class=\"subtitle\" style=\"float:left\">image/tiff 21 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/>\n",
       " <p>Mosaic of the Cerberus hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of 104 Viking Orbiter images acquired???</p>\n",
       " </div>\n",
       " <!-- end description -->\n",
       " </div>,\n",
       " <div class=\"item\">\n",
       " <a class=\"itemLink product-item\" href=\"schiaparelli.html\"><img alt=\"Schiaparelli Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png\"/></a>\n",
       " <div class=\"description\">\n",
       " <a class=\"itemLink product-item\" href=\"schiaparelli.html\">\n",
       " <h3>Schiaparelli Hemisphere Enhanced</h3>\n",
       " </a>\n",
       " <span class=\"subtitle\" style=\"float:left\">image/tiff 35 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/>\n",
       " <p>Mosaic of the Schiaparelli hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The images were acquired in 1980 during early northern???</p>\n",
       " </div>\n",
       " <!-- end description -->\n",
       " </div>,\n",
       " <div class=\"item\">\n",
       " <a class=\"itemLink product-item\" href=\"syrtis.html\"><img alt=\"Syrtis Major Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png\"/></a>\n",
       " <div class=\"description\">\n",
       " <a class=\"itemLink product-item\" href=\"syrtis.html\">\n",
       " <h3>Syrtis Major Hemisphere Enhanced</h3>\n",
       " </a>\n",
       " <span class=\"subtitle\" style=\"float:left\">image/tiff 25 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/>\n",
       " <p>Mosaic of the Syrtis Major hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of about 100 red and violet???</p>\n",
       " </div>\n",
       " <!-- end description -->\n",
       " </div>,\n",
       " <div class=\"item\">\n",
       " <a class=\"itemLink product-item\" href=\"valles.html\"><img alt=\"Valles Marineris Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png\"/></a>\n",
       " <div class=\"description\">\n",
       " <a class=\"itemLink product-item\" href=\"valles.html\">\n",
       " <h3>Valles Marineris Hemisphere Enhanced</h3>\n",
       " </a>\n",
       " <span class=\"subtitle\" style=\"float:left\">image/tiff 27 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/>\n",
       " <p>Mosaic of the Valles Marineris hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The distance is 2500 kilometers from the surface of???</p>\n",
       " </div>\n",
       " <!-- end description -->\n",
       " </div>]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 1. Use browser to visit the URL \n",
    "main_url = 'https://marshemispheres.com/'\n",
    "\n",
    "browser.visit(main_url)\n",
    "\n",
    "html = browser.html\n",
    "mars_main = soup(html, \"html.parser\")\n",
    "\n",
    "# Once this cell is run comment out or it will throw an error \n",
    "# when troubleshooting\n",
    "results = mars_main.find_all(\"div\", class_=\"item\")\n",
    "results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "compressed-organization",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemisphere_image_urls = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "hybrid-appearance",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "urls = [(a.text, a['href']) for a in browser\n",
    "         .find_by_css('div[class=\"description\"] a')]\n",
    "for title,url in urls:\n",
    "    mars_image_dict = {}\n",
    "    browser.visit(url)\n",
    "    img_url = browser.find_by_css('img[class=\"wide-image\"]')['src']\n",
    "    mars_image_dict['img_url'] = img_url\n",
    "    mars_image_dict['title'] = title\n",
    "    hemisphere_image_urls.append(mars_image_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "mathematical-fortune",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': 'https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4. Print the list that holds the dictionary of each image url and title.\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "minor-unemployment",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Quit the browser\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "defensive-function",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
