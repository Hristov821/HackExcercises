import json
import os.path


def get_data(fname):
    with open(fname) as f:
        data = json.load(f)
    return data


def get_people(data):
    assert type(data) is dict,'data is not dict'
    assert 'people' in data,'People not in Dict'
    people = []
    for i in data['people']:
        people.append(i)
    return people


def generate_title(name):
    return '\n <title>{}</title>\n'.format(name)


def generate_link(css_file):
    return '<link rel="stylesheet" type="text/css" href="{}">'.format(css_file)


def generate_head(name, css_file):
    assert os.path.exists(css_file) is True,'css_file doesnt exists'
    name = generate_title(name)
    link = generate_link(css_file)
    first_part = """<!DOCTYPE html>
<html>
<head>"""
    second_part = ' \n</head> '
    start_body = '<body>'
    return '{0} {1} {2} {3} {4}'.format(first_part, name, link, second_part, start_body)


def start_div(gender, name, img):

    div_start = " \n<div class=""\"business-card {}\"> \n".format(gender)
    h1 = "<h1 class=\"full-name\">{} </h1> \n".format(name)
    img = '<img class="avatar" src=\"{}\"> \n'.format(img)
    return '{0} {1} {2}'.format(div_start, h1, img)


def base_info(age, birth_date, birt_place, gender):
    div_start = '<div class=\"base-info\"> \n'
    age_p = '<p>Age: {}</p> \n'.format(age)
    birth_date_p = ' <p>Birth date: {} </p> \n'.format(birth_date)
    birth_place_p = ' <p>Birth place: {}</p> \n'.format(birt_place)
    gener_p = ' <p>Gender: {}</p> \n'.format(gender)
    div_close = '</div> \n'
    return '{0} {1} {2} {3} {4} {5}'.format(div_start, age_p, birth_date_p, birth_place_p, gener_p, div_close)


def create_literal(str_in_literal):
    return ' <li>{}</li> \n'.format(str_in_literal)


def block(list_of_thigs, thing):
    start_div = ' <div class=\" {} \"> \n'.format(thing)
    h = '<h2> {} :</h2> \n'.format(thing)
    uls = '<ul> \n'
    for i in list_of_thigs:
        uls = '{0} {1}'.format(uls, create_literal(i))
    end_uld = '</ul> \n'
    end_div = '</div> \n'
    return '{0}{1}{2}{3}{4}'.format(start_div, h, uls, end_uld, end_div)


def end_Tags():
    tags = """ </div>  
	</body>
	</html>"""
    return tags


def parse_skils(person_skils):
    arr = []
    for i in person_skils:
        arr.append('{} - {}'.format(i['name'], i['level']))
    return arr

    return


def create_indentation_card_string(person):
    assert type(person) is dict,'Person type is not dict'
    img = person['avatar']
    assert os.path.exists(img) is True,'Image for this person doesnt exists'
    age = person['age']
    f_name = person['first_name']
    s_name = person['last_name']
    birth_date = person['birth_date']
    birth_place = person['birth_place']
    gender = person['gender']
    interests_list = person['interests']
    skils_list = parse_skils(person['skills'])

    head = generate_head('{0} {1}'.format(f_name, s_name), 'styles.css')
    div_start = start_div(gender, '{0} {1}'.format(
        f_name, s_name), '{}.png'.format(f_name))
    base_inf = base_info(age, birth_date, birth_place, gender)
    interests = block(interests_list, 'interest')

    skil = block(skils_list, 'skills')

    return '{0}{1}{2}{3}{4}{5}'.format(head, div_start, base_inf, interests, skil, end_Tags())


def write_in_file(data, fname):
    assert data is not None,'data is None'
    assert type(fname) is str,'fname is not string'
    with open(fname, 'w') as f:
        f.write(data)


def main():

    data = get_data('data.json')
    people=get_people(data)
    for i in people:
        if os.path.exists(i['avatar']):
            data = create_indentation_card_string(i)
            write_in_file(data,'{}.html'.format(i['first_name']))


if __name__ == "__main__":
    main()
