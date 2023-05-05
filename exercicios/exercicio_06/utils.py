def is_already_registered_in_list(list_to_check, codigo_to_check) -> bool:
    for item in list_to_check:
        if item.codigo == codigo_to_check:
            return True
    return False
