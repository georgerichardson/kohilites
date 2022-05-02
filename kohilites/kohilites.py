from mdutils.mdutils import MdUtils
from slpp import slpp as lua


class MetaData:
    def __init__(self, path):
        self.path = path


    def decode_data(self):
        """ Converts a lua table to a Python dict
        :type path: str|unicode
        :param path: The path to the lua file
        """
        with open(self.path, "r", encoding="utf8", newline=None) as txt_file:
            txt = txt_file.read()[39:]  # offset the first words of the file
            data = lua.decode(txt.replace("--", "—"))
            if type(data) == dict:
                return data

    def extract_highlights(self, data):
        for highlighted in data['highlight'].values():
            for highlight in highlighted.values():
                yield(highlight)

    def extract_doc_props(self, data):
        title = data['doc_props']['title']
        authors = data['doc_props']['authors']
        authors = authors.replace('\\\n', ', ')
        return {'authors': authors,
                'title': title
                }

    def highlights(self):
        data = self.decode_data()
        doc_props = self.extract_doc_props(data)
        highlights = self.extract_highlights(data)

        md = MdUtils(file_name=doc_props['title'])
        md.write(doc_props['title'], bold_italics_code='b')
        md.new_paragraph(doc_props['authors'], bold_italics_code='i')

        for highlight in highlights:
            md.new_paragraph(f"{highlight['text']}, _{highlight['chapter']}_")

        md.create_md_file()
        self.md = md


