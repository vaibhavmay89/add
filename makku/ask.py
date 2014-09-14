import mechanize
br = mechanize.Browser()
br.open('http://www.askiitians.com/myaccount.aspx')
for f in br.forms():
    print f

print '\n\n\n\n\n'
print br.response()
NAME = 'tannu'
#password = 'sirhacksalot'
mobile = '123456789'
email = 'tannu@bikaner1.com'
br.select_form(nr =0)
br.form['txtfirstname'] = NAME 
#br.form['spnCountryName'] = '+91'
br.form['txtMobile'] = mobile
br.form['txtemailid'] = email
br.form['txtregpassword'] = password
br.form['txtconfirmpassword'] = password
#br.form['drpGrade'] = ['*', '6', '7', '8', '9', '10', '11', '12', '12th pass']
br.form['drpGrade'] = ['6']

br.submit(nr=1)

print '\n\n\n\n\n'
print br.response()
