"""Helper to get Travis/Codecov badges in markdown table."""


class Markdown:
    def _link(what, link):
        return f'[{what}]({link})'
    
    def _img(img_url, alt=''):
        return f'![{alt}]({img_url})'
    
    def linked_image(img_url, link_url):
        img_str = Markdown._img(img_url)
        return Markdown._link(what=img_str, link=link_url)        

class App:
    def badge(self):
        return Markdown.linked_image(self.svg, self.link)


class Travis(App):  
    def __init__(self, repo_name):
        self.link = f'https://travis-ci.org/{repo_name}'
        self.svg = f'{self.link}.svg?branch=master'

assert Travis('mini-kep/parser-rosstat-kep').badge() == ("[![]"
    "(https://travis-ci.org/mini-kep/parser-rosstat-kep.svg?branch=master)]"
    "(https://travis-ci.org/mini-kep/parser-rosstat-kep)")

           
class Codecov(App):    
    def __init__(self, repo_name):
        self.link = f'https://codecov.io/gh/{repo_name}'
        self.svg = f'{self.link}/branch/master/graphs/badge.svg'

        
class Repo:    
    def __init__(self, repo_name):
        self.name = repo_name
        self.name_in_org = f'mini-kep/{repo_name}' 
        self.url = f'https://github.com/mini-kep/{self.name}'
    
    def badge_codecov(self):
        return Codecov(self.name_in_org).badge()
    
    def badge_travis(self):
        return Travis(self.name_in_org).badge()

    def link(self):
        return Markdown._link(self.name, self.url)


def to_markdown(table):
    """Translate *table* list of strings to markdown. 
       Use first row in *table* as header.       
    """    
    header = table[0]
    horiz = ["-" * len(x) for x in header]
    body = table[1:]
    table = [header, horiz]
    table.extend(body)
    
    def add_dividers(row):
        inner_part = " | ".join(row) 
        return f"| {inner_part} |"
    
    table = [add_dividers(row) for row in table]    
    return '\n'.join(table)

def row_with_badges(repo_name):
    repo = Repo(repo_name)
    return [repo.link(), 
            repo.badge_travis(), 
            repo.badge_codecov()] 
           
def row_with_link(repo_name):
    repo = Repo(repo_name)
    return [repo.link(), '', '']
   

if __name__ == "__main__":
    repo_names = ['parser-rosstat-kep', 
                  'parsers',
                  'db',
                  'frontend-app',
                  'full-app']
    table = [['Repo', 'Tests', 'Coverage']]
    table.extend([row_with_badges('parser-rosstat-kep')])
    table.extend([row_with_badges('parsers')])
    table.extend([row_with_link('db')])
    table.extend([row_with_badges('frontend-app')])
    table.extend([row_with_badges('full-app')])
    md_table = to_markdown(table)
    print(md_table)
