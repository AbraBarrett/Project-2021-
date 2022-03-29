from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/mainpage')
def main_page():
    try:
        if request.method=='post':
            import re
            import urllib.parse
            import urllib.request
            import bs4
            def getReport(myurl):
                try:
                    reponse = urllib.request.Request(myurl)
                    html = urllib.request.urlopen(reponse).read().decode("utf-8")
                    soup = bs4.BeautifulSoup(html, 'html.parser')
                    pattern = r'http://v.virscan.org/\w+'
                    vLinks = soup.find_all('a', href=re.compile(pattern))
                    if len(vLinks) == 0:
                        return 'safe'
                    else:
                        for vlink in vLinks:
                            url3 = urllib.parse.quote(vlink['href'])
                            url3 = url3.replace('http%3A', 'http:')
                            if vlink.has_attr('alt'):
                                return 'Unsafe'
                            else:
                                return 'safe'
                except:
                    return'Unsafe'

            if getReport(request.form.get('url'))=='safe':
                message='Это безопасный сайт'
                return render_template('mainpage.html', message=message)
            else:
                message='Сайт не безопасен'
                return render_template('mainpage.html',message=message)
    except:pass
    return render_template('mainpage.html')

@app.route('/vulnerabilities')
def contacts():
    return render_template('vulnerabilities.html')

@app.route('/antiviruses')
def new_things():
    return render_template('antiviruses.html')

if __name__ == '__main__':
    app.run()
