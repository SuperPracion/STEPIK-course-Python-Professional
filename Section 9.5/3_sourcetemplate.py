def sourcetemplate(url):
    def res(**kwargs):
        return url + ('?' if kwargs else '') + '&'.join([f'{k}={v}' for k, v in sorted(kwargs.items())])
    return res

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))