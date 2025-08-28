# 1.
concate: list = ['thirty', 'days', 'of','python']
result: str = ' '.join(concate)
print(result.title())

# 2.
print('Coding'+' For '+'All')

# 3.
company: str = 'Coding For All'

# 4.
print(company)

# 5.
print(len(company))

# 6.
print(company.upper())

# 7.
print(company.lower())

# 8.
company_cap: str = company.capitalize()
company_title: str = company.title()
company_swap: str = company.swapcase()

company_str: str = 'This is Title: {}. This is Capitalize: {}. This is SwapCase: {}'.format(company_cap, company_title, company_swap)
print(company_str)

# 9.
cut = company[6:]
print(cut)

# 10.
print(company.find('Coding'))
sub_string = 'Coding'
print(company.index(sub_string))
