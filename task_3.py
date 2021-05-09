import re


def task_3():
    emails = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'
    domain_pattern = re.compile(r"@(\w+\.\w+)")
    list_domain = domain_pattern.findall(emails)

    return list_domain


if __name__ == '__main__':
    print(task_3())