from xml.etree.ElementTree import Element, dump, SubElement, ElementTree, parse

def indent(elem, level=0):
    i = "\n"+level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i+" "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and(not elem.tail or not elem.tail.strip()):
            elem.tail = i
# <blog date = "20180108", editor = "pycharm">
# <subject>Why python?</subject>
# <author>Eric
#   <age>58</age>
#   <nation>USA</nation>
# </author>
# <Agenda>
#   <a.>Data_Type</1.>
#   <b.>Controll_Flow</2.>
#   <c.>Function</3.>
# </Agenda>
# </blog>

blog = Element("blog")
subject = Element('subject')
subject.text = "Why python?"
blog.attrib["date"] = "20180108"
blog.attrib["editor"] = "pycharm"
blog.append(subject)

author = Element("author")
author.text = "Eric"
blog.append(author)
Agenda = Element("Agenda")
Agenda.text = ''
blog.append(Agenda)
SubElement(author, "age").text = "58"
SubElement(author, "nation").text = "USA"
SubElement(Agenda, "a").text = "Data Type"
SubElement(Agenda, "b").text = "Controll Flow"
SubElement(Agenda, "c").text = "Function"


indent(blog)
dump(blog)

print(blog.items())

# SubElement(note, "from").text = "Jani"
# SubElement(note, "to").text = "김기정"
# SubElement(note, "to").text = "김인한"
# SubElement(note, "to").text = "김건홍"
#
# from_tag = note.find("from")
# from_tags = note.findall("from")
# from_text = note.findtext("from")
#


# ElementTree(note).write("note.xml")
# tree = parse("note.xml")
# note = tree.getroot()
#
# # print(note.get("date"))
# # print(note.get("foo", "default"))
# # print(note.keys())
# # print(note.items())
#
# from_tag = note.find("from")
# print(from_tag)
# from_text = note.findtext("from")
# print(from_text)
# # from_tags = note.findall("from")
# to_tag = note.find("to")
# to_tags = note.findall("to")
#
# for to_element in to_tags:
#     print(to_element.text)
# print("end")


# childs = note.getiterator()
# childs = note.getchildren()

# print("end")
# note.getiterator("from")
#
# print("Search from root")
# for parent in note.getiterator():
#     for child in parent:
#         print(child.text)
#
# print("Search from from")
# for child in note.getiterator("from"):
#     print(child.text)