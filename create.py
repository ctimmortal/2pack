import webbrowser
from urllib.parse import urlencode, quote
import clipboard

packing_list = []

depart_list = {'task': 'Packing List',  'type': 2, 'saveInClipboard': 1, 'starred': 1, 'forList': 'Inbox'}
return_list = {'task': 'Packing List', 'type': 2, 'saveInClipboard': 1, 'starred': 1, 'forList': 'Inbox'}
base = 'twodo://x-callback-url/add?'
fin = '&x-success=pythonista://'


def dates_input():
    print('Format date as "yyyy-mm-dd" or "n", where n is a number of days from current date.')
    depart_list['due'] = input("Departure date: ")
    return_list['due'] = input("Return date: ")
    tag = input("Tag: ")
    depart_list['tag'] = tag
    return_list['tag'] = tag


def list_input():  # create packing list
    i = input("List item: ")
    if i:
        packing_list.append(i)
        list_input()
    else:
        return packing_list


def populate_checklist(TaskDict, PackingList):
    frag = urlencode(TaskDict, quote_via=quote)
    url = "{}{}{}".format(base, frag, fin)
    webbrowser.open(url)
    parent = clipboard.get()
    for item in PackingList:
        item_args = {'task': item,  'type': 0, 'forParentTask': parent}
        item_frag = urlencode(item_args, quote_via=quote)
        url = "{}{}{}".format(base, item_frag, fin)
        webbrowser.open(url)


def main():
    dates_input()
    list_input()
    
if __name__ == "__main__":
    main()
