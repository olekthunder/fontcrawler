import os
import re
import sys
import requests
import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# File with same name as crawlers main file in same dir
LOG_FILE = os.path.abspath(os.path.splitext(__file__)[0])

FONT_FACE_PATTERN = re.compile(r'@font-face\s*{([^}]*)}')

FAMILY_PATTERN = re.compile(r'[\s\S]*font-family:\s*([^;]+);')

STYLE_PATTERN = re.compile(r'[\s\S]*font-style:\s*([^;]+);')

SOURCES_PATTERN = re.compile(r'url\(([^)]+)\)')

FILE_DEBUG_LEVEL = logging.DEBUG

CONSOLE_DEBUG_LEVEL = logging.CRITICAL


# def setup_logging(debug=True):
#     global logger
#     logger = logging.getLogger('fontcrawler_crawler')
#     logger.setLevel(logging.DEBUG)
#     # File handler
#     file_path = '{name}.log'.format(name=LOG_FILE)
#     fh = logging.FileHandler(file_path)
#     fh.setLevel(FILE_DEBUG_LEVEL)
#     # Console handler
#     ch = logging.StreamHandler()
#     ch.setLevel(CONSOLE_DEBUG_LEVEL)
#     # Output format
#     formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(name)s %(message)s')
#     ch.setFormatter(formatter)
#     fh.setFormatter(formatter)
#     logger.addHandler(ch)
#     logger.addHandler(fh)


def fetch_stylesheets(page_url):
    """Send GET request to page, get the response and fetch all link[href]"""
    urls = []
    try:
        response = requests.get(page_url)
    except Exception as e:
        # logger.critical("{url}: {error}".format(url=page_url,
        #                                         error=e))
        sys.exit()
    soup = BeautifulSoup(response.text, 'html.parser')
    external_styles = soup.findAll('link', rel='stylesheet', href=True)
    for style in external_styles:
        style_url = urljoin(page_url, style.get('href'))
        # logger.info("fetched {}".format(style_url))
        urls.append(style_url)
    return urls


def font_faces(style_url):
    resp = requests.get(style_url)
    css = resp.text
    match = FONT_FACE_PATTERN.findall(css)
    yield from match


def get_font_family(font_face):
    match = FAMILY_PATTERN.match(font_face)
    if match:
        return match.group(1)
    return


def get_font_style(font_face):
    match = STYLE_PATTERN.match(font_face)
    if match:
        return match.group(1)
    return


def get_sources(font_face):
    match = SOURCES_PATTERN.findall(font_face)
    if match:
        return match
    return


def fetch_fonts(url):
    result = []
    styles = fetch_stylesheets(url)
    for style in styles:
        for face in font_faces(style):
            sources = [urljoin(url, s.strip('\'\"')) for s in get_sources(face)]
            style = get_font_style(face)
            family = get_font_family(face)
            if family:
                family = family.strip('\'\"')
            result.append({'style':style,
                           'family': family,
                           'sources': sources})
    return result


if __name__ == '__main__':
    urls = ['https://github.com/', 'http://pastebin.com/']
    for url in urls:
        print(fetch_fonts(url))
