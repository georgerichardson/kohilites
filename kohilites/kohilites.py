from datetime import datetime
from mdutils.mdutils import MdUtils
import os
from slpp import slpp as lua

from .utils import make_path_if_not_exist


class MetaData:
    def __init__(self, input, output=None):
        self.input = input
        self.output = output

    def decode_data(self):
        
        with open(self.input, "r", encoding="utf8", newline=None) as txt_file:
            txt = txt_file.read()[39:]  # offset the first words of the file
            data = lua.decode(txt.replace("--", "—"))
            if type(data) == dict:
                return data

    def parse_date(self, date):
        return datetime.strptime(date, "%Y-%m-%d %H:%M:%S")


    def extract_highlights(self, data):
        highlights = []
        for highlighted in data["highlight"].values():
            for highlight in highlighted.values():
                highlights.append(
                    (
                        self.parse_date(highlight['datetime']),
                        highlight,
                    )
                )
        highlights.sort(key=lambda x: x[0])
        
        for highlight in highlights:
                yield(highlight[1])

    def extract_doc_props(self, data):
        title = data["doc_props"]["title"]
        authors = data["doc_props"]["authors"]
        authors = authors.replace("\\\n", ", ")
        return {"authors": authors,
                "title": title
                }

    def highlights(self):
        data = self.decode_data()
        doc_props = self.extract_doc_props(data)
        highlights = self.extract_highlights(data)

        if self.output is None:
            if os.path.isdir(self.input):
                fout = self.input
            elif os.path.isfile(self.input):
                fout = "/".join(self.input.split("/")[:-1])
        else:
            fout = self.output

        make_path_if_not_exist(fout)

        md = MdUtils(file_name=f"{fout}/{doc_props['title']}")
        md.write(f"**{doc_props['title']}**, _{doc_props['authors']}_")

        for highlight in highlights:
            md.new_paragraph(f"{highlight['text']}, _{highlight['chapter']}_")

        md.create_md_file()
        self.md = md


