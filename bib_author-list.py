import pybtex.database
import sys
import webbrowser


def get_authors(bib_data):
    authors = []
    for entry in bib_data.entries:
        try:
            for person in bib_data.entries[entry].persons["author"]:
                authors.append(str(person))
        except KeyError as err:
            pass
    return authors


def open_linkedin_researchgate(author):
    rg_baseurl = 'https://www.researchgate.net/search.Search.html?type=researcher&query='
    linkeding_baseurl = "https://www.linkedin.com/search/results/people/?keywords="
    webbrowser.open(rg_baseurl+author)
    webbrowser.open(linkeding_baseurl+author)
    return


def main(bib_filename):
    bib_data = pybtex.database.parse_file(bib_filename)
    authors = get_authors(bib_data)
    for author in authors:
        open_linkedin_researchgate(author)
        breakpoint()    #arrivé à "Hixson, W. C."
    return


if __name__ == "__main__":
    main(sys.argv[1])
