from dataclasses import dataclass, field
from typing import List, Dict, Callable

from reportlab.platypus import Frame
from reportlab.pdfgen.canvas import Canvas
# from reportlab.lib.pagesizes import A4



@dataclass
class PageFrame:
    fr: Frame
    elements: List[Callable] = field(default_factory=list)

@dataclass
class SimplePage:
    page_frames: List[PageFrame] = field(default_factory=list)

    def add_frame(self, spf: PageFrame) -> None:
        self.page_frames.append(spf)

    def plot(self, canv_data) -> None:
        canv = get_canvas(canv_data)

        for spf in self.page_frames:
            spf.fr.addFromList(spf.elements, canv)

        canv.save()
        
def get_canvas(d):
    c = Canvas(d.filename, d.pagesize)
    c.setTitle(d.title)
    c.setAuthor(d.author)
    c.setCreator(d.creator)
    c.setSubject(d.subject)
    return c
