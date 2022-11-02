from main import get_doc_owner_name, \
    get_all_doc_owners_names, \
    add_new_shelf, \
    delete_doc, \
    get_doc_shelf, \
    move_doc_to_shelf, \
    show_all_docs_info, \
    add_new_doc


def test_get_doc_owner_name():
    result = get_doc_owner_name("10006")
    assert "Аристарх Павлов" == result


def test_get_all_doc_owners_names():
    result = get_all_doc_owners_names()
    assert {'Геннадий Покемонов', 'Аристарх Павлов', 'Василий Гупкин'}== result


def test_show_all_docs_info():
    result = show_all_docs_info()
    assert ['passport "2207 876234" "Василий Гупкин"', 'invoice "11-2" "Геннадий Покемонов"', 'insurance "10006" "Аристарх Павлов"'] == result


def test_get_doc_shelf():
    result = get_doc_shelf("10006")
    assert "2" == result


def test_add_new_doc():
    result = add_new_doc("10006", "insurance", "Аристарх Павлов", "3")
    assert "3" == result


def test_delete_doc():
    result = delete_doc("10006")
    assert ("10006", True) == result


def test_move_doc_to_shelf():
    result = move_doc_to_shelf("10006", "3")
    assert ("10006", "3") == result


def test_add_new_shelf():
    result = add_new_shelf("4")
    assert ("4", True) == result
