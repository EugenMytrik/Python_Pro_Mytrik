def parse(query:str) -> dict:

    result_dict = {}

    if "?" in query:
        raw = query.split("?")[1]
        pairs = raw.split('&')
        
        for pair in pairs:
            if pair != "":
                key, value = pair.split('=')
                result_dict[key] = value
                
    return result_dict


if __name__ == "main":
    assert parse('https://example.com/path/to/page?name=eugene&surname=mytrik') == {'name': 'eugene', 'surname': 'mytrik'}
    assert parse('https://example.com/path/to/page?name=dima&surname=chub') == {'name': 'dima', 'surname': 'chub'}
    assert parse('https://example.com/path/to/page?name=boghdan&surname=ponomarenko') == {'name': 'boghdan', 'surname': 'ponomarenko'}
    assert parse('https://example.com/path/to/page?name=kratos&surname=god') == {'name': 'kratos', 'surname': 'god'}
    assert parse('https://example.com/path/to/page?name=hero&surname=') == {'name': 'hero', 'surname': ''}
    assert parse('https://example.com/path/to/page?name=&surname=') == {'name': '', 'surname': ''}
    assert parse('https://example.com/path/to/page') == {}
    assert parse('https://example.com/path/to/page?') == {}
    assert parse('https://example.com/path/to/page?name=kratos&surname=god&') == {'name': 'kratos', 'surname': 'god'}
    assert parse('https://example.com/path/to/page?&') == {}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}